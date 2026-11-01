"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class MissionCompletedCommodityRewardItem:
    """Nested value object for MissionCompleted.CommodityRewardItem."""

    Count: int | None = None
    Name: str | None = None
    Name_Localised: str | None = None


@dataclass(slots=True, kw_only=True)
class MissionCompletedFactionEffectsItemEffectsItem:
    """Nested value object for MissionCompletedFactionEffectsItem.EffectsItem."""

    Effect: str | None = None
    Effect_Localised: str | None = None
    Trend: str | None = None


@dataclass(slots=True, kw_only=True)
class MissionCompletedFactionEffectsItemInfluenceItem:
    """Nested value object for MissionCompletedFactionEffectsItem.InfluenceItem."""

    System: int | float | None = None
    SystemAddress: int | None = None
    Trend: str | None = None
    Influence: str | None = None


@dataclass(slots=True, kw_only=True)
class MissionCompletedFactionEffectsItem:
    """Nested value object for MissionCompleted.FactionEffectsItem."""

    Faction: str | None = None
    Effects: list[MissionCompletedFactionEffectsItemEffectsItem] | None = None
    Influence: list[MissionCompletedFactionEffectsItemInfluenceItem] | None = None
    ReputationTrend: str | None = None
    Reputation: str | None = None


@dataclass(slots=True, kw_only=True)
class MissionCompletedMaterialsRewardItem:
    """Nested value object for MissionCompleted.MaterialsRewardItem."""

    Name: str | None = None
    Name_Localised: str | None = None
    Category: str | None = None
    Category_Localised: str | None = None
    Count: int | None = None


@dataclass(slots=True, kw_only=True)
class MissionCompleted(JournalEvent):
    Commodity: str | None = None
    Commodity_Localised: str | None = None
    CommodityReward: list[MissionCompletedCommodityRewardItem] | None = None
    Count: int | None = None
    NewDestinationStation: str | None = None
    DestinationStation: str | None = None
    DestinationSettlement: str | None = None
    NewDestinationSystem: str | None = None
    DestinationSystem: str | None = None
    Donation: str | int | float | None = None
    Donated: int | float | None = None
    Faction: str | None = None
    KillCount: int | None = None
    FactionEffects: list[MissionCompletedFactionEffectsItem] | None = None
    MissionID: int | None = None
    Name: str | None = None
    LocalisedName: str | None = None
    PermitsAwarded: list[str] | None = None
    Reward: int | None = None
    MaterialsReward: list[MissionCompletedMaterialsRewardItem] | None = None
    Target: str | None = None
    Target_Localised: str | None = None
    TargetType: str | None = None
    TargetType_Localised: str | None = None
    TargetFaction: str | None = None
