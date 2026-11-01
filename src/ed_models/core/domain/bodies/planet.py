"""Planetary body domain entity.

Governed by ADR 0005 and SDD-006.
"""

from dataclasses import dataclass

from ed_models.core.domain.exceptions import DomainValidationError
from ed_models.core.domain.types.planet_class import PlanetClass


@dataclass(slots=True, kw_only=True)
class PlanetaryBody:
    """Planetary astronomical body with physics attributes."""

    body_id: int
    name: str
    planet_class: PlanetClass
    earth_masses: float
    radius_km: float
    surface_gravity_g: float
    surface_pressure_atm: float = 0.0
    surface_temperature_k: float = 0.0
    is_landable: bool = False
    atmosphere_type: str = "None"
    volcanism: str | None = None

    def __post_init__(self) -> None:
        if not self.name or not self.name.strip():
            raise DomainValidationError("Planet name cannot be empty.")
        if self.earth_masses < 0:
            raise DomainValidationError(f"Earth masses cannot be negative: {self.earth_masses}")
        if self.radius_km < 0:
            raise DomainValidationError(f"Radius cannot be negative: {self.radius_km}")
        if self.surface_gravity_g < 0:
            raise DomainValidationError(
                f"Surface gravity cannot be negative: {self.surface_gravity_g}"
            )
