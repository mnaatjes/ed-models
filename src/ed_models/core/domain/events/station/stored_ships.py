"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class StoredShipsShipsHereItem:
    """Nested value object for StoredShips.ShipsHereItem."""

    Hot: bool | None = None
    Name: str | None = None
    ShipID: int | None = None
    ShipType: str | None = None
    ShipType_Localised: str | None = None
    Value: int | float | None = None


@dataclass(slots=True, kw_only=True)
class StoredShipsShipsRemoteItem:
    """Nested value object for StoredShips.ShipsRemoteItem."""

    Hot: bool | None = None
    InTransit: bool | None = None
    Name: str | None = None
    ShipID: int | None = None
    ShipMarketID: int | None = None
    ShipType: str | None = None
    ShipType_Localised: str | None = None
    StarSystem: str | None = None
    TransferPrice: int | None = None
    TransferTime: int | float | None = None
    Value: int | float | None = None


@dataclass(slots=True, kw_only=True)
class StoredShips(JournalEvent):
    MarketID: int | None = None
    ShipsHere: list[StoredShipsShipsHereItem] | None = None
    ShipsRemote: list[StoredShipsShipsRemoteItem] | None = None
    StarSystem: str | None = None
    StationName: str | None = None
