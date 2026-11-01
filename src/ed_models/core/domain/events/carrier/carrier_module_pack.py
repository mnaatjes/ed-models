"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent
from ed_models.core.domain.types.carrier_type import CarrierType

type CarrierModulePack = CarrierModulePackBuy | CarrierModulePackSell


@dataclass(slots=True, kw_only=True)
class CarrierModulePackBase(JournalEvent):
    CarrierID: int | None = None
    CarrierType: CarrierType | None = None
    PackTheme: str | None = None
    PackTier: int | None = None


@dataclass(slots=True, kw_only=True)
class CarrierModulePackBuy(CarrierModulePackBase):
    Operation: str | None = None
    Cost: int | None = None


@dataclass(slots=True, kw_only=True)
class CarrierModulePackSell(CarrierModulePackBase):
    Operation: str | None = None
    Refund: int | float | None = None
