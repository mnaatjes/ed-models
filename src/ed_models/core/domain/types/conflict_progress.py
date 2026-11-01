"""Domain value object generated from kayahr/ed-journal."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True, kw_only=True)
class ConflictProgress:
    Power: str | None = None
    ConflictProgress: int | None = None
