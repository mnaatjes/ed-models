"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class LeaveBody(JournalEvent):
    """Written when flying away from a planet and distance increases above the 'Orbital Cruise' altitude."""

    StarSystem: str | None = None
    SystemAddress: int | None = None
    Body: str | None = None
    BodyID: int | None = None
