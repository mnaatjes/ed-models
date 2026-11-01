"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class HullDamage(JournalEvent):
    """Written when hull health drops below a threshold (20% steps)."""

    Health: int | float | None = None
    PlayerPilot: bool | None = None
    Fighter: bool | None = None
