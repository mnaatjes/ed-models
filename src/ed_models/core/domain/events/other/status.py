"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum

from ed_models.core.domain.events.base import JournalEvent
from ed_models.core.domain.spatial.coordinates import Coordinates3D


class LegalState(StrEnum):
    """Valid legal states. *"""

    CLEAN = "Clean"
    ILLEGAL_CARGO = "IllegalCargo"
    SPEEDING = "Speeding"
    WANTED = "Wanted"
    HOSTILE = "Hostile"
    PASSENGER_WANTED = "PassengerWanted"
    WARRANT = "Warrant"


@dataclass(slots=True, kw_only=True)
class StatusFuel:
    """Nested value object for Status.Fuel."""

    FuelMain: float | None = None
    FuelReservoir: float | None = None


@dataclass(slots=True, kw_only=True)
class StatusDestination:
    """Nested value object for Status.Destination."""

    System: int | float | None = None
    Body: int | float | None = None
    Name: str | None = None


@dataclass(slots=True, kw_only=True)
class Status(JournalEvent):
    """Some information about the current state of the game written every few seconds to the file 'Status.json' in the journal directory. The latitude or longitude need to change by 0.02 degrees to trigger an update when flying, or by 0.0005 degrees when in the SRV."""

    Flags: int | float | None = None
    Flags2: int | float | None = None
    Pips: Coordinates3D | None = None
    FireGroup: int | float | None = None
    GuiFocus: int | None = None
    Fuel: StatusFuel | None = None
    Cargo: int | float | None = None
    LegalState: LegalState | None = None
    Latitude: int | float | None = None
    Altitude: int | float | None = None
    Longitude: int | float | None = None
    Heading: int | float | None = None
    PlanetRadius: float | None = None
    BodyName: str | None = None
    Balance: int | float | None = None
    Destination: StatusDestination | None = None
    Oxygen: int | float | None = None
    Health: int | float | None = None
    Temperature: float | None = None
    SelectedWeapon: str | None = None
    SelectedWeapon_Localised: str | None = None
    Gravity: int | float | None = None
