"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from __future__ import annotations

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent
from ed_models.core.domain.types.carrier_type import CarrierType


@dataclass(slots=True, kw_only=True)
class CarrierFinance(JournalEvent):
    """Change to tax rate or reserve"""

    CarrierID: int | None = None
    CarrierType: CarrierType | None = None
    TaxRate: int | float | None = None
    CarrierBalance: int | float | None = None
    ReserveBalance: int | float | None = None
    AvailableBalance: int | float | None = None
    ReservePercent: int | float | None = None
    TaxRate_rearm: int | float | None = None
    TaxRate_refuel: float | None = None
    TaxRate_repair: int | float | None = None
    TaxRate_pioneersupplies: int | float | None = None
    TaxRate_shipyard: int | float | None = None
    TaxRate_outfitting: int | float | None = None
