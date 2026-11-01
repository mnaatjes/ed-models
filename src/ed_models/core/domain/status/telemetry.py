"""Status telemetry domain entity.

Governed by ADR 0005 and SDD-006.
"""

from dataclasses import dataclass, field

from ed_models.core.domain.exceptions import DomainValidationError
from ed_models.core.domain.spatial.coordinates import Coordinates3D
from ed_models.core.domain.status.flags import StatusFlags, StatusFlags2


@dataclass(slots=True, kw_only=True)
class StatusTelemetry:
    """Decoded vehicle telemetry snapshot."""

    flags: StatusFlags = StatusFlags(0)
    flags2: StatusFlags2 = StatusFlags2(0)
    pips: tuple[int, int, int] = (4, 4, 4)  # (sys, eng, wpn) half-pips (0-8)
    firegroup: int = 0
    gui_focus: int = 0
    fuel_main: float = 0.0
    fuel_reservoir: float = 0.0
    cargo: int = 0
    legal_state: str = "Clean"
    latitude: float | None = None
    longitude: float | None = None
    altitude: float | None = None
    heading: float | None = None
    body_name: str | None = None
    planet_radius: float | None = None
    coordinates: Coordinates3D | None = None
    oxygen: float | None = None
    health: float | None = None
    temperature: float | None = None
    selected_weapon: str | None = None
    gravity: float | None = None
    additional_fields: dict[str, object] = field(default_factory=dict)

    def __post_init__(self) -> None:
        """Validates telemetry bounds."""
        if self.fuel_main < 0:
            raise DomainValidationError(f"Main fuel cannot be negative: {self.fuel_main}")
        if self.fuel_reservoir < 0:
            raise DomainValidationError(f"Reservoir fuel cannot be negative: {self.fuel_reservoir}")
        if self.cargo < 0:
            raise DomainValidationError(f"Cargo count cannot be negative: {self.cargo}")
        if len(self.pips) != 3:
            raise DomainValidationError(f"Pips must be a 3-element tuple: {self.pips}")

    @property
    def is_docked(self) -> bool:
        return bool(self.flags & StatusFlags.DOCKED)

    @property
    def is_landed(self) -> bool:
        return bool(self.flags & StatusFlags.LANDED)

    @property
    def is_supercruise(self) -> bool:
        return bool(self.flags & StatusFlags.SUPERCRUISE)

    @property
    def is_on_foot(self) -> bool:
        return bool(self.flags2 & StatusFlags2.ON_FOOT)

    @property
    def is_in_srv(self) -> bool:
        return bool(self.flags & StatusFlags.IN_SRV)
