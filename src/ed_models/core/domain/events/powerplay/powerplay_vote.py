"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class PowerplayVote(JournalEvent):
    Power: str | None = None
    System: str | None = None
    Votes: int | float | None = None
