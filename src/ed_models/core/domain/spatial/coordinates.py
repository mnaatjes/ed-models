"""Pure 3D coordinates value object.

Governed by ADR 0001, ADR 0002, and SDD-002.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Coordinates3D:
    """Immutable 3D spatial vector in light years (x, y, z)."""

    x: float
    y: float
    z: float
