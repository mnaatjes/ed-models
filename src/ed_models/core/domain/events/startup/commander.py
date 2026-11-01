"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class Commander(JournalEvent):
    """Written at start of the game loading process."""

    Name: str | None = None
    FID: str | None = None
