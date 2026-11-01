"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class EngineerContribution(JournalEvent):
    Commodity: str | None = None
    Commodity_Localised: str | None = None
    Engineer: str | None = None
    EngineerID: int | None = None
    Faction: str | None = None
    Material: str | None = None
    Material_Localised: str | None = None
    Quantity: int | float | None = None
    TotalQuantity: int | None = None
    Type: str | None = None
