"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class ScanOrganic(JournalEvent):
    ScanType: str | None = None
    Genus: str | None = None
    Genus_Localised: str | None = None
    Species: str | None = None
    Species_Localised: str | None = None
    Variant: str | None = None
    Variant_Localised: str | None = None
    WasLogged: bool | None = None
    SystemAddress: int | None = None
    Body: int | float | None = None
