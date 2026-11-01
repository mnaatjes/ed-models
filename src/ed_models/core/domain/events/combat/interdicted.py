"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class Interdicted(JournalEvent):
    """Written when player was interdicted by player or NPC."""

    Submitted: bool | None = None
    Interdictor: str | None = None
    Interdictor_Localised: str | None = None
    IsPlayer: bool | None = None
    CombatRank: int | None = None
    Faction: str | None = None
    Power: str | None = None
