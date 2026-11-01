"""Ship module and outfitting equipment entity."""

from dataclasses import dataclass

from ed_models.core.domain.exceptions import DomainValidationError


@dataclass(slots=True, kw_only=True)
class ShipModule:
    """Ship module specification."""

    fdev_id: int
    symbol: str
    name: str
    class_num: int
    rating: str
    mass: float
    power_draw: float | None = None

    def __post_init__(self) -> None:
        """Validates module invariants."""
        if not self.symbol or not self.symbol.strip():
            raise DomainValidationError("Module symbol cannot be empty.")
        if self.mass < 0:
            raise DomainValidationError(f"Module mass cannot be negative: {self.mass}")
