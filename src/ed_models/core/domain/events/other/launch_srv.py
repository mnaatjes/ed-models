"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class LaunchSRV(JournalEvent):
    Loadout: str | None = None
    PlayerControlled: bool | None = None
    ID: int | None = None
    SRVType: str | None = None
    SRVType_Localised: str | None = None
