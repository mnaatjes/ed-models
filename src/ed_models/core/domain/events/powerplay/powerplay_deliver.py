"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class PowerplayDeliver(JournalEvent):
    Count: int | None = None
    Power: str | None = None
    Type: str | None = None
    Type_Localised: str | None = None
