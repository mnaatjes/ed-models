"""Engineer entity domain model.

Governed by ADR 0005 and SDD-006.
"""

from dataclasses import dataclass

from ed_models.core.domain.exceptions import DomainValidationError
from ed_models.core.domain.spatial.coordinates import Coordinates3D


@dataclass(slots=True, kw_only=True)
class EngineerEntity:
    """Frontier registered engineer."""

    engineer_id: int
    name: str
    system_name: str
    station_name: str
    coordinates: Coordinates3D
    specialties: tuple[str, ...]

    def __post_init__(self) -> None:
        if self.engineer_id <= 0:
            raise DomainValidationError(f"Invalid engineer ID: {self.engineer_id}")
        if not self.name or not self.name.strip():
            raise DomainValidationError("Engineer name cannot be empty.")
        if not self.system_name or not self.system_name.strip():
            raise DomainValidationError("Engineer system name cannot be empty.")
