"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class MassModuleStoreItemsItem:
    """Nested value object for MassModuleStore.ItemsItem."""

    EngineerModifications: str | None = None
    Hot: bool | None = None
    Level: int | None = None
    Name: str | None = None
    Name_Localised: str | None = None
    Quality: int | float | None = None
    Slot: str | None = None


@dataclass(slots=True, kw_only=True)
class MassModuleStore(JournalEvent):
    Items: list[MassModuleStoreItemsItem] | None = None
    MarketID: int | None = None
    Ship: str | None = None
    ShipID: int | None = None
