"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class BuyExplorationData(JournalEvent):
    """Written when buying system data via the galaxy map."""

    System: str | None = None
    Cost: int | None = None
