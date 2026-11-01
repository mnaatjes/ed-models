"""Ship hull domain entity."""

from dataclasses import dataclass, field

from ed_models.core.domain.exceptions import DomainValidationError
from ed_models.core.domain.types.manufacturer import Manufacturer
from ed_models.core.domain.types.pad_size import PadSize


@dataclass(slots=True, kw_only=True)
class ShipHull:
    """Immutable ship hull specification."""

    model: str
    name: str
    manufacturer: Manufacturer
    pad_size: PadSize
    hull_mass: float
    reserve_fuel_capacity: float
    military_slots: dict[str, int] = field(default_factory=dict)

    def __post_init__(self) -> None:
        """Validates ship hull invariants."""
        if not self.model or not self.model.strip():
            raise DomainValidationError("Ship model identifier cannot be empty.")
        if self.hull_mass < 0:
            raise DomainValidationError(f"Hull mass cannot be negative: {self.hull_mass}")
