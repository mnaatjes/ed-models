"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class Interdiction(JournalEvent):
    """Written when player has (attempted to) interdict another player or NPC."""

    Success: bool | None = None
    Interdicted: str | None = None
    IsPlayer: bool | None = None
    CombatRank: int | None = None
    Faction: str | None = None
    Power: str | None = None
