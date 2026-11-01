"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class ShipLockerItem(JournalEvent):
    Name: str | None = None
    Name_Localised: str | None = None
    OwnerID: int | None = None
    Count: int | None = None
    MissionID: int | None = None


@dataclass(slots=True, kw_only=True)
class ShipLocker(JournalEvent):
    """Lists the contents of the ship locker, eg at startup. The full list is written into the journal at startup (if in a ship) and when boarding a ship. For other updates the ship locker has to be watched separately."""

    Items: list[ShipLockerItem] | None = None
    Components: list[ShipLockerItem] | None = None
    Consumables: list[ShipLockerItem] | None = None
    Data: list[ShipLockerItem] | None = None
