"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class ColonisationConstructionResource(JournalEvent):
    Name: str | None = None
    Name_Localised: str | None = None
    RequiredAmount: int | None = None
    ProvidedAmount: int | None = None
    Payment: int | float | None = None


@dataclass(slots=True, kw_only=True)
class ColonisationConstructionDepot(JournalEvent):
    MarketID: int | None = None
    ConstructionProgress: int | None = None
    ConstructionComplete: bool | None = None
    ConstructionFailed: bool | None = None
    ResourcesRequired: list[ColonisationConstructionResource] | None = None
