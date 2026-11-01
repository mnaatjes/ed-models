"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class ShipTargeted(JournalEvent):
    """Written when the current player selects a new target. The amount of data written depends on the extent to which the target ship has been scanned"""

    TargetLocked: bool | None = None
    Ship: str | None = None
    Ship_Localised: str | None = None
    ScanStage: int | float | None = None
    PilotName: str | None = None
    PilotName_Localised: str | None = None
    PilotRank: str | None = None
    ShieldHealth: int | float | None = None
    HullHealth: int | float | None = None
    Faction: str | None = None
    LegalStatus: str | None = None
    Bounty: int | None = None
    Subsystem: str | None = None
    Subsystem_Localised: str | None = None
    SubsystemHealth: int | float | None = None
    Power: str | None = None
    SquadronID: str | None = None
