"""Odyssey suit and weapon domain entities.

Governed by ADR 0005 and SDD-006.
"""

from dataclasses import dataclass

from ed_models.core.domain.exceptions import DomainValidationError


@dataclass(slots=True, kw_only=True)
class SuitEntity:
    """Odyssey personal flight / combat suit."""

    suit_id: int
    symbol: str
    name: str
    primary_weapons_capacity: int
    secondary_weapons_capacity: int
    base_shields: float
    base_health: float
    mod_slots: int

    def __post_init__(self) -> None:
        if self.suit_id <= 0:
            raise DomainValidationError(f"Invalid suit ID: {self.suit_id}")
        if not self.symbol or not self.symbol.strip():
            raise DomainValidationError("Suit symbol cannot be empty.")
        if self.base_shields < 0:
            raise DomainValidationError(f"Base shields cannot be negative: {self.base_shields}")
        if self.base_health <= 0:
            raise DomainValidationError(f"Base health must be positive: {self.base_health}")


@dataclass(slots=True, kw_only=True)
class SuitWeaponEntity:
    """Odyssey personal handheld weapon."""

    weapon_id: int
    symbol: str
    name: str
    damage_type: str
    clip_size: int
    fire_rate: float

    def __post_init__(self) -> None:
        if self.weapon_id <= 0:
            raise DomainValidationError(f"Invalid weapon ID: {self.weapon_id}")
        if not self.symbol or not self.symbol.strip():
            raise DomainValidationError("Weapon symbol cannot be empty.")
        if self.clip_size <= 0:
            raise DomainValidationError(f"Clip size must be positive: {self.clip_size}")
        if self.fire_rate <= 0:
            raise DomainValidationError(f"Fire rate must be positive: {self.fire_rate}")
