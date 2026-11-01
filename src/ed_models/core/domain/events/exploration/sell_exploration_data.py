"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class SellExplorationData(JournalEvent):
    """Written when selling exploration data in Cartographics."""

    Systems: list[str] | None = None
    Discovered: list[str] | None = None
    BaseValue: int | float | None = None
    Bonus: int | float | None = None
    TotalEarnings: int | None = None
