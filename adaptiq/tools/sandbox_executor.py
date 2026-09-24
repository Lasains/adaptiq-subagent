"""Sandboxed Node.js 20+ execution harness with timeout guards."""

from __future__ import annotations

import asyncio
import os
import shutil
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Optional


@dataclass
class ExecutionResult:
    stdout: str
    stderr: str
    exit_code: int
    timed_out: bool = False

    @property
    def passed(self) -> bool:
        return self.exit_code == 0 and not self.timed_out


class SandboxExecutor:
    """Safely executes JavaScript in an isolated Node.js child process."""

    def __init__(
        self,
        node_path: Optional[str] = None,
        default_timeout_seconds: float = 5.0,
    ):
        self.node_path = node_path or os.getenv("ADAPTIQ_NODE_PATH", "node")
        self.default_timeout = float(
            os.getenv("ADAPTIQ_SANDBOX_TIMEOUT_SECONDS", default_timeout_seconds)
        )

        # Check if node exists in system
        if not shutil.which(self.node_path):
            raise EnvironmentError(
                f"Node.js binary '{self.node_path}' not found in PATH."
            )

    async def execute_snippet(
        self, code: str, timeout: Optional[float] = None
    ) -> ExecutionResult:
        """Execute a standalone JavaScript snippet."""
        timeout = timeout or self.default_timeout
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".js", delete=False, encoding="utf-8"
        ) as tmp:
            tmp.write(code)
            tmp_path = tmp.name

        try:
            proc = await asyncio.create_subprocess_exec(
                self.node_path,
                tmp_path,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
            )

            try:
                stdout_bytes, stderr_bytes = await asyncio.wait_for(
                    proc.communicate(), timeout=timeout
                )
                return ExecutionResult(
                    stdout=stdout_bytes.decode("utf-8", errors="replace"),
                    stderr=stderr_bytes.decode("utf-8", errors="replace"),
                    exit_code=proc.returncode if proc.returncode is not None else 1,
                    timed_out=False,
                )
            except asyncio.TimeoutError:
                try:
                    proc.kill()
                except ProcessLookupError:
                    pass
                return ExecutionResult(
                    stdout="",
                    stderr=f"Execution timed out after {timeout} seconds.",
                    exit_code=-1,
                    timed_out=True,
                )
        finally:
            try:
                os.remove(tmp_path)
            except OSError:
                pass

    async def execute_test_harness(
        self, submission_code: str, test_code: str, timeout: Optional[float] = None
    ) -> ExecutionResult:
        """Combine submission code and assertion test code and execute."""
        harness = f"""
// === SUBMISSION CODE ===
{submission_code}

// === ASSERTION HARNESS ===
const assert = require('assert');
(async () => {{
  try {{
{test_code}
  }} catch (err) {{
    console.error('TEST_FAILURE:', err.message);
    process.exit(1);
  }}
}})();
"""
        return await self.execute_snippet(harness, timeout=timeout)
