"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent
from ed_models.core.domain.types.station_type import StationType


@dataclass(slots=True, kw_only=True)
class Undocked(JournalEvent):
    """Written when liftoff from a landing pad in a station, outpost or settlement."""

    StationName: str | None = None
    MarketID: int | None = None
    StationType: StationType | None = None
    Taxi: bool | None = None
    Multicrew: bool | None = None
