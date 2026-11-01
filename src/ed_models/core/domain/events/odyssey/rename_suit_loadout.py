"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class RenameSuitLoadout(JournalEvent):
    SuitID: int | None = None
    SuitName: str | None = None
    SuitName_Localised: str | None = None
    LoadoutID: int | None = None
    LoadoutName: str | None = None
