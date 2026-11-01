"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class Powerplay(JournalEvent):
    """Written at startup if player has pledged to a power."""

    Power: str | None = None
    Rank: int | None = None
    Merits: int | float | None = None
    Votes: int | float | None = None
    TimePledged: int | float | None = None
