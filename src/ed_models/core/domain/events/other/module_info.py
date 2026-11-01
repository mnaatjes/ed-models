"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class ModuleInfo(JournalEvent):
    pass


@dataclass(slots=True, kw_only=True)
class ExtendedModuleInfoModulesItem:
    """Nested value object for ExtendedModuleInfo.ModulesItem."""

    Slot: str | None = None
    Item: str | None = None
    Power: int | float | None = None
    Priority: int | float | None = None


@dataclass(slots=True, kw_only=True)
class ExtendedModuleInfo(ModuleInfo):
    """Extended modules info written to separate 'ModulesInfo.json' file."""

    Modules: list[ExtendedModuleInfoModulesItem] | None = None
