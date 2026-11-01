"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class StoredModulesItemsItem:
    """Nested value object for StoredModules.ItemsItem."""

    BuyPrice: int | None = None
    EngineerModifications: str | None = None
    Hot: bool | None = None
    InTransit: bool | None = None
    Level: int | None = None
    MarketID: int | None = None
    Name: str | None = None
    Name_Localised: str | None = None
    Quality: int | float | None = None
    StarSystem: str | None = None
    StorageSlot: int | float | None = None
    TransferCost: int | None = None
    TransferTime: int | float | None = None


@dataclass(slots=True, kw_only=True)
class StoredModules(JournalEvent):
    """TODO Revalidate? Some mismatches between Log and API doc *"""

    Items: list[StoredModulesItemsItem] | None = None
    MarketID: int | None = None
    StarSystem: str | None = None
    StationName: str | None = None
