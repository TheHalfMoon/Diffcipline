import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


ADAPTER = load("executor_adapter", HERE / "executor_adapter.py")
RUN_ARM = load("run_arm", HERE / "run_arm.py")


class ExecutorAdapterTests(unittest.TestCase):
    def invoke(self, work: Path, prompt: dict, transcript: Path, treatment: Path | None = None):
        command = [
            sys.executable, "-S", str(HERE / "executor_adapter.py"),
            "--adapter-kind", "contract-test",
            "--workdir", str(work),
            "--prompt", json.dumps(prompt, sort_keys=True),
            "--transcript", str(transcript),
            "--timeout-seconds", "2",
        ]
        if treatment:
            command += ["--treatment", str(treatment)]
        return subprocess.run(command, text=True, capture_output=True)

    def test_reference_adapter_builds_local_agent_command(self) -> None:
        namespace = type("Args", (), {
            "base_url": "http://127.0.0.1:8080/v1",
            "model": "model",
            "workdir": Path("/work"),
            "prompt": "task",
            "transcript": Path("/out/transcript.md"),
            "timeout_seconds": 480,
            "treatment": Path("/skill.md"),
        })()
        command = ADAPTER.local_command(Path("/repo"), namespace)
        self.assertIn("/repo/benchmarks/harness/local_agent.py", command)
        self.assertIn("--skill", command)
        self.assertIn("/skill.md", command)

    def test_contract_test_write_preserves_treatment_and_transcript(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            work = Path(directory)
            treatment = work / "skill.md"
            treatment.write_text("exact treatment bytes\n", encoding="utf-8")
            transcript = work / "transcript.md"
            done = self.invoke(
                work, {"action": "write", "path": "src/result.txt", "content": "ok\n"},
                transcript, treatment,
            )
            self.assertEqual(0, done.returncode)
            self.assertEqual("ok\n", (work / "src/result.txt").read_text(encoding="utf-8"))
            self.assertIn("contract-test wrote src/result.txt", done.stdout)
            text = transcript.read_text(encoding="utf-8")
            self.assertIn("exact treatment bytes", text)
            self.assertIn('"action": "write"', text)

    def test_contract_test_exit_preserves_streams_and_exit_code(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            work = Path(directory)
            done = self.invoke(
                work, {"action": "exit", "code": 7, "stdout": "out\n", "stderr": "err\n"},
                work / "transcript.md",
            )
            self.assertEqual(7, done.returncode)
            self.assertEqual("out\n", done.stdout)
            self.assertEqual("err\n", done.stderr)

    def test_contract_test_rejects_workspace_escape(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            work = Path(directory)
            transcript = work / "transcript.md"
            done = self.invoke(
                work, {"action": "write", "path": "../escape.txt", "content": "bad"},
                transcript,
            )
            self.assertEqual(2, done.returncode)
            self.assertIn("stay inside workdir", done.stderr)
            self.assertIn("Adapter error", transcript.read_text(encoding="utf-8"))
            self.assertFalse((work.parent / "escape.txt").exists())

    def test_capture_process_preserves_exit_and_streams(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            code, stdout, stderr, timed_out = RUN_ARM.capture_process(
                [sys.executable, "-S", "-c", "import sys; print('out'); print('err', file=sys.stderr); sys.exit(9)"],
                Path(directory), 1, grace_seconds=0,
            )
            self.assertEqual((9, "out\n", "err\n", False), (code, stdout, stderr, timed_out))

    def test_capture_process_preserves_timeout_as_124(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            code, stdout, stderr, timed_out = RUN_ARM.capture_process(
                [sys.executable, "-S", "-c", "import time; time.sleep(1)"],
                Path(directory), 0.05, grace_seconds=0,
            )
            self.assertEqual(124, code)
            self.assertTrue(timed_out)
            self.assertEqual("", stdout)
            self.assertEqual("", stderr)

    def test_arm_orchestration_uses_adapter_and_blocks_contract_test(self) -> None:
        root = Path("/repo")
        command = RUN_ARM.build_adapter_command(
            root, "local-openai-tool-loop", Path("/work"), "task", Path("/out/transcript.md"),
            480, "model", "http://127.0.0.1:8080/v1", Path("/skill.md"),
        )
        self.assertIn(str(root / "benchmarks/harness/executor_adapter.py"), command)
        self.assertNotIn(str(root / "benchmarks/harness/local_agent.py"), command)
        with self.assertRaises(ValueError):
            RUN_ARM.validate_adapter_for_arm("contract-test")


if __name__ == "__main__":
    unittest.main()
