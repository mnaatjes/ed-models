"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class BookDropship(JournalEvent):
    Retreat: bool | None = None
    Cost: int | None = None
    DestinationSystem: str | None = None
    DestinationLocation: str | None = None
