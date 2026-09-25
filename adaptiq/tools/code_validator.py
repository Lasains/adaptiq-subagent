"""Code validator for extracting and validating JavaScript snippets in markdown."""

from __future__ import annotations

import re
from typing import Optional

from adaptiq.tools.sandbox_executor import SandboxExecutor


class CodeValidator:
    """Validates JavaScript and Java code blocks within markdown documents using SandboxExecutor."""

    def __init__(self, sandbox: Optional[SandboxExecutor] = None):
        self.sandbox = sandbox or SandboxExecutor()
        self.pattern = re.compile(r"```(?:javascript|js)\s*\n(.*?)```", re.DOTALL | re.IGNORECASE)
        self.java_pattern = re.compile(r"```(?:java)\s*\n(.*?)```", re.DOTALL | re.IGNORECASE)

    def extract_code_blocks(self, markdown_text: str) -> list[str]:
        """Extract all JavaScript/JS fenced code snippets from markdown."""
        return [match.strip() for match in self.pattern.findall(markdown_text)]

    def extract_java_blocks(self, markdown_text: str) -> list[str]:
        """Extract all Java fenced code snippets from markdown."""
        return [match.strip() for match in self.java_pattern.findall(markdown_text)]

    async def validate_markdown(
        self, markdown_text: str, timeout: Optional[float] = 3.0
    ) -> tuple[bool, list[str]]:
        """Validate all JS and Java snippets in markdown.

        Returns (is_valid, error_messages).
        """
        js_snippets = self.extract_code_blocks(markdown_text)
        java_snippets = self.extract_java_blocks(markdown_text)
        errors: list[str] = []

        for idx, snippet in enumerate(js_snippets, start=1):
            if not snippet:
                continue
            res = await self.sandbox.execute_snippet(snippet, timeout=timeout)
            if not res.passed:
                err_detail = res.stderr.strip() or f"Exit code {res.exit_code}"
                errors.append(f"JS Snippet #{idx} failed execution: {err_detail}")

        for idx, snippet in enumerate(java_snippets, start=1):
            if not snippet:
                continue
            res = await self.sandbox.execute_java_snippet(snippet, timeout=timeout)
            if not res.passed:
                err_detail = res.stderr.strip() or f"Exit code {res.exit_code}"
                errors.append(f"Java Snippet #{idx} failed compilation/execution: {err_detail}")

        return (len(errors) == 0, errors)
