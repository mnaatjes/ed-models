"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent
from ed_models.core.domain.types.carrier_type import CarrierType


@dataclass(slots=True, kw_only=True)
class Pack(JournalEvent):
    PackTheme: str | None = None
    PackTier: int | None = None


@dataclass(slots=True, kw_only=True)
class CarrierStatsSpaceUsage:
    """Nested value object for CarrierStats.SpaceUsage."""

    TotalCapacity: int | None = None
    Crew: int | float | None = None
    Cargo: int | float | None = None
    CargoSpaceReserved: int | float | None = None
    ShipPacks: int | float | None = None
    ModulePacks: int | float | None = None
    FreeSpace: int | float | None = None


@dataclass(slots=True, kw_only=True)
class CarrierStatsFinance:
    """Nested value object for CarrierStats.Finance."""

    CarrierBalance: int | float | None = None
    ReserveBalance: int | float | None = None
    AvailableBalance: int | float | None = None
    ReservePercent: int | float | None = None
    TaxRate_rearm: int | float | None = None
    TaxRate_refuel: float | None = None
    TaxRate_repair: int | float | None = None
    TaxRate_pioneersupplies: int | float | None = None
    TaxRate_shipyard: int | float | None = None
    TaxRate_outfitting: int | float | None = None


@dataclass(slots=True, kw_only=True)
class CarrierStatsCrewItem:
    """Nested value object for CarrierStats.CrewItem."""

    CrewRole: str | None = None
    Activated: bool | None = None
    Enabled: bool | None = None
    CrewName: str | None = None


@dataclass(slots=True, kw_only=True)
class CarrierStats(JournalEvent):
    CarrierID: int | None = None
    CarrierType: CarrierType | None = None
    Callsign: str | None = None
    Name: str | None = None
    DockingAccess: str | None = None
    AllowNotorious: bool | None = None
    FuelLevel: int | None = None
    JumpRangeCurr: int | float | None = None
    JumpRangeMax: int | float | None = None
    PendingDecommission: bool | None = None
    SpaceUsage: CarrierStatsSpaceUsage | None = None
    Finance: CarrierStatsFinance | None = None
    Crew: list[CarrierStatsCrewItem] | None = None
    ShipPacks: list[Pack] | None = None
    ModulePacks: list[Pack] | None = None
