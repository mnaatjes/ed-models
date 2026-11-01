"""Unit tests for remaining codified game domains.

Governed by ADR 0005, SDD-006, and hexagonal boundary quality gates.
"""

from __future__ import annotations

import pytest

from ed_models.adapters.driven.static_catalogs.engineering_catalog import (
    StaticEngineeringCatalogAdapter,
)
from ed_models.core.domain.bodies.planet import PlanetaryBody
from ed_models.core.domain.bodies.star import StarBody
from ed_models.core.domain.exceptions import DomainValidationError
from ed_models.core.domain.flight.jump import JumpCalculationParameters
from ed_models.core.domain.odyssey.suit import SuitEntity, SuitWeaponEntity
from ed_models.core.domain.spatial.coordinates import Coordinates3D
from ed_models.core.domain.status.flags import StatusFlags, StatusFlags2
from ed_models.core.domain.status.telemetry import StatusTelemetry
from ed_models.core.domain.types.planet_class import PlanetClass
from ed_models.core.domain.types.star_type import StarType
from ed_models.core.use_cases.execute_jump_calculation import ExecuteJumpCalculationUseCase


def test_status_flags_bitfield_decomposition() -> None:
    """Verifies that StatusFlags and StatusFlags2 decompose discrete states accurately."""
    # Bitmask representing docked, landing gear down, shields up
    flags = StatusFlags.DOCKED | StatusFlags.LANDING_GEAR_DOWN | StatusFlags.SHIELDS_UP

    assert flags & StatusFlags.DOCKED
    assert flags & StatusFlags.LANDING_GEAR_DOWN
    assert flags & StatusFlags.SHIELDS_UP
    assert not (flags & StatusFlags.SUPERCRUISE)

    # Status telemetry entity
    telemetry = StatusTelemetry(
        flags=flags,
        flags2=StatusFlags2.ON_FOOT | StatusFlags2.BREATHABLE_ATMOSPHERE,
        fuel_main=32.0,
        fuel_reservoir=0.5,
        cargo=4,
        pips=(4, 4, 4),
    )

    assert telemetry.is_docked is True
    assert telemetry.is_landed is False
    assert telemetry.is_on_foot is True


def test_status_telemetry_validation_guards() -> None:
    """Verifies that StatusTelemetry rejects invalid bounds."""
    with pytest.raises(DomainValidationError):
        StatusTelemetry(fuel_main=-1.0)

    with pytest.raises(DomainValidationError):
        StatusTelemetry(cargo=-5)

    with pytest.raises(DomainValidationError):
        StatusTelemetry(pips=(4, 4))  # type: ignore[arg-type]


def test_star_and_planetary_body_models() -> None:
    """Verifies celestial body domain entities."""
    star = StarBody(
        body_id=1,
        name="Sol",
        star_type=StarType.G,
        solar_masses=1.0,
        solar_radii=1.0,
        surface_temperature_k=5778.0,
        luminosity_class="V",
        is_main_star=True,
    )
    assert star.name == "Sol"
    assert star.star_type == StarType.G

    planet = PlanetaryBody(
        body_id=2,
        name="Earth",
        planet_class=PlanetClass.EARTHLIKE_BODY,
        earth_masses=1.0,
        radius_km=6371.0,
        surface_gravity_g=1.0,
        surface_pressure_atm=1.0,
        surface_temperature_k=288.0,
        is_landable=False,
        atmosphere_type="Nitrogen-Oxygen",
    )
    assert planet.surface_gravity_g == 1.0
    assert planet.is_landable is False


def test_odyssey_suit_and_weapon_entities() -> None:
    """Verifies Odyssey on-foot equipment models."""
    suit = SuitEntity(
        suit_id=1,
        symbol="tacticalsuit_class1",
        name="Dominator Suit",
        primary_weapons_capacity=2,
        secondary_weapons_capacity=1,
        base_shields=15.0,
        base_health=100.0,
        mod_slots=4,
    )
    assert suit.name == "Dominator Suit"
    assert suit.primary_weapons_capacity == 2

    weapon = SuitWeaponEntity(
        weapon_id=101,
        symbol="wpn_m_assaultrifle_plasma",
        name="Aphelion",
        damage_type="Plasma",
        clip_size=25,
        fire_rate=6.5,
    )
    assert weapon.damage_type == "Plasma"
    assert weapon.clip_size == 25


def test_engineering_catalog_lookups() -> None:
    """Verifies static catalog lookups for blueprints, experimental effects, and engineers."""
    catalog = StaticEngineeringCatalogAdapter()

    blueprint = catalog.get_blueprint("fsd_longrange")
    assert blueprint is not None
    assert blueprint.name == "Increased Range"
    assert 1 in blueprint.grades
    assert 5 in blueprint.grades
    assert blueprint.grades[5].modifiers[0].attribute_name == "FSDOptimalMass"

    effect = catalog.get_experimental_effect("special_fsd_massmanager")
    assert effect is not None
    assert effect.name == "Mass Manager"

    engineer = catalog.get_engineer(300000)
    assert engineer is not None
    assert engineer.name == "Felicity Farseer"
    assert engineer.system_name == "Deciat"
    assert engineer.coordinates == Coordinates3D(x=122.625, y=-0.8125, z=-47.28125)


def test_execute_jump_calculation_interactor() -> None:
    """Verifies Frame Shift Drive jump range calculation interactor against physics formulas."""
    interactor = ExecuteJumpCalculationUseCase()

    # Anaconda with 6A FSD specification
    params = JumpCalculationParameters(
        fsd_optimal_mass=2700.0,
        fsd_max_fuel_per_jump=8.0,
        fsd_fuel_multiplier=0.012,
        fsd_fuel_power=2.75,
        unladen_mass=450.0,
        cargo_mass=0.0,
        fuel_mass=32.0,
    )

    result = interactor.execute(params)
    assert result.current_jump_range_ly > 40.0
    assert result.unladen_jump_range_ly == result.current_jump_range_ly
    assert result.max_jump_range_ly > result.current_jump_range_ly
    assert result.fuel_consumed == 8.0
