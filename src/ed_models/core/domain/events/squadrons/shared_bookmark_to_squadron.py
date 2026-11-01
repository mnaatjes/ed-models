"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class SharedBookmarkToSquadron(JournalEvent):
    SquadronID: int | None = None
    SquadronName: str | None = None
