"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class DockSRV(JournalEvent):
    ID: int | None = None
    SRVType: str | None = None
    SRVType_Localised: str | None = None
