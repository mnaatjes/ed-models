"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class CargoTransferTransfersItem:
    """Nested value object for CargoTransfer.TransfersItem."""

    Type: str | None = None
    Type_Localised: str | None = None
    Count: int | None = None
    Direction: str | None = None


@dataclass(slots=True, kw_only=True)
class CargoTransfer(JournalEvent):
    Transfers: list[CargoTransferTransfersItem] | None = None
