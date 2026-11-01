"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass
from enum import StrEnum

from ed_models.core.domain.events.base import JournalEvent


class CargoVessel(StrEnum):
    """The vessel for which the cargo event is written. *"""

    SHIP = "Ship"
    S_R_V = "SRV"


@dataclass(slots=True, kw_only=True)
class CargoInventoryItem:
    """Nested value object for Cargo.InventoryItem."""

    Name: str | None = None
    Name_Localised: str | None = None
    Count: int | None = None
    Stolen: int | float | None = None
    MissionID: int | None = None


@dataclass(slots=True, kw_only=True)
class Cargo(JournalEvent):
    """Written slightly later in startup after missions are initialized so cargo coming from an abandoned delivery mission can be detected. The first Cargo event in the file will contain the full inventory. A simple event (with no Inventory property) is written to the main journal file when the cargo file is updated."""

    Vessel: CargoVessel | None = None
    Count: int | None = None
    Inventory: list[CargoInventoryItem] | None = None
