"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class SAAScanComplete(JournalEvent):
    """Written after using the Surface Area Analysis scanner."""

    SystemAddress: int | None = None
    BodyName: str | None = None
    BodyID: int | None = None
    ProbesUsed: int | float | None = None
    EfficiencyTarget: int | float | None = None
