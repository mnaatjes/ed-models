"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class MaterialTradePaid:
    """Nested value object for MaterialTrade.Paid."""

    Category: str | None = None
    Category_Localised: str | None = None
    Material: str | None = None
    Material_Localised: str | None = None
    Quantity: int | float | None = None


@dataclass(slots=True, kw_only=True)
class MaterialTradeReceived:
    """Nested value object for MaterialTrade.Received."""

    Category: str | None = None
    Category_Localised: str | None = None
    Material: str | None = None
    Material_Localised: str | None = None
    Quantity: int | float | None = None


@dataclass(slots=True, kw_only=True)
class MaterialTrade(JournalEvent):
    MarketID: int | None = None
    Paid: MaterialTradePaid | None = None
    Received: MaterialTradeReceived | None = None
    TraderType: str | None = None
