"""Flight mechanics and jump calculation value objects.

Governed by ADR 0005, SDD-006, and EDMC physics formulas.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class JumpCalculationParameters:
    """Parameters required to calculate Frame Shift Drive jump range."""

    fsd_optimal_mass: float
    fsd_max_fuel_per_jump: float
    fsd_fuel_multiplier: float
    fsd_fuel_power: float
    unladen_mass: float
    cargo_mass: float
    fuel_mass: float
    fsd_flat_boost_ly: float = 0.0
    fsd_multiplier_boost: float = 1.0


@dataclass(frozen=True, slots=True)
class JumpCalculationResult:
    """Result of FSD jump range evaluation."""

    unladen_jump_range_ly: float
    current_jump_range_ly: float
    max_jump_range_ly: float
    fuel_consumed: float
