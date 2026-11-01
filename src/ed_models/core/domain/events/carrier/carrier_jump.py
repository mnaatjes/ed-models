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
class CarrierJumpStationFaction:
    """Nested value object for CarrierJump.StationFaction."""

    Name: str | None = None


@dataclass(slots=True, kw_only=True)
class CarrierJumpStationEconomiesItem:
    """Nested value object for CarrierJump.StationEconomiesItem."""

    Name: str | None = None
    Name_Localised: str | None = None
    Proportion: int | float | None = None


@dataclass(slots=True, kw_only=True)
class CarrierJumpConflictsItem:
    """Nested value object for CarrierJump.ConflictsItem."""

    WarType: str | None = None
    Status: str | None = None
    Faction1: ConflictFaction | None = None
    Faction2: ConflictFaction | None = None


@dataclass(slots=True, kw_only=True)
class CarrierJumpFactionsItemPendingStatesItem:
    """Nested value object for CarrierJumpFactionsItem.PendingStatesItem."""

    State: str | None = None
    Trend: int | float | None = None


@dataclass(slots=True, kw_only=True)
class CarrierJumpFactionsItemRecoveringStatesItem:
    """Nested value object for CarrierJumpFactionsItem.RecoveringStatesItem."""

    State: str | None = None
    Trend: int | float | None = None


@dataclass(slots=True, kw_only=True)
class CarrierJumpFactionsItemActiveStatesItem:
    """Nested value object for CarrierJumpFactionsItem.ActiveStatesItem."""

    State: str | None = None


@dataclass(slots=True, kw_only=True)
class CarrierJumpFactionsItem:
    """Nested value object for CarrierJump.FactionsItem."""

    Name: str | None = None
    FactionState: str | None = None
    Government: str | None = None
    Influence: int | float | None = None
    Allegiance: str | None = None
    Happiness: str | None = None
    Happiness_Localised: str | None = None
    MyReputation: int | None = None
    PendingStates: list[CarrierJumpFactionsItemPendingStatesItem] | None = None
    RecoveringStates: list[CarrierJumpFactionsItemRecoveringStatesItem] | None = None
    ActiveStates: list[CarrierJumpFactionsItemActiveStatesItem] | None = None


@dataclass(slots=True, kw_only=True)
class CarrierJumpSystemFaction:
    """Nested value object for CarrierJump.SystemFaction."""

    Name: str | None = None
    FactionState: str | None = None


@dataclass(slots=True, kw_only=True)
class CarrierJump(JournalEvent):
    Docked: bool | None = None
    OnFoot: bool | None = None
    StationName: str | None = None
    StationType: StationType | None = None
    MarketID: int | None = None
    StationFaction: CarrierJumpStationFaction | None = None
    StationGovernment: str | None = None
    StationGovernment_Localised: str | None = None
    StationServices: list[StationService] | None = None
    StationEconomy: str | None = None
    StationEconomy_Localised: str | None = None
    StationEconomies: list[CarrierJumpStationEconomiesItem] | None = None
    Conflicts: list[CarrierJumpConflictsItem] | None = None
    Powers: list[str] | None = None
    PowerplayState: PowerState | None = None
    PowerplayStateControlProgress: int | None = None
    PowerplayStateReinforcement: int | float | None = None
    PowerplayStateUndermining: int | float | None = None
    PowerplayConflictProgress: list[ConflictProgress] | None = None
    Taxi: bool | None = None
    Multicrew: bool | None = None
    StarSystem: str | None = None
    SystemAddress: int | None = None
    StarPos: Coordinates3D | None = None
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
    Body: str | None = None
    BodyID: int | None = None
    BodyType: BodyType | None = None
    ControllingPower: str | None = None
    Factions: list[CarrierJumpFactionsItem] | None = None
    SystemFaction: CarrierJumpSystemFaction | None = None
