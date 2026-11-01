"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class DiscoveryScan(JournalEvent):
    """Written when using the discovery scanner, and new body discoveries are displayed in the cockpit info window. Note you can get two or three of these in a row, where some bodies are discovered by the automatic passive scan, before the active scan is complete."""

    SystemAddress: int | None = None
    Bodies: int | float | None = None
