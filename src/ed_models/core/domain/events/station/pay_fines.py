"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class PayFines(JournalEvent):
    Amount: int | None = None
    AllFines: bool | None = None
    Faction: str | None = None
    Faction_Localised: str | None = None
    BrokerPercentage: int | float | None = None
    ShipID: int | None = None
