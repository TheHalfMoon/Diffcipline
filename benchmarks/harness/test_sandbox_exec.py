import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
PINNED_IMAGE = "python:3.12.11-slim-bookworm@sha256:519591d6871b7bc437060736b9f7456b8731f1499a57e22e6c285135ae657bf7"


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


SANDBOX = load("sandbox_exec", HERE / "sandbox_exec.py")
LOCAL_AGENT = load("local_agent", HERE / "local_agent.py")


class SandboxExecTests(unittest.TestCase):
    def test_image_must_be_digest_pinned(self) -> None:
        SANDBOX.validate_image(PINNED_IMAGE)
        with self.assertRaises(ValueError):
            SANDBOX.validate_image("python:3.12.11-slim-bookworm")

    def test_command_enforces_containment_and_drops_secrets(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            work = Path(directory)
            argv = SANDBOX.docker_command(
                PINNED_IMAGE,
                work,
                "python -V",
                "sandbox-test",
                4,
                16,
                {"GITHUB_TOKEN": "secret", "GH_TOKEN": "secret", "LANG": "C.UTF-8"},
            )
        joined = " ".join(argv)
        for required in (
            "--pull=never", "--network none", "--read-only", "--cap-drop ALL",
            "no-new-privileges:true", "--cpus 4", "--memory 16g", "--memory-swap 16g",
            "dst=/workspace", "PYTHONDONTWRITEBYTECODE=1",
        ):
            self.assertIn(required, joined)
        self.assertNotIn("GITHUB_TOKEN", joined)
        self.assertNotIn("GH_TOKEN", joined)
        self.assertEqual(PINNED_IMAGE, argv[-6])

    def test_invalid_resource_limits_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            work = Path(directory)
            with self.assertRaises(ValueError):
                SANDBOX.docker_command(PINNED_IMAGE, work, "true", "test", 0, 1)
            with self.assertRaises(ValueError):
                SANDBOX.docker_command(PINNED_IMAGE, work, "true", "test", 1, 0)

    def test_text_policy_rejects_network_and_git_push_before_execution(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            work = Path(directory)
            for command in ("git push origin main", "curl https://example.com"):
                result = json.loads(
                    LOCAL_AGENT.bash_tool(command, work, 1, PINNED_IMAGE, 1, 1)
                )
                self.assertEqual(126, result["exit_code"])
                self.assertIn("no-network/no-push", result["stderr"])


if __name__ == "__main__":
    unittest.main()
