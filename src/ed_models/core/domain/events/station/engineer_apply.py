"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class EngineerApply(JournalEvent):
    """This event is obsolete and no longer written since ED v3.0."""

    Blueprint: str | None = None
    Engineer: str | None = None
    Level: int | None = None
    Override: str | None = None
