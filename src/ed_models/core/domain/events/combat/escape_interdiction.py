"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class EscapeInterdiction(JournalEvent):
    """Written when player has escaped interdiction."""

    Interdictor: str | None = None
    Interdictor_Localised: str | None = None
    IsPlayer: bool | None = None
