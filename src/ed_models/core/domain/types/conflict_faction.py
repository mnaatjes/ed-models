"""Domain value object generated from kayahr/ed-journal."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True, kw_only=True)
class ConflictFaction:
    """A faction in a conflict. *"""

    Name: str | None = None
    Stake: str | None = None
    WonDays: int | None = None
