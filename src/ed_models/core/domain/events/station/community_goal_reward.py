"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class CommunityGoalReward(JournalEvent):
    Name: str | None = None
    Reward: int | None = None
    System: str | None = None
    CGID: int | None = None
