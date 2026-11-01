"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class ModuleSwap(JournalEvent):
    FromItem: str | None = None
    FromItem_Localised: str | None = None
    FromSlot: str | None = None
    MarketID: int | None = None
    Ship: str | None = None
    ShipID: int | None = None
    ToItem: str | None = None
    ToItem_Localised: str | None = None
    ToSlot: str | None = None
