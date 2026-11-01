"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class ShipyardNew(JournalEvent):
    NewShipID: int | None = None
    ShipType: str | None = None
    ShipType_Localised: str | None = None
