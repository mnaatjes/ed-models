"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class ModuleBuy(JournalEvent):
    BuyItem: str | None = None
    BuyItem_Localised: str | None = None
    BuyPrice: int | None = None
    MarketID: int | None = None
    SellItem: str | None = None
    SellItem_Localised: str | None = None
    SellPrice: int | None = None
    Ship: str | None = None
    ShipID: int | None = None
    Slot: str | None = None
    StoredItem: str | None = None
    StoredItem_Localised: str | None = None
