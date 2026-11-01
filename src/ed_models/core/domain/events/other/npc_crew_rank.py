"""Frontier Player Journal event model generated from kayahr/ed-journal."""

import typing
from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class NpcCrewRank(JournalEvent):
    NpcCrewId: int | None = None
    NpcCrewName: str | None = None
    RankCombat: typing.Any | None = None
