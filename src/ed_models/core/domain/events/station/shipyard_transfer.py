"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class ShipyardTransfer(JournalEvent):
    Distance: float | None = None
    MarketID: int | None = None
    ShipID: int | None = None
    ShipMarketID: int | None = None
    ShipType: str | None = None
    ShipType_Localised: str | None = None
    System: str | None = None
    TransferPrice: int | None = None
    TransferTime: int | float | None = None
