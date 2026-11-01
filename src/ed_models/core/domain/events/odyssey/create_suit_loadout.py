"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class CreateSuitLoadoutModulesItem:
    """Nested value object for CreateSuitLoadout.ModulesItem."""

    SlotName: str | None = None
    SuitModuleID: int | None = None
    ModuleName: str | None = None
    ModuleName_Localised: str | None = None
    Class: int | float | None = None
    WeaponMods: list[str] | None = None


@dataclass(slots=True, kw_only=True)
class CreateSuitLoadout(JournalEvent):
    SuitID: int | None = None
    SuitName: str | None = None
    SuitName_Localised: str | None = None
    SuitMods: list[str] | None = None
    LoadoutID: int | None = None
    LoadoutName: str | None = None
    Modules: list[CreateSuitLoadoutModulesItem] | None = None
