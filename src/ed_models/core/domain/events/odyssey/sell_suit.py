"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class SellSuit(JournalEvent):
    Name: str | None = None
    Name_Localised: str | None = None
    Price: int | None = None
    SuitID: int | None = None
    SuitMods: list[str] | None = None
