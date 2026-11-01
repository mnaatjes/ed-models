"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class ScientificResearch(JournalEvent):
    Category: str | None = None
    Count: int | None = None
    MarketID: int | None = None
    Name: str | None = None
    Name_Localised: str | None = None
