"""Sandboxed Node.js 20+ execution harness with timeout guards."""

from __future__ import annotations

import asyncio
import os
import re
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
    """Safely executes JavaScript and Java in an isolated child process."""

    def __init__(
        self,
        node_path: Optional[str] = None,
        default_timeout_seconds: float = 5.0,
        java_path: Optional[str] = None,
        javac_path: Optional[str] = None,
    ):
        self.node_path = node_path or os.getenv("ADAPTIQ_NODE_PATH", "node")
        self.java_path = java_path or os.getenv("ADAPTIQ_JAVA_PATH", shutil.which("java") or "java")
        self.javac_path = javac_path or os.getenv("ADAPTIQ_JAVAC_PATH", shutil.which("javac") or "javac")
        self.default_timeout = float(
            os.getenv("ADAPTIQ_SANDBOX_TIMEOUT_SECONDS", default_timeout_seconds)
        )

        # Check if node exists in system
        if not shutil.which(self.node_path):
            raise EnvironmentError(
                f"Node.js binary '{self.node_path}' not found in PATH."
            )

    async def execute_java_snippet(
        self, code: str, timeout: Optional[float] = None
    ) -> ExecutionResult:
        """Compile and execute a standalone Java snippet (JDK 21+)."""
        timeout = timeout or self.default_timeout
        temp_dir = tempfile.mkdtemp()
        try:
            # Detect class name if declared, otherwise wrap in public class Main
            match = re.search(r"public\s+class\s+([A-Za-z0-9_]+)", code)
            if match:
                class_name = match.group(1)
                java_source = code
            elif "class " in code:
                match_class = re.search(r"class\s+([A-Za-z0-9_]+)", code)
                class_name = match_class.group(1) if match_class else "Main"
                java_source = code
            else:
                class_name = "Main"
                java_source = f"""public class Main {{
    public static void main(String[] args) {{
{code}
    }}
}}"""

            file_path = os.path.join(temp_dir, f"{class_name}.java")
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(java_source)

            # Compile step
            compile_proc = await asyncio.create_subprocess_exec(
                self.javac_path,
                f"{class_name}.java",
                cwd=temp_dir,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
            )
            c_out, c_err = await asyncio.wait_for(compile_proc.communicate(), timeout=timeout)
            if compile_proc.returncode != 0:
                return ExecutionResult(
                    stdout=c_out.decode("utf-8", errors="replace"),
                    stderr=c_err.decode("utf-8", errors="replace"),
                    exit_code=compile_proc.returncode or 1,
                    timed_out=False,
                )

            # Run step
            run_proc = await asyncio.create_subprocess_exec(
                self.java_path,
                class_name,
                cwd=temp_dir,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
            )
            r_out, r_err = await asyncio.wait_for(run_proc.communicate(), timeout=timeout)
            return ExecutionResult(
                stdout=r_out.decode("utf-8", errors="replace"),
                stderr=r_err.decode("utf-8", errors="replace"),
                exit_code=run_proc.returncode if run_proc.returncode is not None else 0,
                timed_out=False,
            )
        except asyncio.TimeoutError:
            return ExecutionResult(
                stdout="",
                stderr=f"Execution timed out after {timeout} seconds.",
                exit_code=-1,
                timed_out=True,
            )
        except Exception as e:
            return ExecutionResult(
                stdout="",
                stderr=f"Java Execution Exception: {e}",
                exit_code=1,
                timed_out=False,
            )
        finally:
            shutil.rmtree(temp_dir, ignore_errors=True)

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
