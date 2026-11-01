"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class LoadoutEquipModule(JournalEvent):
    LoadoutName: str | None = None
    SuitID: int | None = None
    SuitName: str | None = None
    SuitName_Localised: str | None = None
    LoadoutID: int | None = None
    SlotName: str | None = None
    ModuleName: str | None = None
    ModuleName_Localised: str | None = None
    Class: int | float | None = None
    WeaponMods: list[str] | None = None
    SuitModuleID: int | None = None
