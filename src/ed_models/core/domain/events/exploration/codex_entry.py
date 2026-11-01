"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class CodexEntry(JournalEvent):
    """Written when a new discovery is added to the Codex."""

    EntryID: int | None = None
    Name: str | None = None
    Name_Localised: str | None = None
    SubCategory: str | None = None
    SubCategory_Localised: str | None = None
    Category: str | None = None
    Category_Localised: str | None = None
    Region: str | None = None
    Region_Localised: str | None = None
    System: str | None = None
    SystemAddress: int | None = None
    BodyID: int | None = None
    NearestDestination: str | None = None
    NearestDestination_Localised: str | None = None
    Latitude: int | float | None = None
    Longitude: int | float | None = None
    IsNewEntry: bool | None = None
    VoucherAmount: int | None = None
    Traits: list[str] | None = None
    NewTraitsDiscovered: bool | None = None
