"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class AsteroidCracked(JournalEvent):
    """Written when the player has broken up a 'Motherlode' asteroid for mining."""

    Body: str | None = None
