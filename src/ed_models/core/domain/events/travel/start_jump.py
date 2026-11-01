"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum

from ed_models.core.domain.events.base import JournalEvent
from ed_models.core.domain.types.star_type import StarType


class JumpType(StrEnum):
    """The type of jump. *"""

    HYPERSPACE = "Hyperspace"
    SUPERCRUISE = "Supercruise"


@dataclass(slots=True, kw_only=True)
class StartJump(JournalEvent):
    """Written at the start of a hyperspace or supercruise jump (start of countdown)"""

    JumpType: JumpType | None = None
    StarSystem: str | None = None
    SystemAddress: int | None = None
    StarClass: StarType | None = None
    Taxi: bool | None = None
