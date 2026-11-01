"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class MultiSellExplorationDataDiscoveredItem:
    """Nested value object for MultiSellExplorationData.DiscoveredItem."""

    SystemName: str | None = None
    SystemName_Localised: str | None = None
    NumBodies: int | float | None = None


@dataclass(slots=True, kw_only=True)
class MultiSellExplorationData(JournalEvent):
    """Written when selling exploration data in Cartographics, a page at a time."""

    Discovered: list[MultiSellExplorationDataDiscoveredItem] | None = None
    BaseValue: int | float | None = None
    Bonus: int | float | None = None
    TotalEarnings: int | None = None
