"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class SupercruiseDestinationDrop(JournalEvent):
    """When dropping out of supercruise at a targeted destination."""

    Type: str | None = None
    Type_Localised: str | None = None
    Threat: int | float | None = None
    MarketID: int | None = None
