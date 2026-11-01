"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent
from ed_models.core.domain.types.station_type import StationType


@dataclass(slots=True, kw_only=True)
class DockingTimeout(JournalEvent):
    """Written when a docking request has timed out."""

    StationName: str | None = None
    StationType: StationType | None = None
    MarketID: int | None = None
