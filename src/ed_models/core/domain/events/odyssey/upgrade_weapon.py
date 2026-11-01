"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class UpgradeWeaponResourcesItem:
    """Nested value object for UpgradeWeapon.ResourcesItem."""

    Name: str | None = None
    Name_Localised: str | None = None
    Count: int | None = None


@dataclass(slots=True, kw_only=True)
class UpgradeWeapon(JournalEvent):
    Name: str | None = None
    Name_Localised: str | None = None
    Class: int | float | None = None
    SuitModuleID: int | None = None
    Cost: int | None = None
    Resources: list[UpgradeWeaponResourcesItem] | None = None
