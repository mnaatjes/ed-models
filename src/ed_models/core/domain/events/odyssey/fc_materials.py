"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class FCMaterials(JournalEvent):
    """Written when trading with a Fleet Carrier Bartender for materials, a file is written with the price list. Similar to the Shipyard and Cargo events, a brief entry is written in the journal."""

    MarketID: int | None = None
    CarrierName: str | None = None
    CarrierID: str | None = None


@dataclass(slots=True, kw_only=True)
class ExtendedFCMaterialsItemsItem:
    """Nested value object for ExtendedFCMaterials.ItemsItem."""

    id: int | None = None
    Name: str | None = None
    Name_Localised: str | None = None
    Price: int | None = None
    Stock: int | float | None = None
    Demand: int | float | None = None


@dataclass(slots=True, kw_only=True)
class ExtendedFCMaterials(FCMaterials):
    """Extended Fleet Carrier materials list written to separate 'FCMaterials.json' file."""

    Items: list[ExtendedFCMaterialsItemsItem] | None = None
