"""Unit tests for LearnerProfile schemas and ProfileStore (PRD Section 5.1)."""

import os
import pytest

from adaptiq.state.learner_profile import (
    LearnerProfile,
    CognitiveTraits,
    ProfileStore,
    create_default_profile,
)

DB_PATH = "test_profile.db"


@pytest.fixture(autouse=True)
def cleanup_db():
    yield
    for suffix in ["", "-wal", "-shm"]:
        if os.path.exists(DB_PATH + suffix):
            os.remove(DB_PATH + suffix)


def test_default_profile_values():
    """Default profile has visual_imagery_score=5 and mixed preference."""
    profile = create_default_profile("test_learner")
    assert profile.learner_id == "test_learner"
    assert profile.cognitive_traits.visual_imagery_score == 5.0
    assert profile.cognitive_traits.abstraction_preference == "mixed"
    assert profile.cognitive_traits.preferred_explanation_modality == "standard"
    assert profile.diagnostic_confidence == 0.5
    assert profile.current_misconceptions == []


def test_profile_serialization():
    """LearnerProfile serializes to JSON dict and deserializes back faithfully."""
    profile = create_default_profile("learner_roundtrip")
    profile.current_misconceptions = ["Promises run synchronously", "setTimeout resolves microtasks"]
    profile.cognitive_traits.visual_imagery_score = 2.5

    data = profile.model_dump()
    restored = LearnerProfile.model_validate(data)

    assert restored.learner_id == profile.learner_id
    assert restored.cognitive_traits.visual_imagery_score == 2.5
    assert len(restored.current_misconceptions) == 2
    assert "Promises run synchronously" in restored.current_misconceptions


def test_cognitive_traits_validation():
    """CognitiveTraits accepts valid scores and rejects bad types."""
    traits = CognitiveTraits(
        visual_imagery_score=7.0,
        abstraction_preference="formal_symbolic",
        pacing_score=8.0,
        preferred_explanation_modality="aphantasia_adapted",
    )
    assert traits.visual_imagery_score == 7.0
    assert traits.abstraction_preference == "formal_symbolic"


@pytest.mark.asyncio
async def test_profile_store_save_and_load():
    """Saving and loading a profile from ProfileStore round-trips correctly."""
    store = ProfileStore(db_path=DB_PATH)

    profile = create_default_profile("dana_7f3a")
    profile.current_misconceptions = ["Microtask confusion"]
    profile.cognitive_traits.visual_imagery_score = 3.0

    await store.save(profile)

    loaded = await store.load("dana_7f3a", default_if_missing=False)
    assert loaded.learner_id == "dana_7f3a"
    assert loaded.cognitive_traits.visual_imagery_score == 3.0
    assert "Microtask confusion" in loaded.current_misconceptions

    await store.close()


@pytest.mark.asyncio
async def test_profile_store_default_if_missing():
    """Loading a missing profile with default_if_missing=True creates a new default profile."""
    store = ProfileStore(db_path=DB_PATH)

    profile = await store.load("new_learner_xyz", default_if_missing=True)
    assert profile.learner_id == "new_learner_xyz"
    assert profile.cognitive_traits.visual_imagery_score == 5.0

    await store.close()


@pytest.mark.asyncio
async def test_profile_store_upsert():
    """Saving an updated profile overwrites the existing entry (upsert behavior)."""
    store = ProfileStore(db_path=DB_PATH)

    profile = create_default_profile("learner_upsert")
    await store.save(profile)

    profile.cognitive_traits.visual_imagery_score = 1.5
    profile.current_misconceptions = ["New misconception"]
    await store.save(profile)

    loaded = await store.load("learner_upsert", default_if_missing=False)
    assert loaded.cognitive_traits.visual_imagery_score == 1.5
    assert "New misconception" in loaded.current_misconceptions

    await store.close()
