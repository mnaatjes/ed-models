"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class PVPKill(JournalEvent):
    """Written when this player has killed another player."""

    Victim: str | None = None
    CombatRank: int | None = None
