#!/usr/bin/env python3
import argparse, json, os, re, subprocess, time, urllib.error, urllib.request
from pathlib import Path

BLOCKED = re.compile(
    r"(?ix)(\bcurl\b|\bwget\b|\bssh\b|\bscp\b|\bsftp\b|\bftp\b|\btelnet\b|\bnc\b|\bncat\b|"
    r"\bgh\b|\bgit\s+(push|fetch|pull|clone)\b|\bpip3?\s+install\b|\bnpm\s+install\b|"
    r"\bpnpm\s+(add|install)\b|\bcargo\s+add\b|\bapt(-get)?\b|https?://)"
)
MAX_OUTPUT = 12000

def post_json(url, payload, timeout):
    req = urllib.request.Request(url, data=json.dumps(payload).encode(), headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            return json.load(response)
    except urllib.error.HTTPError as error:
        raise RuntimeError(f"provider HTTP {error.code}: {error.read().decode(errors='replace')}") from error

def trim(text):
    if len(text) <= MAX_OUTPUT:
        return text
    half = MAX_OUTPUT // 2
    return text[:half] + "\n...[truncated]...\n" + text[-half:]

def record(path, title, body):
    with path.open("a", encoding="utf-8") as handle:
        handle.write(f"## {title}\n\n{body.rstrip()}\n\n")

def bash_tool(command, cwd, timeout):
    if BLOCKED.search(command):
        return json.dumps({"exit_code": 126, "stdout": "", "stderr": "rejected by no-network/no-push policy"}, sort_keys=True)
    env = os.environ.copy()
    for key in ("GITHUB_TOKEN", "GH_TOKEN", "ACTIONS_RUNTIME_TOKEN", "ACTIONS_ID_TOKEN_REQUEST_TOKEN"):
        env.pop(key, None)
    try:
        done = subprocess.run(["bash", "-lc", command], cwd=cwd, env=env, text=True, capture_output=True, timeout=max(1, timeout))
        result = {"exit_code": done.returncode, "stdout": trim(done.stdout), "stderr": trim(done.stderr)}
    except subprocess.TimeoutExpired as error:
        stdout = error.stdout.decode(errors="replace") if isinstance(error.stdout, bytes) else error.stdout or ""
        stderr = error.stderr.decode(errors="replace") if isinstance(error.stderr, bytes) else error.stderr or ""
        result = {"exit_code": 124, "stdout": trim(stdout), "stderr": trim(stderr + "\ncommand timed out")}
    return json.dumps(result, sort_keys=True)

def tools(has_skill):
    result = [{"type": "function", "function": {
        "name": "bash",
        "description": "Run one synchronous shell command in the current repository. Returns exit_code, stdout, stderr. No network, installs, commits, pushes, or gh.",
        "parameters": {"type": "object", "properties": {"command": {"type": "string"}}, "required": ["command"], "additionalProperties": False},
    }}]
    if has_skill:
        result.append({"type": "function", "function": {
            "name": "skill",
            "description": "Load the exact installed behavioral skill. Call once before changing files.",
            "parameters": {"type": "object", "properties": {}, "additionalProperties": False},
        }})
    return result

def arguments(value):
    value = json.loads(value) if isinstance(value, str) else value
    if not isinstance(value, dict):
        raise ValueError("tool arguments must be an object")
    return value

def run_agent(base_url, model, workdir, prompt, transcript, timeout_seconds, skill=None):
    deadline = time.monotonic() + timeout_seconds
    transcript.parent.mkdir(parents=True, exist_ok=True)
    transcript.write_text("# Local agent transcript\n\n", encoding="utf-8")
    system = (
        "You are a coding agent operating only in the current repository. Use only provided tools. "
        "bash is synchronous and directly returns exit_code, stdout, and stderr; never invent lifecycle tools. "
        "Do not use network resources, install dependencies, commit, push, or use gh. "
        "Inspect before editing, make the smallest correct change, run repository tests, then finish concisely."
    )
    if skill:
        system += " A behavioral skill is installed. You MUST call skill exactly once before changing files and follow it."
    messages = [{"role": "system", "content": system}, {"role": "user", "content": prompt}]
    available = tools(skill is not None)
    skill_text = skill.read_text(encoding="utf-8") if skill else None
    record(transcript, "User", prompt)

    for step in range(48):
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            record(transcript, "Timeout", "Global agent timeout reached.")
            return 124, ""
        payload = {
            "model": model, "messages": messages, "tools": available, "tool_choice": "auto",
            "temperature": 0, "top_p": 1, "seed": 1, "max_tokens": 768, "stream": False,
        }
        response = post_json(base_url.rstrip("/") + "/chat/completions", payload, remaining)
        choices = response.get("choices") or []
        if not choices:
            raise RuntimeError(f"provider returned no choices: {response}")
        message = choices[0].get("message") or {}
        content, calls = message.get("content") or "", message.get("tool_calls") or []
        if content:
            record(transcript, "Assistant", content)
        if not calls:
            return 0, content
        calls = [dict(call, id=call.get("id") or f"call_{step}_{i}") for i, call in enumerate(calls)]
        messages.append({"role": "assistant", "content": content or None, "tool_calls": calls})
        for call in calls:
            function, result = call.get("function") or {}, None
            name = function.get("name")
            try:
                args = arguments(function.get("arguments", {}))
                if name == "bash":
                    command = args.get("command")
                    if not isinstance(command, str) or not command.strip():
                        result = json.dumps({"error": "bash.command must be a non-empty string"})
                    else:
                        result = bash_tool(command, workdir, min(120, max(1, deadline - time.monotonic())))
                        record(transcript, "Tool: bash", f"```sh\n{command}\n```\n\n```json\n{result}\n```")
                elif name == "skill" and skill_text is not None:
                    result = skill_text
                    record(transcript, "Tool: skill", skill_text)
                else:
                    result = json.dumps({"error": f"unknown or unavailable tool: {name}"})
            except (ValueError, json.JSONDecodeError) as error:
                result = json.dumps({"error": f"invalid tool arguments: {error}"})
            messages.append({"role": "tool", "tool_call_id": call["id"], "content": result})
    record(transcript, "Failure", "Maximum agent tool steps reached.")
    return 2, ""

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-url", required=True)
    parser.add_argument("--model", required=True)
    parser.add_argument("--workdir", required=True, type=Path)
    parser.add_argument("--prompt", required=True)
    parser.add_argument("--transcript", required=True, type=Path)
    parser.add_argument("--timeout-seconds", type=int, default=480)
    parser.add_argument("--skill", type=Path)
    args = parser.parse_args()
    try:
        code, final = run_agent(
            args.base_url, args.model, args.workdir.resolve(), args.prompt, args.transcript.resolve(),
            args.timeout_seconds, args.skill.resolve() if args.skill else None,
        )
    except Exception as error:
        record(args.transcript.resolve(), "Agent error", repr(error))
        print(f"agent error: {error}", file=os.sys.stderr)
        return 2
    if final:
        print(final)
    return code

if __name__ == "__main__":
    raise SystemExit(main())
