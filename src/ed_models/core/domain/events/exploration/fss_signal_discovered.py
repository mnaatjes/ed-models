"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass
from enum import StrEnum

from ed_models.core.domain.events.base import JournalEvent


class SignalType(StrEnum):
    OUTPOST = "Outpost"
    STATION_CORIOLIS = "StationCoriolis"
    FLEET_CARRIER = "FleetCarrier"
    STATION_O_NEIL_ORBIS = "StationONeilOrbis"
    NAV_BEACON = "NavBeacon"
    MEGASHIP = "Megaship"
    COMBAT = "Combat"
    INSTALLATION = "Installation"
    STATION_O_NEIL_CYLINDER = "StationONeilCylinder"
    GENERIC = "Generic"
    RESOURCE_EXTRACTION = "ResourceExtraction"
    STATION_BERNAL_SPHERE = "StationBernalSphere"
    TOURIST_BEACON = "TouristBeacon"
    TITAN = "Titan"
    STATION_MEGA_SHIP = "StationMegaShip"
    U_S_S = "USS"
    CODEX = "Codex"
    STATION_ASTEROID = "StationAsteroid"
    SQUADRON_CARRIER = "SquadronCarrier"
    STATION_DODEC = "StationDodec"


@dataclass(slots=True, kw_only=True)
class FSSSignalDiscovered(JournalEvent):
    """Written when zooming in on a signal using the FSS scanner."""

    SignalName: str | None = None
    SignalName_Localised: str | None = None
    SignalType: SignalType | None = None
    SpawningState: str | None = None
    SpawningState_Localised: str | None = None
    SpawningFaction: str | None = None
    SpawningFaction_Localised: str | None = None
    TimeRemaining: int | float | None = None
    SystemAddress: int | None = None
    ThreatLevel: int | None = None
    USSType: str | None = None
    USSType_Localised: str | None = None
    SpawningPower: str | None = None
    OpposingPower: str | None = None
    IsStation: bool | None = None
