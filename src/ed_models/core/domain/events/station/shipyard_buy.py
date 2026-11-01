"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class ShipyardBuy(JournalEvent):
    """Verify by buying a new ship and selling the current one the same time. *"""

    MarketID: int | None = None
    ShipPrice: int | None = None
    ShipType: str | None = None
    ShipType_Localised: str | None = None
    StoreOldShip: str | None = None
    StoreShipID: int | None = None
    SellOldShip: str | None = None
    SellShipID: int | None = None
    SellPrice: int | None = None
