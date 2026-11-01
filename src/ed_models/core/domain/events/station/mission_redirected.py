"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class MissionRedirected(JournalEvent):
    MissionID: int | None = None
    Name: str | None = None
    LocalisedName: str | None = None
    NewDestinationStation: str | None = None
    NewDestinationSystem: str | None = None
    OldDestinationStation: str | None = None
    OldDestinationSystem: str | None = None
