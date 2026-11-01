"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class Promotion(JournalEvent):
    Combat: int | float | None = None
    CQC: int | float | None = None
    Empire: int | float | None = None
    Explore: int | float | None = None
    Federation: int | float | None = None
    Trade: int | float | None = None
    Soldier: int | float | None = None
    Exobiologist: int | float | None = None
