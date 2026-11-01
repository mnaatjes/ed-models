"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class NewCommander(JournalEvent):
    """Written when creating a new commander."""

    Name: str | None = None
    FID: str | None = None
    Package: str | None = None
