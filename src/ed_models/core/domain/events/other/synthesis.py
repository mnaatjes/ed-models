"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class SynthesisMaterialsItem:
    """Nested value object for Synthesis.MaterialsItem."""

    Count: int | None = None
    Name: str | None = None
    Name_Localised: str | None = None
    Percent: int | float | None = None


@dataclass(slots=True, kw_only=True)
class Synthesis(JournalEvent):
    Materials: list[SynthesisMaterialsItem] | None = None
    Name: str | None = None
