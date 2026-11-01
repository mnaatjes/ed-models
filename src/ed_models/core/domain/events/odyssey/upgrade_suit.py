"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class UpgradeSuitResourcesItem:
    """Nested value object for UpgradeSuit.ResourcesItem."""

    Name: str | None = None
    Name_Localised: str | None = None
    Count: int | None = None


@dataclass(slots=True, kw_only=True)
class UpgradeSuit(JournalEvent):
    Name: str | None = None
    Name_Localised: str | None = None
    SuitID: int | None = None
    Class: int | float | None = None
    Cost: int | None = None
    Resources: list[UpgradeSuitResourcesItem] | None = None
