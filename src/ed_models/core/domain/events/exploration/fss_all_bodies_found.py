"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class FSSAllBodiesFound(JournalEvent):
    """Written after having identified all bodies in the system."""

    SystemName: str | None = None
    SystemAddress: int | None = None
    Count: int | None = None
