"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class ModuleSellRemote(JournalEvent):
    SellItem: str | None = None
    SellItem_Localised: str | None = None
    SellPrice: int | None = None
    ServerId: int | None = None
    Ship: str | None = None
    ShipID: int | None = None
    StorageSlot: int | float | None = None
