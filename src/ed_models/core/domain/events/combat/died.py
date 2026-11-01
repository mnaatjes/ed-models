"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class Died(JournalEvent):
    """Written when player was killed."""

    KillerName: str | None = None
    KillerName_Localised: str | None = None
    KillerShip: str | None = None
    KillerRank: str | None = None
