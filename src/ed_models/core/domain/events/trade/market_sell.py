"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class MarketSell(JournalEvent):
    AvgPricePaid: int | None = None
    BlackMarket: bool | None = None
    Count: int | None = None
    IllegalGoods: bool | None = None
    MarketID: int | None = None
    SellPrice: int | None = None
    StolenGoods: bool | None = None
    TotalSale: int | None = None
    Type: str | None = None
    Type_Localised: str | None = None
