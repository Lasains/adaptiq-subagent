"""Unit tests for ArtifactManager read/write operations (PRD Section 2.1)."""

import os
import shutil
import pytest

from adaptiq.filesystem.artifact_manager import ArtifactManager

SESSION_DIR = "./test_session_artifacts"


@pytest.fixture(autouse=True)
def cleanup_session_dir():
    yield
    if os.path.exists(SESSION_DIR):
        shutil.rmtree(SESSION_DIR)


@pytest.mark.asyncio
async def test_write_and_read_artifact():
    """Written artifact content is read back identically."""
    manager = ArtifactManager(base_dir=SESSION_DIR)
    content = "# Chapter 1: Event Loop\n\nFormal definition here."

    path = await manager.write_artifact("sess_001", "materi.md", content)
    assert path.exists()

    read_back = await manager.read_artifact("sess_001", "materi.md")
    assert read_back == content


@pytest.mark.asyncio
async def test_session_dir_created_automatically():
    """Session directory is created if it does not exist."""
    manager = ArtifactManager(base_dir=SESSION_DIR)
    await manager.write_artifact("sess_new_123", "blackboard.json", '{"test": true}')

    assert os.path.exists(os.path.join(SESSION_DIR, "sess_new_123", "blackboard.json"))


@pytest.mark.asyncio
async def test_artifact_exists():
    """artifact_exists returns True after write and False before."""
    manager = ArtifactManager(base_dir=SESSION_DIR)

    exists_before = await manager.artifact_exists("sess_002", "submission.js")
    assert exists_before is False

    await manager.write_artifact("sess_002", "submission.js", "console.log('test')")
    exists_after = await manager.artifact_exists("sess_002", "submission.js")
    assert exists_after is True


@pytest.mark.asyncio
async def test_read_missing_artifact_raises():
    """Reading a non-existent artifact raises FileNotFoundError."""
    manager = ArtifactManager(base_dir=SESSION_DIR)
    with pytest.raises(FileNotFoundError):
        await manager.read_artifact("sess_003", "nonexistent.json")


@pytest.mark.asyncio
async def test_list_artifacts():
    """list_artifacts returns all written file names for a session."""
    manager = ArtifactManager(base_dir=SESSION_DIR)
    await manager.write_artifact("sess_004", "materi.md", "content")
    await manager.write_artifact("sess_004", "challenge.md", "challenge content")
    await manager.write_artifact("sess_004", "submission.js", "code")

    artifacts = await manager.list_artifacts("sess_004")
    assert "materi.md" in artifacts
    assert "challenge.md" in artifacts
    assert "submission.js" in artifacts
    assert len(artifacts) == 3


@pytest.mark.asyncio
async def test_write_multiple_artifacts_isolated():
    """Different sessions do not share artifacts."""
    manager = ArtifactManager(base_dir=SESSION_DIR)
    await manager.write_artifact("sess_A", "materi.md", "Session A content")
    await manager.write_artifact("sess_B", "materi.md", "Session B content")

    content_a = await manager.read_artifact("sess_A", "materi.md")
    content_b = await manager.read_artifact("sess_B", "materi.md")

    assert content_a == "Session A content"
    assert content_b == "Session B content"
