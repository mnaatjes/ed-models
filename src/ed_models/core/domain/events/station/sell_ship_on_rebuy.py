"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class SellShipOnRebuy(JournalEvent):
    """TODO Verify by getting destroyed and selling the ship. *"""

    ShipType: str | None = None
    System: str | None = None
    SellShipId: int | None = None
    ShipPrice: int | None = None
