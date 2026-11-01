"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class ShipyardSwap(JournalEvent):
    """TODO Verify by swapping ship and selling the old one at the same time. *"""

    MarketID: int | None = None
    ShipID: int | None = None
    ShipType: str | None = None
    ShipType_Localised: str | None = None
    StoreOldShip: str | None = None
    StoreShipID: int | None = None
    SellOldShip: str | None = None
    SellShipID: int | None = None
