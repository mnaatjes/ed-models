"""Flight mechanics jump calculation interactor."""

from __future__ import annotations

from ed_models.core.domain.exceptions import DomainValidationError
from ed_models.core.domain.flight.jump import (
    JumpCalculationParameters,
    JumpCalculationResult,
)


class ExecuteJumpCalculationUseCase:
    """Calculates FSD jump ranges based on Frontier Newtonian jump formulas."""

    def __init__(self) -> None:
        """Stateless interactor constructor."""
        pass

    def execute(self, params: JumpCalculationParameters) -> JumpCalculationResult:
        """Executes jump range calculation."""
        if params.fsd_optimal_mass <= 0:
            raise DomainValidationError("FSD optimal mass must be positive.")
        if params.fsd_max_fuel_per_jump <= 0:
            raise DomainValidationError("FSD max fuel per jump must be positive.")
        if params.fsd_fuel_power <= 0:
            raise DomainValidationError("FSD fuel power must be positive.")
        if params.fsd_fuel_multiplier <= 0:
            raise DomainValidationError("FSD fuel multiplier must be positive.")

        # Total mass configurations
        current_mass = params.unladen_mass + params.cargo_mass + params.fuel_mass
        unladen_mass = params.unladen_mass + params.fuel_mass
        max_mass = params.unladen_mass + params.fsd_max_fuel_per_jump

        if current_mass <= 0:
            raise DomainValidationError("Total vessel mass must be positive.")

        # Formula: range = (opt_mass / total_mass) * (fuel / fuel_mult) ** (1 / fuel_power)
        fuel_ratio = (params.fsd_max_fuel_per_jump / params.fsd_fuel_multiplier) ** (
            1.0 / params.fsd_fuel_power
        )

        def calc_range(mass: float) -> float:
            base_range = (params.fsd_optimal_mass / mass) * fuel_ratio
            boosted = (base_range * params.fsd_multiplier_boost) + params.fsd_flat_boost_ly
            return round(boosted, 2)

        current_range = calc_range(current_mass)
        unladen_range = calc_range(unladen_mass)
        max_range = calc_range(max_mass)

        return JumpCalculationResult(
            current_jump_range_ly=current_range,
            unladen_jump_range_ly=unladen_range,
            max_jump_range_ly=max_range,
            fuel_consumed=params.fsd_max_fuel_per_jump,
        )
