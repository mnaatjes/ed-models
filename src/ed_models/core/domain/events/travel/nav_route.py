"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent
from ed_models.core.domain.spatial.coordinates import Coordinates3D


@dataclass(slots=True, kw_only=True)
class NavRoute(JournalEvent):
    """When plotting a multi-star route, the file “NavRoute.json” is written in the same directory as the journal, with a list of stars along that route."""

    pass


@dataclass(slots=True, kw_only=True)
class ExtendedNavRoute(JournalEvent):
    """Extended nav route data written to separate 'NavRoute.json' file."""

    Route: Coordinates3D | None = None
