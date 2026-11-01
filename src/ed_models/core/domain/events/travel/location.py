"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from __future__ import annotations

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent
from ed_models.core.domain.spatial.coordinates import Coordinates3D
from ed_models.core.domain.types.body_type import BodyType
from ed_models.core.domain.types.conflict_faction import ConflictFaction
from ed_models.core.domain.types.conflict_progress import ConflictProgress
from ed_models.core.domain.types.power_state import PowerState
from ed_models.core.domain.types.station_service import StationService
from ed_models.core.domain.types.station_type import StationType


@dataclass(slots=True, kw_only=True)
class LocationSystemFaction:
    """Nested value object for Location.SystemFaction."""

    Name: str | None = None
    FactionState: str | None = None


@dataclass(slots=True, kw_only=True)
class LocationFactionsItemPendingStatesItem:
    """Nested value object for LocationFactionsItem.PendingStatesItem."""

    State: str | None = None
    Trend: int | float | None = None


@dataclass(slots=True, kw_only=True)
class LocationFactionsItemRecoveringStatesItem:
    """Nested value object for LocationFactionsItem.RecoveringStatesItem."""

    State: str | None = None
    Trend: int | float | None = None


@dataclass(slots=True, kw_only=True)
class LocationFactionsItemActiveStatesItem:
    """Nested value object for LocationFactionsItem.ActiveStatesItem."""

    State: str | None = None


@dataclass(slots=True, kw_only=True)
class LocationFactionsItem:
    """Nested value object for Location.FactionsItem."""

    Allegiance: str | None = None
    FactionState: str | None = None
    Government: str | None = None
    Influence: int | float | None = None
    Name: str | None = None
    PendingStates: list[LocationFactionsItemPendingStatesItem] | None = None
    RecoveringStates: list[LocationFactionsItemRecoveringStatesItem] | None = None
    ActiveStates: list[LocationFactionsItemActiveStatesItem] | None = None
    Happiness: str | None = None
    Happiness_Localised: str | None = None
    MyReputation: int | None = None
    SquadronFaction: bool | None = None


@dataclass(slots=True, kw_only=True)
class LocationConflictsItem:
    """Nested value object for Location.ConflictsItem."""

    WarType: str | None = None
    Status: str | None = None
    Faction1: ConflictFaction | None = None
    Faction2: ConflictFaction | None = None


@dataclass(slots=True, kw_only=True)
class LocationThargoidWar:
    """Nested value object for Location.ThargoidWar."""

    CurrentState: str | None = None
    NextStateSuccess: str | None = None
    NextStateFailure: str | None = None
    SuccessStateReached: bool | None = None
    WarProgress: int | None = None
    RemainingPorts: int | None = None


@dataclass(slots=True, kw_only=True)
class LocationStationFaction:
    """Nested value object for Location.StationFaction."""

    Name: str | None = None
    FactionState: str | None = None


@dataclass(slots=True, kw_only=True)
class LocationStationEconomiesItem:
    """Nested value object for Location.StationEconomiesItem."""

    Name: str | None = None
    Name_Localised: str | None = None
    Proportion: int | float | None = None


@dataclass(slots=True, kw_only=True)
class Location(JournalEvent):
    """Written at startup or when being resurrected at a station."""

    StarSystem: str | None = None
    SystemAddress: int | None = None
    StarPos: Coordinates3D | None = None
    Body: str | None = None
    Body_Localised: str | None = None
    BodyID: int | None = None
    BodyType: BodyType | None = None
    ControllingPower: str | None = None
    DistFromStarLS: float | None = None
    Docked: bool | None = None
    Latitude: int | float | None = None
    Longitude: int | float | None = None
    StationName: str | None = None
    StationType: StationType | None = None
    MarketID: int | None = None
    SystemFaction: LocationSystemFaction | None = None
    SystemAllegiance: str | None = None
    SystemEconomy: str | None = None
    SystemEconomy_Localised: str | None = None
    SystemSecondEconomy: str | None = None
    SystemSecondEconomy_Localised: str | None = None
    SystemGovernment: str | None = None
    SystemGovernment_Localised: str | None = None
    SystemSecurity: str | None = None
    SystemSecurity_Localised: str | None = None
    Population: int | None = None
    Wanted: bool | None = None
    Factions: list[LocationFactionsItem] | None = None
    Conflicts: list[LocationConflictsItem] | None = None
    Powers: list[str] | None = None
    PowerplayState: PowerState | None = None
    PowerplayStateControlProgress: int | None = None
    PowerplayStateReinforcement: int | float | None = None
    PowerplayStateUndermining: int | float | None = None
    PowerplayConflictProgress: list[ConflictProgress] | None = None
    ThargoidWar: LocationThargoidWar | None = None
    StationFaction: LocationStationFaction | None = None
    StationGovernment: str | None = None
    StationGovernment_Localised: str | None = None
    StationAllegiance: str | None = None
    StationServices: list[StationService] | None = None
    StationEconomies: list[LocationStationEconomiesItem] | None = None
    Taxi: bool | None = None
    Multicrew: bool | None = None
    InSRV: bool | None = None
    OnFoot: bool | None = None
    StationEconomy: str | None = None
    StationEconomy_Localised: str | None = None
