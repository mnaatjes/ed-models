"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class Touchdown(JournalEvent):
    """Written when landing on a planet surface."""

    Latitude: int | float | None = None
    Longitude: int | float | None = None
    StarSystem: str | None = None
    SystemAddress: int | None = None
    Body: str | None = None
    BodyID: int | None = None
    OnStation: bool | None = None
    OnPlanet: bool | None = None
    NearestDestination: str | None = None
    NearestDestination_Localised: str | None = None
    PlayerControlled: bool | None = None
    Taxi: bool | None = None
    Multicrew: bool | None = None
