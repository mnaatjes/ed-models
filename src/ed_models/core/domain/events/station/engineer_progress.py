"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass
from enum import StrEnum

from ed_models.core.domain.events.base import JournalEvent


class EngineerProgressState(StrEnum):
    """The possible progress states of an engineer. *"""

    KNOWN = "Known"
    INVITED = "Invited"
    UNLOCKED = "Unlocked"


type Engineer = LockedEngineer | UnlockedEngineer


@dataclass(slots=True, kw_only=True)
class EngineerBase(JournalEvent):
    """Base interface for an engineer extended by {@link LockedEngineer} and {@link UnlockedEngineer}"""

    Engineer: str | None = None
    EngineerID: int | None = None
    Progress: EngineerProgressState | None = None


@dataclass(slots=True, kw_only=True)
class LockedEngineer(EngineerBase):
    """A locked engineer (known or invited state) without rank and rang progress information."""

    Progress: EngineerProgressState | None = None


@dataclass(slots=True, kw_only=True)
class UnlockedEngineer(EngineerBase):
    """An unlocked engineer with rank and rank progress."""

    Progress: EngineerProgressState | None = None
    Rank: int | None = None
    RankProgress: int | None = None


@dataclass(slots=True, kw_only=True)
class EngineerProgress(JournalEvent):
    Engineers: list[Engineer] | None = None
