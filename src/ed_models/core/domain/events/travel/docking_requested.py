"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from __future__ import annotations

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent
from ed_models.core.domain.types.station_type import StationType


@dataclass(slots=True, kw_only=True)
class DockingRequestedLandingPads:
    """Nested value object for DockingRequested.LandingPads."""

    Small: int | float | None = None
    Medium: int | float | None = None
    Large: int | float | None = None


@dataclass(slots=True, kw_only=True)
class DockingRequested(JournalEvent):
    """Written when the player requests a docking at a station."""

    StationName: str | None = None
    StationType: StationType | None = None
    MarketID: int | None = None
    LandingPads: DockingRequestedLandingPads | None = None
