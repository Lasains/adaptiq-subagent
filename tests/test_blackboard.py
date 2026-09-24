"""Unit tests for Blackboard state store (PRD Section 2.3)."""

import asyncio
import os
import pytest
import pytest_asyncio

from adaptiq.state.blackboard import BlackboardStore, BlackboardState


DB_PATH = "test_blackboard.db"


@pytest.fixture(autouse=True)
def cleanup_db():
    yield
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    if os.path.exists(DB_PATH + "-wal"):
        os.remove(DB_PATH + "-wal")
    if os.path.exists(DB_PATH + "-shm"):
        os.remove(DB_PATH + "-shm")


@pytest.mark.asyncio
async def test_create_session():
    """Creating a new session returns a properly initialized BlackboardState."""
    store = BlackboardStore(db_path=DB_PATH)
    state = await store.get_or_create("sess_001", "learner_001", "JavaScript Event Loop")

    assert state.session_id == "sess_001"
    assert state.learner_id == "learner_001"
    assert state.current_topic == "JavaScript Event Loop"
    assert state.current_chapter == 1
    assert state.attempt_count == 1
    assert state.remediation_triggered is False
    assert state.last_assessment_score is None
    await store.close()


@pytest.mark.asyncio
async def test_write_and_read_back():
    """Values written to blackboard are correctly retrieved on read."""
    store = BlackboardStore(db_path=DB_PATH)
    await store.get_or_create("sess_002", "learner_002", "Closures")

    updated = await store.update("sess_002", last_assessment_score=0.75, current_chapter=2)
    assert updated.last_assessment_score == 0.75
    assert updated.current_chapter == 2

    re_read = await store.read("sess_002")
    assert re_read is not None
    assert re_read.last_assessment_score == 0.75
    assert re_read.current_chapter == 2
    await store.close()


@pytest.mark.asyncio
async def test_write_three_keys():
    """Write 3 separate keys and verify all persist correctly."""
    store = BlackboardStore(db_path=DB_PATH)
    await store.get_or_create("sess_003", "learner_003", "Prototypes")

    await store.update("sess_003", attempt_count=2)
    await store.update("sess_003", remediation_triggered=True)
    await store.update("sess_003", current_chapter=3)

    state = await store.read("sess_003")
    assert state is not None
    assert state.attempt_count == 2
    assert state.remediation_triggered is True
    assert state.current_chapter == 3
    await store.close()


@pytest.mark.asyncio
async def test_agent_lock():
    """Locking and unlocking an agent modifies the agent_locks field."""
    store = BlackboardStore(db_path=DB_PATH)
    await store.get_or_create("sess_004", "learner_004", "Async/Await")

    await store.lock_agent("sess_004", "tutor", locked=True)
    state = await store.read("sess_004")
    assert state is not None
    assert state.agent_locks.tutor is True

    await store.lock_agent("sess_004", "tutor", locked=False)
    state = await store.read("sess_004")
    assert state is not None
    assert state.agent_locks.tutor is False
    await store.close()


@pytest.mark.asyncio
async def test_get_or_create_idempotent():
    """Calling get_or_create twice for the same session_id does not duplicate."""
    store = BlackboardStore(db_path=DB_PATH)
    s1 = await store.get_or_create("sess_005", "learner_005", "Topic A")
    # Update something so we can detect if it's reset
    await store.update("sess_005", current_chapter=5)

    # Calling get_or_create again should return existing (not reset)
    s2 = await store.get_or_create("sess_005", "learner_005", "Topic A")
    assert s2.current_chapter == 5
    await store.close()
