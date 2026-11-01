"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class TechnologyBrokerCommoditiesItem:
    """Nested value object for TechnologyBroker.CommoditiesItem."""

    Count: int | None = None
    Name: str | None = None
    Name_Localised: str | None = None


@dataclass(slots=True, kw_only=True)
class TechnologyBrokerItemsUnlockedItem:
    """Nested value object for TechnologyBroker.ItemsUnlockedItem."""

    Name: str | None = None
    Name_Localised: str | None = None


@dataclass(slots=True, kw_only=True)
class TechnologyBrokerMaterialsItem:
    """Nested value object for TechnologyBroker.MaterialsItem."""

    Category: str | None = None
    Count: int | None = None
    Name: str | None = None
    Name_Localised: str | None = None


@dataclass(slots=True, kw_only=True)
class TechnologyBroker(JournalEvent):
    BrokerType: str | None = None
    Commodities: list[TechnologyBrokerCommoditiesItem] | None = None
    ItemsUnlocked: list[TechnologyBrokerItemsUnlockedItem] | None = None
    MarketID: int | None = None
    Materials: list[TechnologyBrokerMaterialsItem] | None = None
