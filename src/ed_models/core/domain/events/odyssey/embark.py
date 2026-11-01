"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent
from ed_models.core.domain.types.station_type import StationType


@dataclass(slots=True, kw_only=True)
class EmbarkCrewItem:
    """Nested value object for Embark.CrewItem."""

    Name: str | None = None
    Role: str | None = None


@dataclass(slots=True, kw_only=True)
class Embark(JournalEvent):
    SRV: bool | None = None
    Taxi: bool | None = None
    Multicrew: bool | None = None
    ID: int | None = None
    Crew: list[EmbarkCrewItem] | None = None
    StarSystem: str | None = None
    SystemAddress: int | None = None
    Body: str | None = None
    BodyID: int | None = None
    OnStation: bool | None = None
    OnPlanet: bool | None = None
    StationName: str | None = None
    StationType: StationType | None = None
    MarketID: int | None = None
