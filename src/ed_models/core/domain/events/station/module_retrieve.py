"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class ModuleRetrieve(JournalEvent):
    Cost: int | None = None
    EngineerModifications: str | None = None
    Hot: bool | None = None
    Level: int | None = None
    MarketID: int | None = None
    Quality: int | float | None = None
    RetrievedItem: str | None = None
    RetrievedItem_Localised: str | None = None
    Ship: str | None = None
    ShipID: int | None = None
    Slot: str | None = None
    SwapOutItem: str | None = None
    SwapOutItem_Localised: str | None = None
