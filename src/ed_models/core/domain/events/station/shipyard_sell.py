"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class ShipyardSell(JournalEvent):
    MarketID: int | None = None
    SellShipID: int | None = None
    ShipPrice: int | None = None
    ShipType: str | None = None
    ShipType_Localised: str | None = None
    System: str | None = None
    ShipMarketID: int | None = None
