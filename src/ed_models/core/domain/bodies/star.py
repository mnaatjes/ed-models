"""Star celestial body domain entity.

Governed by ADR 0005 and SDD-006.
"""

from dataclasses import dataclass

from ed_models.core.domain.exceptions import DomainValidationError
from ed_models.core.domain.types.star_type import StarType


@dataclass(slots=True, kw_only=True)
class StarBody:
    """Stellar astronomical body."""

    body_id: int
    name: str
    star_type: StarType
    solar_masses: float
    solar_radii: float
    surface_temperature_k: float
    luminosity_class: str
    is_main_star: bool = False

    def __post_init__(self) -> None:
        if not self.name or not self.name.strip():
            raise DomainValidationError("Star name cannot be empty.")
        if self.solar_masses < 0:
            raise DomainValidationError(f"Solar masses cannot be negative: {self.solar_masses}")
        if self.solar_radii < 0:
            raise DomainValidationError(f"Solar radii cannot be negative: {self.solar_radii}")
        if self.surface_temperature_k < 0:
            raise DomainValidationError(
                f"Surface temperature cannot be negative: {self.surface_temperature_k}"
            )
