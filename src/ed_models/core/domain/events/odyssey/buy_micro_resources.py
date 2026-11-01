"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent
from ed_models.core.domain.types.micro_resource import MicroResource

type BuyMicroResources = OldBuyMicroResources | NewBuyMicroResources


@dataclass(slots=True, kw_only=True)
class OldBuyMicroResources(JournalEvent):
    Name: str | None = None
    Name_Localised: str | None = None
    Category: str | None = None
    Count: int | None = None
    Price: int | None = None
    MarketID: int | None = None


@dataclass(slots=True, kw_only=True)
class NewBuyMicroResources(JournalEvent):
    TotalCount: int | None = None
    MicroResources: list[MicroResource] | None = None
    Price: int | None = None
    MarketID: int | None = None
