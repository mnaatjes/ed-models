"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class Screenshot(JournalEvent):
    """Written when a screenshot has been taken. The latitude, longitude, altitude and heading will be included if on a planet or in low-altitude flight."""

    Filename: str | None = None
    Width: int | None = None
    Height: int | float | None = None
    System: str | None = None
    Body: str | None = None
    Latitude: int | float | None = None
    Longitude: int | float | None = None
    Altitude: int | float | None = None
    Heading: int | float | None = None
