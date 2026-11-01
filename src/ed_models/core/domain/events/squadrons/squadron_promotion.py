"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class SquadronPromotion(JournalEvent):
    SquadronID: int | None = None
    SquadronName: str | None = None
    OldRank: int | None = None
    OldRankName: str | None = None
    NewRank: int | None = None
    NewRankName: str | None = None
