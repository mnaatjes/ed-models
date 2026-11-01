"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent
from ed_models.core.domain.types.micro_resource import MicroResource


@dataclass(slots=True, kw_only=True)
class SellMicroResources(JournalEvent):
    TotalCount: int | None = None
    MicroResources: list[MicroResource] | None = None
    Price: int | None = None
    MarketID: int | None = None
