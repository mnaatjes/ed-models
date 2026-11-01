"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class ModuleBuyAndStore(JournalEvent):
    BuyItem: str | None = None
    BuyItem_Localised: str | None = None
    BuyPrice: int | None = None
    MarketID: int | None = None
    Ship: str | None = None
    ShipID: int | None = None
