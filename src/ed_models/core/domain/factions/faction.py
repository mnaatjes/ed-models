"""Minor faction and background simulation (BGS) domain entities.

Governed by ADR 0006 and SDD-007.
"""

from dataclasses import dataclass
from enum import StrEnum

from ed_models.core.domain.exceptions import DomainValidationError


class Allegiance(StrEnum):
    """Major galactic superpower or independent allegiance."""

    FEDERATION = "Federation"
    EMPIRE = "Empire"
    ALLIANCE = "Alliance"
    INDEPENDENT = "Independent"
    PILOTS_FEDERATION = "PilotsFederation"
    NONE = "None"


class Government(StrEnum):
    """Faction political government classification."""

    ANARCHY = "Anarchy"
    COMMUNISM = "Communism"
    CONFEDERACY = "Confederacy"
    COOPERATIVE = "Cooperative"
    CORPORATE = "Corporate"
    DEMOCRACY = "Democracy"
    DICTATORSHIP = "Dictatorship"
    FEUDAL = "Feudal"
    PATRONAGE = "Patronage"
    PRISON_COLONY = "PrisonColony"
    THEOCRACY = "Theocracy"
    ENGINEER = "Engineer"
    NONE = "None"


class FactionState(StrEnum):
    """Minor faction active, pending, or recovering BGS states."""

    NONE = "None"
    BOOM = "Boom"
    BUST = "Bust"
    CIVIL_LIBERTY = "CivilLiberty"
    CIVIL_UNREST = "CivilUnrest"
    CIVIL_WAR = "CivilWar"
    ELECTION = "Election"
    EXPANSION = "Expansion"
    FAMINE = "Famine"
    INVESTMENT = "Investment"
    LOCKDOWN = "Lockdown"
    OUTBREAK = "Outbreak"
    RETREAT = "Retreat"
    WAR = "War"
    DROUGHT = "Drought"
    INCURSION = "Incursion"
    PIRATE_ATTACK = "PirateAttack"
    BLIGHT = "Blight"
    COLD_WAR = "ColdWar"
    COLONISATION = "Colonisation"
    HISTORIC_EVENT = "HistoricEvent"
    INFRASTRUCTURE_FAILURE = "InfrastructureFailure"
    NATURAL_DISASTER = "NaturalDisaster"
    PUBLIC_HOLIDAY = "PublicHoliday"
    REVOLUTION = "Revolution"
    TECHNOLOGICAL_LEAP = "TechnologicalLeap"
    TERRORISM = "Terrorism"
    TRADE_WAR = "TradeWar"
    THARGOID_PROBING = "Thargoid_Probing"
    THARGOID_HARVEST = "Thargoid_Harvest"


@dataclass(slots=True, kw_only=True)
class MinorFactionPresence:
    """Stateful minor faction presence in a star system."""

    faction_name: str
    allegiance: Allegiance
    government: Government
    influence: float
    active_states: tuple[FactionState, ...] = ()
    pending_states: tuple[FactionState, ...] = ()
    recovering_states: tuple[FactionState, ...] = ()
    happiness: str | None = None
    squadron_faction: bool = False

    def __post_init__(self) -> None:
        """Validates faction presence invariants."""
        if not self.faction_name or not self.faction_name.strip():
            raise DomainValidationError("Faction name cannot be empty.")
        if not 0.0 <= self.influence <= 1.0:
            raise DomainValidationError(
                f"Faction influence must be between 0.0 and 1.0: {self.influence}"
            )
