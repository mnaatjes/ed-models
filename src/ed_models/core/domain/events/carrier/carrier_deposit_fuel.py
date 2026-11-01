"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class CarrierDepositFuel(JournalEvent):
    CarrierID: int | None = None
    Amount: int | None = None
    Total: int | None = None
