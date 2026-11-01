"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from __future__ import annotations

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent
from ed_models.core.domain.types.carrier_type import CarrierType


@dataclass(slots=True, kw_only=True)
class CarrierTradeOrder(JournalEvent):
    CarrierID: int | None = None
    CarrierType: CarrierType | None = None
    BlackMarket: bool | None = None
    Commodity: str | None = None
    Commodity_Localised: str | None = None
    CancelTrade: bool | None = None
    PurchaseOrder: int | float | None = None
    SaleOrder: int | float | None = None
    Price: int | None = None
