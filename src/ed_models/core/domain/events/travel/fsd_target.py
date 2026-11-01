"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent
from ed_models.core.domain.types.star_type import StarType


@dataclass(slots=True, kw_only=True)
class FSDTarget(JournalEvent):
    """Written when selecting a star system to jump to. Note, when following a multi-jump route, this will typically appear for the next star, during a jump, ie after 'StartJump' but before the 'FSDJump'"""

    Name: str | None = None
    RemainingJumpsInRoute: int | float | None = None
    StarClass: StarType | None = None
    SystemAddress: int | None = None
