"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from __future__ import annotations

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent
from ed_models.core.domain.types.carrier_type import CarrierType


@dataclass(slots=True, kw_only=True)
class CarrierJumpRequest(JournalEvent):
    CarrierID: int | None = None
    CarrierType: CarrierType | None = None
    SystemName: str | None = None
    Body: str | None = None
    SystemAddress: int | None = None
    BodyID: int | None = None
    DepartureTime: str | None = None
