"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from __future__ import annotations

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent
from ed_models.core.domain.types.carrier_type import CarrierType

type CarrierShipPack = CarrierShipPackBuy | CarrierShipPackSell


@dataclass(slots=True, kw_only=True)
class CarrierShipPackBase(JournalEvent):
    CarrierID: int | None = None
    CarrierType: CarrierType | None = None
    PackTheme: str | None = None
    PackTier: int | None = None


@dataclass(slots=True, kw_only=True)
class CarrierShipPackBuy(CarrierShipPackBase):
    Operation: str | None = None
    Cost: int | None = None


@dataclass(slots=True, kw_only=True)
class CarrierShipPackSell(CarrierShipPackBase):
    Operation: str | None = None
    Refund: int | float | None = None
