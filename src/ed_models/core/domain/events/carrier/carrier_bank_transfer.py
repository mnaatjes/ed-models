"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from __future__ import annotations

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent
from ed_models.core.domain.types.carrier_type import CarrierType


@dataclass(slots=True, kw_only=True)
class CarrierBankTransfer(JournalEvent):
    CarrierID: int | None = None
    CarrierType: CarrierType | None = None
    Deposit: int | float | None = None
    Withdraw: int | float | None = None
    PlayerBalance: int | float | None = None
    CarrierBalance: int | float | None = None
