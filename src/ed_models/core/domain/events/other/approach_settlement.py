"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent
from ed_models.core.domain.types.station_service import StationService


@dataclass(slots=True, kw_only=True)
class ApproachSettlementStationFaction:
    """Nested value object for ApproachSettlement.StationFaction."""

    Name: str | None = None
    FactionState: str | None = None


@dataclass(slots=True, kw_only=True)
class ApproachSettlementStationEconomiesItem:
    """Nested value object for ApproachSettlement.StationEconomiesItem."""

    Name: str | None = None
    Name_Localised: str | None = None
    Proportion: int | float | None = None


@dataclass(slots=True, kw_only=True)
class ApproachSettlement(JournalEvent):
    MarketID: int | None = None
    Name: str | None = None
    Name_Localised: str | None = None
    Latitude: int | float | None = None
    Longitude: int | float | None = None
    SystemAddress: int | None = None
    BodyID: int | None = None
    BodyName: str | None = None
    StationFaction: ApproachSettlementStationFaction | None = None
    StationGovernment: str | None = None
    StationGovernment_Localised: str | None = None
    StationAllegiance: str | None = None
    StationServices: list[StationService] | None = None
    StationEconomy: str | None = None
    StationEconomy_Localised: str | None = None
    StationEconomies: list[ApproachSettlementStationEconomiesItem] | None = None
