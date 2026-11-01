"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class ReceiveText(JournalEvent):
    Channel: str | None = None
    From: str | None = None
    From_Localised: str | None = None
    Message: str | None = None
    Message_Localised: str | None = None
