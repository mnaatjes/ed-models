"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class SetUserShipName(JournalEvent):
    Ship: str | None = None
    ShipID: int | None = None
    UserShipId: str | None = None
    UserShipName: str | None = None
