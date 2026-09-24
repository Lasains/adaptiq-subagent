"""LearnerProfile models and storage for cognitive diagnostic tracking."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Literal, Optional
import aiofiles
import aiosqlite
from pydantic import BaseModel, Field

AbstractionPreference = Literal[
    "visual_spatial", "formal_symbolic", "narrative", "mixed"
]
ExplanationModality = Literal["standard", "aphantasia_adapted", "hybrid"]


class CognitiveTraits(BaseModel):
    visual_imagery_score: float = 5.0  # 0 (Aphantasic) - 10 (Hyper-phantasic)
    visual_imagery_score_history: list[float] = Field(default_factory=lambda: [5.0])
    abstraction_preference: AbstractionPreference = "mixed"
    pacing_score: float = 5.0
    preferred_explanation_modality: ExplanationModality = "standard"


class AphantasiaIndicators(BaseModel):
    spatial_metaphor_confusion_events: int = 0
    formal_syntax_high_comprehension_events: int = 0
    score_delta_last_3_sessions: float = 0.0


class Progression(BaseModel):
    topics_completed: list[str] = Field(default_factory=list)
    topics_in_progress: list[str] = Field(default_factory=list)
    topics_pending: list[str] = Field(default_factory=list)


class LearnerProfile(BaseModel):
    learner_id: str
    updated_at: str = Field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )
    cognitive_traits: CognitiveTraits = Field(default_factory=CognitiveTraits)
    diagnostic_confidence: float = 0.5  # 0.0 to 1.0
    current_misconceptions: list[str] = Field(default_factory=list)
    resolved_misconceptions: list[str] = Field(default_factory=list)
    aphantasia_indicators: AphantasiaIndicators = Field(
        default_factory=AphantasiaIndicators
    )
    progression: Progression = Field(default_factory=Progression)


def create_default_profile(learner_id: str) -> LearnerProfile:
    """Factory function for initializing a new learner profile."""
    return LearnerProfile(
        learner_id=learner_id,
        cognitive_traits=CognitiveTraits(
            visual_imagery_score=5.0,
            visual_imagery_score_history=[5.0],
            abstraction_preference="mixed",
            pacing_score=5.0,
            preferred_explanation_modality="standard",
        ),
        diagnostic_confidence=0.5,
    )


class ProfileStore:
    """Persistent storage for LearnerProfile with SQLite + JSON fallback."""

    def __init__(self, db_path: str = "adaptiq.db"):
        self.db_path = db_path
        self._db: Optional[aiosqlite.Connection] = None

    async def connect(self) -> aiosqlite.Connection:
        if self._db is None:
            self._db = await aiosqlite.connect(self.db_path)
            await self._db.execute("PRAGMA journal_mode = WAL;")
            await self._db.execute(
                """
                CREATE TABLE IF NOT EXISTS learner_profiles (
                    learner_id TEXT PRIMARY KEY,
                    profile_json TEXT NOT NULL,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
                """
            )
            await self._db.commit()
        return self._db

    async def load(
        self, learner_id: str, default_if_missing: bool = True
    ) -> LearnerProfile:
        db = await self.connect()
        async with db.execute(
            "SELECT profile_json FROM learner_profiles WHERE learner_id = ?",
            (learner_id,),
        ) as cursor:
            row = await cursor.fetchone()
            if row:
                data = json.loads(row[0])
                return LearnerProfile.model_validate(data)

        if default_if_missing:
            default_profile = create_default_profile(learner_id)
            await self.save(default_profile)
            return default_profile

        raise ValueError(f"Profile for learner '{learner_id}' not found.")

    async def save(self, profile: LearnerProfile) -> None:
        profile.updated_at = datetime.now(timezone.utc).isoformat()
        db = await self.connect()
        await db.execute(
            """
            INSERT INTO learner_profiles (learner_id, profile_json, updated_at)
            VALUES (?, ?, CURRENT_TIMESTAMP)
            ON CONFLICT(learner_id) DO UPDATE SET
                profile_json = excluded.profile_json,
                updated_at = CURRENT_TIMESTAMP
            """,
            (profile.learner_id, json.dumps(profile.model_dump())),
        )
        await db.commit()

    async def close(self) -> None:
        if self._db:
            await self._db.close()
            self._db = None
