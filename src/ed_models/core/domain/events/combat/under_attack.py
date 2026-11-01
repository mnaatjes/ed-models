"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class UnderAttack(JournalEvent):
    """Written when under fire (same time as the Under Attack voice message)."""

    Target: str | None = None
