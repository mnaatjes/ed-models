"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class Shipyard(JournalEvent):
    """Written when accessing shipyard in a station."""

    MarketID: int | None = None
    StarSystem: str | None = None
    StationName: str | None = None


@dataclass(slots=True, kw_only=True)
class ExtendedShipyardPriceListItem:
    """Nested value object for ExtendedShipyard.PriceListItem."""

    id: int | None = None
    ShipType: str | None = None
    ShipType_Localised: str | None = None
    ShipPrice: int | None = None


@dataclass(slots=True, kw_only=True)
class ExtendedShipyard(Shipyard):
    """Extended shipyard info written to separate 'Shipyard.json' file."""

    Horizons: bool | None = None
    AllowCobraMkIV: bool | None = None
    PriceList: list[ExtendedShipyardPriceListItem] | None = None
