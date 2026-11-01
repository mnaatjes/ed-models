"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent
from ed_models.core.domain.types.micro_resource import MicroResource


@dataclass(slots=True, kw_only=True)
class TradeMicroResources(JournalEvent):
    Offered: list[MicroResource] | None = None
    TotalCount: int | None = None
    Received: str | None = None
    Received_Localised: str | None = None
    Count: int | None = None
    Category: str | None = None
    MarketID: int | None = None
