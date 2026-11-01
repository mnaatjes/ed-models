"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from __future__ import annotations

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent
from ed_models.core.domain.types.station_service import StationService
from ed_models.core.domain.types.station_type import StationType


@dataclass(slots=True, kw_only=True)
class DockedStationFaction:
    """Nested value object for Docked.StationFaction."""

    Name: str | None = None
    FactionState: str | None = None


@dataclass(slots=True, kw_only=True)
class DockedStationEconomiesItem:
    """Nested value object for Docked.StationEconomiesItem."""

    Name: str | None = None
    Name_Localised: str | None = None
    Proportion: int | float | None = None


@dataclass(slots=True, kw_only=True)
class DockedLandingPads:
    """Nested value object for Docked.LandingPads."""

    Small: int | float | None = None
    Medium: int | float | None = None
    Large: int | float | None = None


@dataclass(slots=True, kw_only=True)
class Docked(JournalEvent):
    """Written when landing at landing pad in a space station, output, or surface settlement. The 'anonymous docking' protocol comes into effect if you're either Wanted (ie have a local bounty) or have an ActiveFine."""

    StationName: str | None = None
    MarketID: int | None = None
    SystemAddress: int | None = None
    StationType: StationType | None = None
    StarSystem: str | None = None
    CockpitBreach: bool | None = None
    StationFaction: DockedStationFaction | None = None
    StationAllegiance: str | None = None
    StationEconomy: str | None = None
    StationEconomy_Localised: str | None = None
    StationEconomies: list[DockedStationEconomiesItem] | None = None
    StationGovernment: str | None = None
    StationGovernment_Localised: str | None = None
    DistFromStarLS: float | None = None
    StationServices: list[StationService] | None = None
    Wanted: bool | None = None
    ActiveFine: bool | None = None
    LandingPads: DockedLandingPads | None = None
    Taxi: bool | None = None
    Multicrew: bool | None = None
    StationState: str | None = None
    Security: str | None = None
    Security_Localised: str | None = None
