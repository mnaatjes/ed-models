"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class SquadronStartup(JournalEvent):
    SquadronName: str | None = None
    SquadronID: int | None = None
    CurrentRank: int | None = None
    CurrentRankName: str | None = None
    CurrentRankName_Localised: str | None = None
