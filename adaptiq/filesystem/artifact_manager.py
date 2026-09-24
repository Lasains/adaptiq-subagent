"""ArtifactManager for async read/write of session artifacts."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Optional
import aiofiles


class ArtifactManager:
    """Manages reading and writing of session artifacts under ./session/{session_id}/."""

    def __init__(self, base_dir: str | Path = "./session"):
        self.base_dir = Path(base_dir)

    def get_session_dir(self, session_id: str) -> Path:
        session_path = self.base_dir / session_id
        session_path.mkdir(parents=True, exist_ok=True)
        return session_path

    def get_artifact_path(self, session_id: str, filename: str) -> Path:
        return self.get_session_dir(session_id) / filename

    async def write_artifact(
        self, session_id: str, filename: str, content: str
    ) -> Path:
        """Asynchronously write text content to a session artifact."""
        filepath = self.get_artifact_path(session_id, filename)
        async with aiofiles.open(filepath, "w", encoding="utf-8") as f:
            await f.write(content)
        return filepath

    async def read_artifact(self, session_id: str, filename: str) -> str:
        """Asynchronously read content from a session artifact."""
        filepath = self.get_artifact_path(session_id, filename)
        if not filepath.exists():
            raise FileNotFoundError(
                f"Artifact '{filename}' does not exist for session '{session_id}'."
            )
        async with aiofiles.open(filepath, "r", encoding="utf-8") as f:
            return await f.read()

    async def artifact_exists(self, session_id: str, filename: str) -> bool:
        """Check if an artifact exists."""
        filepath = self.get_artifact_path(session_id, filename)
        return filepath.exists()

    async def list_artifacts(self, session_id: str) -> list[str]:
        """List all artifact filenames for a session."""
        session_path = self.get_session_dir(session_id)
        return [f.name for f in session_path.iterdir() if f.is_file()]
