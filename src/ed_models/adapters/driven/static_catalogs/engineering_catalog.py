"""Pre-compiled static engineering catalog adapter."""

from __future__ import annotations

from ed_models.core.domain.engineering.blueprint import (
    AttributeModifier,
    BlueprintGrade,
    EngineeringBlueprint,
    ExperimentalEffect,
    RecipeIngredient,
)
from ed_models.core.domain.engineering.engineer import EngineerEntity
from ed_models.core.domain.spatial.coordinates import Coordinates3D
from ed_models.core.ports.driven.engineering_catalog_port import EngineeringCatalogProviderPort

_BLUEPRINTS: dict[str, EngineeringBlueprint] = {
    "fsd_longrange": EngineeringBlueprint(
        symbol="FSD_LongRange",
        name="Increased Range",
        target_modules=("Frame Shift Drive",),
        grades={
            1: BlueprintGrade(
                grade=1,
                ingredients=(
                    RecipeIngredient(
                        material_symbol="phosphorus",
                        name="Phosphorus",
                        count=1,
                    ),
                ),
                modifiers=(
                    AttributeModifier(
                        attribute_name="FSDOptimalMass",
                        is_positive=True,
                        multiplier=1.15,
                    ),
                    AttributeModifier(
                        attribute_name="Integrity",
                        is_positive=False,
                        multiplier=0.95,
                    ),
                    AttributeModifier(
                        attribute_name="Mass",
                        is_positive=False,
                        multiplier=1.10,
                    ),
                ),
            ),
            5: BlueprintGrade(
                grade=5,
                ingredients=(
                    RecipeIngredient(
                        material_symbol="dataminedwakeexceptions",
                        name="Datamined Wake Exceptions",
                        count=1,
                    ),
                    RecipeIngredient(
                        material_symbol="chemicalmanipulators",
                        name="Chemical Manipulators",
                        count=1,
                    ),
                    RecipeIngredient(
                        material_symbol="arsenic",
                        name="Arsenic",
                        count=1,
                    ),
                ),
                modifiers=(
                    AttributeModifier(
                        attribute_name="FSDOptimalMass",
                        is_positive=True,
                        multiplier=1.55,
                    ),
                    AttributeModifier(
                        attribute_name="Integrity",
                        is_positive=False,
                        multiplier=0.80,
                    ),
                    AttributeModifier(
                        attribute_name="Mass",
                        is_positive=False,
                        multiplier=1.30,
                    ),
                ),
            ),
        },
    ),
    "thrusters_dirty": EngineeringBlueprint(
        symbol="Thrusters_Dirty",
        name="Dirty Drives",
        target_modules=("Thrusters",),
        grades={
            1: BlueprintGrade(
                grade=1,
                ingredients=(
                    RecipeIngredient(
                        material_symbol="specialisedlegacyfirmware",
                        name="Specialised Legacy Firmware",
                        count=1,
                    ),
                ),
                modifiers=(
                    AttributeModifier(
                        attribute_name="EngineOptimalMultiplier",
                        is_positive=True,
                        multiplier=1.15,
                    ),
                    AttributeModifier(
                        attribute_name="ThermalLoad",
                        is_positive=False,
                        multiplier=1.20,
                    ),
                ),
            ),
        },
    ),
}

_EXPERIMENTAL_EFFECTS: dict[str, ExperimentalEffect] = {
    "special_fsd_massmanager": ExperimentalEffect(
        symbol="Special_FSD_MassManager",
        name="Mass Manager",
        target_modules=("Frame Shift Drive",),
        ingredients=(
            RecipeIngredient(
                material_symbol="chemicalprocessors",
                name="Chemical Processors",
                count=1,
            ),
            RecipeIngredient(
                material_symbol="disruptedwakeechoes",
                name="Disrupted Wake Echoes",
                count=1,
            ),
        ),
        modifiers=(
            AttributeModifier(
                attribute_name="FSDOptimalMass",
                is_positive=True,
                multiplier=1.04,
            ),
            AttributeModifier(
                attribute_name="Integrity",
                is_positive=False,
                multiplier=0.92,
            ),
        ),
    ),
}

_ENGINEERS: dict[int, EngineerEntity] = {
    300000: EngineerEntity(
        engineer_id=300000,
        name="Felicity Farseer",
        system_name="Deciat",
        station_name="Farseer Inc",
        coordinates=Coordinates3D(x=122.625, y=-0.8125, z=-47.28125),
        specialties=("Frame Shift Drive", "Thrusters", "Sensors"),
    ),
    300010: EngineerEntity(
        engineer_id=300010,
        name="Elvira Martuuk",
        system_name="Khun",
        station_name="Long Sight Base",
        coordinates=Coordinates3D(x=-78.84375, y=-144.375, z=-159.28125),
        specialties=("Frame Shift Drive", "Shield Generators"),
    ),
}


class StaticEngineeringCatalogAdapter(EngineeringCatalogProviderPort):
    """In-memory provider for pre-compiled engineering blueprints and engineers."""

    def get_blueprint(self, symbol: str) -> EngineeringBlueprint | None:
        return _BLUEPRINTS.get(symbol.lower())

    def get_experimental_effect(self, symbol: str) -> ExperimentalEffect | None:
        return _EXPERIMENTAL_EFFECTS.get(symbol.lower())

    def get_engineer(self, engineer_id: int) -> EngineerEntity | None:
        return _ENGINEERS.get(engineer_id)

    def list_engineers(self) -> list[EngineerEntity]:
        return list(_ENGINEERS.values())
