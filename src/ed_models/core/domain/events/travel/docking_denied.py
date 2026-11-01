"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from __future__ import annotations

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent
from ed_models.core.domain.types.station_type import StationType


@dataclass(slots=True, kw_only=True)
class DockingDenied(JournalEvent):
    """Written when the station denies a docking request."""

    StationName: str | None = None
    StationType: StationType | None = None
    MarketID: int | None = None
    Reason: str | None = None
