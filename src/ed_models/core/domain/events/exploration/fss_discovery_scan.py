"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class FSSDiscoveryScan(JournalEvent):
    """Written when performing a full system scan ('Honk')"""

    Progress: int | None = None
    BodyCount: int | None = None
    NonBodyCount: int | None = None
    SystemName: str | None = None
    SystemAddress: int | None = None
