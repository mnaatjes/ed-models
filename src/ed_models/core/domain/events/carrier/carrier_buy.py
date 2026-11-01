"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent
from ed_models.core.domain.types.carrier_type import CarrierType


@dataclass(slots=True, kw_only=True)
class CarrierBuy(JournalEvent):
    CarrierID: int | None = None
    CarrierType: CarrierType | None = None
    BoughtAtMarket: int | float | None = None
    Location: str | None = None
    SystemAddress: int | None = None
    Price: int | None = None
    Variant: str | None = None
    Callsign: str | None = None
