"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class SellDrones(JournalEvent):
    Count: int | None = None
    SellPrice: int | None = None
    TotalSale: int | None = None
    Type: str | None = None
