"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class Mission(JournalEvent):
    """Data about a single mission. *"""

    MissionID: int | None = None
    Name: str | None = None
    Name_Localised: str | None = None
    PassengerMission: bool | None = None
    Expires: int | float | None = None


@dataclass(slots=True, kw_only=True)
class Missions(JournalEvent):
    """The player's missions. Written at startup."""

    Active: list[Mission] | None = None
    Complete: list[Mission] | None = None
    Failed: list[Mission] | None = None
