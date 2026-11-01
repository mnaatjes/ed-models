"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class Outfitting(JournalEvent):
    """Written when accessing the outfitting menu."""

    MarketID: int | None = None
    StarSystem: str | None = None
    StationName: str | None = None


@dataclass(slots=True, kw_only=True)
class ExtendedOutfittingItemsItem:
    """Nested value object for ExtendedOutfitting.ItemsItem."""

    id: int | None = None
    Name: str | None = None
    BuyPrice: int | None = None


@dataclass(slots=True, kw_only=True)
class ExtendedOutfitting(Outfitting):
    """Extended outfitting info written to separate 'Outfitting.json' file."""

    Horizons: bool | None = None
    Items: list[ExtendedOutfittingItemsItem] | None = None
