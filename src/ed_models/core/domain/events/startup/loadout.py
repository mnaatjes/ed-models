"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class LoadoutFuelCapacity:
    """Nested value object for Loadout.FuelCapacity."""

    Main: int | float | None = None
    Reserve: int | float | None = None


@dataclass(slots=True, kw_only=True)
class LoadoutModulesItemEngineeringModifiersItem:
    """Nested value object for LoadoutModulesItemEngineering.ModifiersItem."""

    Label: str | None = None
    LessIsGood: int | float | None = None
    OriginalValue: int | float | None = None
    Value: str | int | float | None = None
    Value_Localised: str | None = None
    ValueStr: str | None = None
    ValueStr_Localised: str | None = None


@dataclass(slots=True, kw_only=True)
class LoadoutModulesItemEngineering:
    """Nested value object for LoadoutModulesItem.Engineering."""

    BlueprintID: int | None = None
    BlueprintName: str | None = None
    Engineer: str | None = None
    EngineerID: int | None = None
    ExperimentalEffect: str | None = None
    ExperimentalEffect_Localised: str | None = None
    Level: int | None = None
    Modifiers: list[LoadoutModulesItemEngineeringModifiersItem] | None = None
    Quality: int | float | None = None


@dataclass(slots=True, kw_only=True)
class LoadoutModulesItem:
    """Nested value object for Loadout.ModulesItem."""

    Slot: str | None = None
    Item: str | None = None
    On: bool | None = None
    Priority: int | float | None = None
    Health: int | float | None = None
    Value: int | float | None = None
    AmmoInClip: int | float | None = None
    AmmoInHopper: int | float | None = None
    Engineering: LoadoutModulesItemEngineering | None = None
    EngineerBlueprint: str | None = None
    EngineerLevel: int | None = None


@dataclass(slots=True, kw_only=True)
class Loadout(JournalEvent):
    """Written at startup when loading from main menu, when switching ships, after changing the ship in outfitting or when docking SRV back in mothership."""

    Ship: str | None = None
    ShipID: int | None = None
    ShipName: str | None = None
    ShipIdent: str | None = None
    HullValue: int | float | None = None
    ModulesValue: int | float | None = None
    HullHealth: int | float | None = None
    UnladenMass: float | None = None
    FuelCapacity: LoadoutFuelCapacity | None = None
    CargoCapacity: int | None = None
    MaxJumpRange: int | float | None = None
    Rebuy: int | float | None = None
    Hot: bool | None = None
    Modules: list[LoadoutModulesItem] | None = None
