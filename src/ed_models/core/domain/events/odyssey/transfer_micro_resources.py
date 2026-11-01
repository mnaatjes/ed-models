"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class TransferMicroResourcesTransfersItem:
    """Nested value object for TransferMicroResources.TransfersItem."""

    Name: str | None = None
    Name_Localised: str | None = None
    Category: str | None = None
    LockerOldCount: int | None = None
    LockerNewCount: int | None = None
    Count: int | None = None
    Direction: str | None = None


@dataclass(slots=True, kw_only=True)
class TransferMicroResources(JournalEvent):
    Transfers: list[TransferMicroResourcesTransfersItem] | None = None
