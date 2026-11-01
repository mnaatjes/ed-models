"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class CrewHire(JournalEvent):
    CrewID: int | None = None
    CombatRank: int | None = None
    Cost: int | None = None
    Faction: str | None = None
    Name: str | None = None
