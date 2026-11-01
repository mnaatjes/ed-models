"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class ShipyardRedeem(JournalEvent):
    ShipType: str | None = None
    ShipType_Localised: str | None = None
    BundleID: int | None = None
    MarketID: int | None = None
