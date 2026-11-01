"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class SupercruiseEntry(JournalEvent):
    """Written when entering supercruise from normal space."""

    StarSystem: str | None = None
    SystemAddress: int | None = None
    Taxi: bool | None = None
    Multicrew: bool | None = None
