"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class NavRouteClear(JournalEvent):
    """When the current plotted nav route is cleared."""

    pass
