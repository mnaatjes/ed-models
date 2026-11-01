"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class CommunityGoalCurrentGoalsItemTopTier:
    """Nested value object for CommunityGoalCurrentGoalsItem.TopTier."""

    Name: str | None = None
    Bonus: str | None = None


@dataclass(slots=True, kw_only=True)
class CommunityGoalCurrentGoalsItem:
    """Nested value object for CommunityGoal.CurrentGoalsItem."""

    Bonus: int | float | None = None
    CGID: int | None = None
    CurrentTotal: int | None = None
    Expiry: str | None = None
    IsComplete: bool | None = None
    MarketName: str | None = None
    NumContributors: int | float | None = None
    PlayerContribution: int | float | None = None
    PlayerInTopRank: bool | None = None
    PlayerPercentileBand: int | float | None = None
    SystemName: str | None = None
    TierReached: str | None = None
    Title: str | None = None
    TopRankSize: int | None = None
    TopTier: CommunityGoalCurrentGoalsItemTopTier | None = None


@dataclass(slots=True, kw_only=True)
class CommunityGoal(JournalEvent):
    CurrentGoals: list[CommunityGoalCurrentGoalsItem] | None = None
