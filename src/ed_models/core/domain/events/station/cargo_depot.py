"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class CargoDepot(JournalEvent):
    MissionID: int | None = None
    UpdateType: str | None = None
    CargoType: str | None = None
    CargoType_Localised: str | None = None
    Count: int | None = None
    StartMarketID: int | None = None
    EndMarketID: int | None = None
    ItemsCollected: int | float | None = None
    ItemsDelivered: int | float | None = None
    TotalItemsToDeliver: int | None = None
    Progress: int | None = None
