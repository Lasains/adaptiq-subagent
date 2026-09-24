"""Blackboard state store and schemas for AdaptIQ multi-agent orchestration."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Optional
import aiosqlite
from pydantic import BaseModel, Field


class AgentLocks(BaseModel):
    tutor: bool = False
    assessor: bool = False
    diagnostician: bool = False


class TokenBudget(BaseModel):
    session_total_tokens: int = 0
    tutor_budget_per_call: int = 4096
    assessor_budget_per_call: int = 2048
    diagnostician_budget_per_call: int = 1024


class BlackboardState(BaseModel):
    session_id: str
    learner_id: str
    current_topic: str
    current_chapter: int = 1
    attempt_count: int = 1
    remediation_triggered: bool = False
    escalation_flag: bool = False
    pending_diagnostic_payload: Optional[dict[str, Any]] = None
    last_assessment_score: Optional[float] = None
    agent_locks: AgentLocks = Field(default_factory=AgentLocks)
    token_budget: TokenBudget = Field(default_factory=TokenBudget)


class BlackboardStore:
    """Asynchronous SQLite-backed Blackboard storage with WAL mode support."""

    def __init__(self, db_path: str = "adaptiq.db"):
        self.db_path = db_path
        self._db: Optional[aiosqlite.Connection] = None

    async def connect(self) -> aiosqlite.Connection:
        if self._db is None:
            self._db = await aiosqlite.connect(self.db_path)
            # Enable WAL mode for high concurrency
            await self._db.execute("PRAGMA journal_mode = WAL;")
            await self._db.execute("PRAGMA synchronous = NORMAL;")
            await self._init_tables()
        return self._db

    async def _init_tables(self) -> None:
        assert self._db is not None
        await self._db.execute(
            """
            CREATE TABLE IF NOT EXISTS blackboard (
                session_id TEXT PRIMARY KEY,
                learner_id TEXT NOT NULL,
                current_topic TEXT NOT NULL,
                state_json TEXT NOT NULL,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        await self._db.commit()

    async def get_or_create(
        self, session_id: str, learner_id: str, topic: str
    ) -> BlackboardState:
        db = await self.connect()
        async with db.execute(
            "SELECT state_json FROM blackboard WHERE session_id = ?", (session_id,)
        ) as cursor:
            row = await cursor.fetchone()
            if row:
                data = json.loads(row[0])
                return BlackboardState.model_validate(data)

        # Create new state
        new_state = BlackboardState(
            session_id=session_id, learner_id=learner_id, current_topic=topic
        )
        await db.execute(
            """
            INSERT INTO blackboard (session_id, learner_id, current_topic, state_json)
            VALUES (?, ?, ?, ?)
            """,
            (session_id, learner_id, topic, json.dumps(new_state.model_dump())),
        )
        await db.commit()
        return new_state

    async def read(self, session_id: str) -> Optional[BlackboardState]:
        db = await self.connect()
        async with db.execute(
            "SELECT state_json FROM blackboard WHERE session_id = ?", (session_id,)
        ) as cursor:
            row = await cursor.fetchone()
            if row:
                data = json.loads(row[0])
                return BlackboardState.model_validate(data)
        return None

    async def update(self, session_id: str, **updates: Any) -> BlackboardState:
        state = await self.read(session_id)
        if not state:
            raise ValueError(f"Session '{session_id}' not found in Blackboard.")

        state_dict = state.model_dump()
        for key, value in updates.items():
            if key in state_dict:
                state_dict[key] = value

        updated_state = BlackboardState.model_validate(state_dict)
        db = await self.connect()
        await db.execute(
            "UPDATE blackboard SET state_json = ?, updated_at = CURRENT_TIMESTAMP WHERE session_id = ?",
            (json.dumps(updated_state.model_dump()), session_id),
        )
        await db.commit()
        return updated_state

    async def lock_agent(
        self, session_id: str, agent_name: str, locked: bool = True
    ) -> bool:
        state = await self.read(session_id)
        if not state:
            return False

        locks = state.agent_locks.model_dump()
        if agent_name not in locks:
            raise ValueError(f"Unknown agent name '{agent_name}'")

        locks[agent_name] = locked
        await self.update(session_id, agent_locks=locks)
        return True

    async def close(self) -> None:
        if self._db:
            await self._db.close()
            self._db = None
