"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent
from ed_models.core.domain.types.station_type import StationType


@dataclass(slots=True, kw_only=True)
class Market(JournalEvent):
    MarketID: int | None = None
    StarSystem: str | None = None
    StationName: str | None = None
    StationType: StationType | None = None
    CarrierDockingAccess: str | None = None


@dataclass(slots=True, kw_only=True)
class ExtendedMarketItemsItem:
    """Nested value object for ExtendedMarket.ItemsItem."""

    id: int | None = None
    Name: str | None = None
    Name_Localised: str | None = None
    Category: str | None = None
    Category_Localised: str | None = None
    BuyPrice: int | None = None
    SellPrice: int | None = None
    MeanPrice: int | None = None
    StockBracket: int | float | None = None
    DemandBracket: int | float | None = None
    Stock: int | float | None = None
    Demand: int | float | None = None
    Consumer: bool | None = None
    Producer: bool | None = None
    Rare: bool | None = None


@dataclass(slots=True, kw_only=True)
class ExtendedMarket(Market):
    """Extended market data written to separate 'Market.json' file."""

    Items: list[ExtendedMarketItemsItem] | None = None
