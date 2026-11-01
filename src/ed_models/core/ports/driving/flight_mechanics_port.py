"""Driving port contract for flight mechanics and jump calculation."""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from ed_models.core.domain.flight.jump import (
    JumpCalculationParameters,
    JumpCalculationResult,
)
from ed_models.core.ports.base import DrivingPort


@runtime_checkable
class ExecuteJumpCalculationPort(DrivingPort, Protocol):
    """Primary driving port for vessel physics and jump mechanics."""

    def calculate_jump(self, params: JumpCalculationParameters) -> JumpCalculationResult:
        """Calculates vessel jump range across unladen, current, and maximum loadouts."""
        ...
