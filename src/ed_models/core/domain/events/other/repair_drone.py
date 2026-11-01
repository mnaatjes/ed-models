"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class RepairDrone(JournalEvent):
    HullRepaired: int | float | None = None
    CockpitRepaired: int | float | None = None
    CorrosionRepaired: int | float | None = None
