"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from __future__ import annotations

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent
from ed_models.core.domain.types.body_type import BodyType


@dataclass(slots=True, kw_only=True)
class SupercruiseExit(JournalEvent):
    """Written when leaving supercruise for normal space."""

    StarSystem: str | None = None
    SystemAddress: int | None = None
    Body: str | None = None
    BodyID: int | None = None
    BodyType: BodyType | None = None
    Taxi: bool | None = None
    Multicrew: bool | None = None
