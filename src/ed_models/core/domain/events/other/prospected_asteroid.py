"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class ProspectedAsteroidMaterialsItem:
    """Nested value object for ProspectedAsteroid.MaterialsItem."""

    Name: str | None = None
    Name_Localised: str | None = None
    Proportion: int | float | None = None


@dataclass(slots=True, kw_only=True)
class ProspectedAsteroid(JournalEvent):
    Materials: list[ProspectedAsteroidMaterialsItem] | None = None
    MotherlodeMaterial: str | None = None
    MotherlodeMaterial_Localised: str | None = None
    Content: str | None = None
    Content_Localised: str | None = None
    Remaining: int | float | None = None
