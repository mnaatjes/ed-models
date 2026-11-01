"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class BountyRewardsItem:
    """Nested value object for Bounty.RewardsItem."""

    Faction: str | None = None
    Reward: int | None = None


@dataclass(slots=True, kw_only=True)
class Bounty(JournalEvent):
    """Written when player is awarded a bounty for a kill."""

    Rewards: list[BountyRewardsItem] | None = None
    Target: str | None = None
    Target_Localised: str | None = None
    VictimFaction: str | None = None
    VictimFaction_Localised: str | None = None
    TotalReward: int | None = None
    SharedWithOthers: int | float | None = None
    Faction: str | None = None
    Faction_Localised: str | None = None
    Reward: int | None = None
    PilotName: str | None = None
    PilotName_Localised: str | None = None
