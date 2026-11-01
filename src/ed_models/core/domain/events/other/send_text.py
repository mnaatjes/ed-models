"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class SendText(JournalEvent):
    Message: str | None = None
    To: str | None = None
    To_Localised: str | None = None
    Sent: bool | None = None
