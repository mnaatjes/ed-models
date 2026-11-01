"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class EngineerLegacyConvertModifiersItem:
    """Nested value object for EngineerLegacyConvert.ModifiersItem."""

    Label: str | None = None
    LessIsGood: int | float | None = None
    OriginalValue: int | float | None = None
    Value: int | float | None = None
    ValueStr: str | None = None
    ValueStr_Localised: str | None = None


@dataclass(slots=True, kw_only=True)
class EngineerLegacyConvert(JournalEvent):
    ApplyExperimentalEffect: str | None = None
    Blueprint: str | None = None
    BlueprintID: int | None = None
    BlueprintName: str | None = None
    Engineer: str | None = None
    EngineerID: int | None = None
    ExperimentalEffect: str | None = None
    ExperimentalEffect_Localised: str | None = None
    IsPreview: bool | None = None
    Level: int | None = None
    Modifiers: list[EngineerLegacyConvertModifiersItem] | None = None
    Module: str | None = None
    Quality: int | float | None = None
    Slot: str | None = None
