"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class DropItems(JournalEvent):
    Name: str | None = None
    Name_Localised: str | None = None
    Type: str | None = None
    OwnerID: int | None = None
    Count: int | None = None
