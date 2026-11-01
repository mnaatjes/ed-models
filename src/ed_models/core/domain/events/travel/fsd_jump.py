"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent
from ed_models.core.domain.spatial.coordinates import Coordinates3D
from ed_models.core.domain.types.body_type import BodyType
from ed_models.core.domain.types.conflict_faction import ConflictFaction
from ed_models.core.domain.types.conflict_progress import ConflictProgress
from ed_models.core.domain.types.power_state import PowerState


@dataclass(slots=True, kw_only=True)
class FSDJumpSystemFaction:
    """Nested value object for FSDJump.SystemFaction."""

    Name: str | None = None
    FactionState: str | None = None


@dataclass(slots=True, kw_only=True)
class FSDJumpFactionsItemPendingStatesItem:
    """Nested value object for FSDJumpFactionsItem.PendingStatesItem."""

    State: str | None = None
    Trend: int | float | None = None


@dataclass(slots=True, kw_only=True)
class FSDJumpFactionsItemRecoveringStatesItem:
    """Nested value object for FSDJumpFactionsItem.RecoveringStatesItem."""

    State: str | None = None
    Trend: int | float | None = None


@dataclass(slots=True, kw_only=True)
class FSDJumpFactionsItemActiveStatesItem:
    """Nested value object for FSDJumpFactionsItem.ActiveStatesItem."""

    State: str | None = None


@dataclass(slots=True, kw_only=True)
class FSDJumpFactionsItem:
    """Nested value object for FSDJump.FactionsItem."""

    Name: str | None = None
    FactionState: str | None = None
    Government: str | None = None
    Influence: int | float | None = None
    Allegiance: str | None = None
    Happiness: str | None = None
    Happiness_Localised: str | None = None
    MyReputation: int | None = None
    PendingStates: list[FSDJumpFactionsItemPendingStatesItem] | None = None
    RecoveringStates: list[FSDJumpFactionsItemRecoveringStatesItem] | None = None
    ActiveStates: list[FSDJumpFactionsItemActiveStatesItem] | None = None
    SquadronFaction: bool | None = None


@dataclass(slots=True, kw_only=True)
class FSDJumpConflictsItem:
    """Nested value object for FSDJump.ConflictsItem."""

    WarType: str | None = None
    Status: str | None = None
    Faction1: ConflictFaction | None = None
    Faction2: ConflictFaction | None = None


@dataclass(slots=True, kw_only=True)
class FSDJumpThargoidWar:
    """Nested value object for FSDJump.ThargoidWar."""

    CurrentState: str | None = None
    NextStateSuccess: str | None = None
    NextStateFailure: str | None = None
    SuccessStateReached: bool | None = None
    WarProgress: int | None = None
    RemainingPorts: int | None = None


@dataclass(slots=True, kw_only=True)
class FSDJump(JournalEvent):
    """Written when jumping from one star to another."""

    StarSystem: str | None = None
    SystemAddress: int | None = None
    StarPos: Coordinates3D | None = None
    Body: str | None = None
    BodyID: int | None = None
    BodyType: BodyType | None = None
    ControllingPower: str | None = None
    JumpDist: float | None = None
    FuelUsed: float | None = None
    FuelLevel: int | None = None
    BoostUsed: int | None = None
    SystemFaction: FSDJumpSystemFaction | None = None
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
    Factions: list[FSDJumpFactionsItem] | None = None
    Conflicts: list[FSDJumpConflictsItem] | None = None
    ThargoidWar: FSDJumpThargoidWar | None = None
    Powers: list[str] | None = None
    PowerplayState: PowerState | None = None
    PowerplayStateControlProgress: int | None = None
    PowerplayStateReinforcement: int | float | None = None
    PowerplayStateUndermining: int | float | None = None
    PowerplayConflictProgress: list[ConflictProgress] | None = None
    Taxi: bool | None = None
    Multicrew: bool | None = None
