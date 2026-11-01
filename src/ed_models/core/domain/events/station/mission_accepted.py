"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class MissionAccepted(JournalEvent):
    """Accept some kill missions to verify *"""

    Commodity: str | None = None
    Commodity_Localised: str | None = None
    Count: int | None = None
    DestinationStation: str | None = None
    DestinationSystem: str | None = None
    DestinationSettlement: str | None = None
    Expiry: str | None = None
    Faction: str | None = None
    Influence: str | None = None
    KillCount: int | None = None
    LocalisedName: str | None = None
    MissionID: int | None = None
    Name: str | None = None
    PassengerCount: int | None = None
    PassengerType: str | None = None
    PassengerVIPs: bool | None = None
    PassengerWanted: bool | None = None
    Reputation: str | None = None
    Reward: int | None = None
    Target: str | None = None
    Target_Localised: str | None = None
    TargetType: str | None = None
    TargetType_Localised: str | None = None
    TargetFaction: str | None = None
    Wing: bool | None = None
    Donation: str | None = None
