"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class EngineerCraftIngredientsItem:
    """Nested value object for EngineerCraft.IngredientsItem."""

    Count: int | None = None
    Name: str | None = None
    Name_Localised: str | None = None


@dataclass(slots=True, kw_only=True)
class EngineerCraftModifiersItem:
    """Nested value object for EngineerCraft.ModifiersItem."""

    Label: str | None = None
    LessIsGood: int | float | None = None
    OriginalValue: int | float | None = None
    Value: int | float | None = None
    ValueStr: str | None = None
    ValueStr_Localised: str | None = None


@dataclass(slots=True, kw_only=True)
class EngineerCraft(JournalEvent):
    ApplyExperimentalEffect: str | None = None
    Blueprint: str | None = None
    BlueprintID: int | None = None
    BlueprintName: str | None = None
    Engineer: str | None = None
    EngineerID: int | None = None
    ExperimentalEffect: str | None = None
    ExperimentalEffect_Localised: str | None = None
    Ingredients: list[EngineerCraftIngredientsItem] | None = None
    Level: int | None = None
    Modifiers: list[EngineerCraftModifiersItem] | None = None
    Module: str | None = None
    Quality: int | float | None = None
    Slot: str | None = None
