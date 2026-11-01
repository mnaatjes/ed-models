"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class BuyWeapon(JournalEvent):
    Name: str | None = None
    Name_Localised: str | None = None
    Class: int | float | None = None
    WeaponMods: list[str] | None = None
    Price: int | None = None
    SuitModuleID: int | None = None
