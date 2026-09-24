"""Unit tests for SandboxExecutor Node.js harness (PRD Section 3.3)."""

import pytest

from adaptiq.tools.sandbox_executor import SandboxExecutor


@pytest.fixture
def sandbox():
    return SandboxExecutor()


@pytest.mark.asyncio
async def test_execute_valid_snippet(sandbox):
    """A valid console.log snippet returns exit code 0 and expected stdout."""
    result = await sandbox.execute_snippet("console.log('hello adaptiq');")
    assert result.passed is True
    assert "hello adaptiq" in result.stdout
    assert result.timed_out is False


@pytest.mark.asyncio
async def test_execute_math_output(sandbox):
    """Arithmetic expression output is correctly captured."""
    result = await sandbox.execute_snippet("console.log(2 + 2);")
    assert result.passed is True
    assert "4" in result.stdout.strip()


@pytest.mark.asyncio
async def test_syntax_error_captured(sandbox):
    """A syntax error returns non-zero exit code with stderr content."""
    result = await sandbox.execute_snippet("console.log(")
    assert result.passed is False
    assert result.exit_code != 0
    assert result.stderr != ""


@pytest.mark.asyncio
async def test_runtime_error_captured(sandbox):
    """A runtime exception (undefined variable) returns non-zero exit code."""
    result = await sandbox.execute_snippet("console.log(undefinedVariable);")
    assert result.passed is False
    assert result.exit_code != 0


@pytest.mark.asyncio
async def test_timeout_enforced(sandbox):
    """An infinite loop is forcibly killed and returns timed_out=True."""
    result = await sandbox.execute_snippet("while(true){}", timeout=1.0)
    assert result.timed_out is True
    assert result.passed is False


@pytest.mark.asyncio
async def test_execute_test_harness_pass(sandbox):
    """A reference solution passes its own unit test assertion."""
    submission = """
async function delayedEcho(value, delayMs) {
  return new Promise((resolve) => setTimeout(() => resolve(value), delayMs));
}
"""
    test_code = """
const res = await delayedEcho('hello', 10);
assert.strictEqual(res, 'hello');
"""
    result = await sandbox.execute_test_harness(submission, test_code)
    assert result.passed is True


@pytest.mark.asyncio
async def test_execute_test_harness_fail(sandbox):
    """A broken implementation fails the assertion and returns exit code 1."""
    submission = """
async function delayedEcho(value, delayMs) {
  return 'wrong_value';
}
"""
    test_code = """
const res = await delayedEcho('hello', 10);
assert.strictEqual(res, 'hello');
"""
    result = await sandbox.execute_test_harness(submission, test_code)
    assert result.passed is False
    assert "TEST_FAILURE" in result.stderr or result.exit_code != 0
