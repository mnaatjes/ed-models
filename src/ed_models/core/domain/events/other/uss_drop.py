"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class USSDrop(JournalEvent):
    USSThreat: int | float | None = None
    USSType: str | None = None
    USSType_Localised: str | None = None
