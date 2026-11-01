"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class FetchRemoteModule(JournalEvent):
    ServerId: int | None = None
    Ship: str | None = None
    ShipID: int | None = None
    StorageSlot: int | float | None = None
    StoredItem: str | None = None
    StoredItem_Localised: str | None = None
    TransferCost: int | None = None
    TransferTime: int | float | None = None
