"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from __future__ import annotations

import typing
from dataclasses import dataclass
from enum import StrEnum

from ed_models.core.domain.events.base import JournalEvent
from ed_models.core.domain.types.planet_class import PlanetClass
from ed_models.core.domain.types.star_type import StarType


class ScanType(StrEnum):
    """The scan type. - `AutoScan`: Automatic scan of nearby bodies after jumping into a system. - `Basic`: A basic scan in older game versions, when no Detailed Surface Scanner was installed. - `Detailed`: Normal scan made with Full Spectrum System Scanner or in older game versions a scan made with the Detailed Surface Scanner installed. - `NavBeaconDetail`: Data learned by scanning a nav beacon."""

    AUTO_SCAN = "AutoScan"
    BASIC = "Basic"
    DETAILED = "Detailed"
    NAV_BEACON_DETAIL = "NavBeaconDetail"


class RingClass(StrEnum):
    """The ring class (Icy, Metallic, Metal Rich or Rocky). *"""

    E_RING_CLASS_ICY = "eRingClass_Icy"
    E_RING_CLASS_METALIC = "eRingClass_Metalic"
    E_RING_CLASS_METAL_RICH = "eRingClass_MetalRich"
    E_RING_CLASS_ROCKY = "eRingClass_Rocky"


class ReserveLevel(StrEnum):
    """The resource reserve level. *"""

    PRISTINE_RESOURCES = "PristineResources"
    LOW_RESOURCES = "LowResources"
    DEPLETED_RESOURCES = "DepletedResources"
    MAJOR_RESOURCES = "MajorResources"
    COMMON_RESOURCES = "CommonResources"


type Scan = ScanStar | ScanPlanet | ScanOther


@dataclass(slots=True, kw_only=True)
class Ring(JournalEvent):
    """A ring of a planet, moon or star. *"""

    Name: str | None = None
    RingClass: RingClass | None = None
    MassMT: float | None = None
    InnerRad: int | float | None = None
    OuterRad: int | float | None = None


@dataclass(slots=True, kw_only=True)
class ScanBody(JournalEvent):
    """General scan data for every type of scanned body. *"""

    ScanType: ScanType | None = None
    StarSystem: str | None = None
    SystemAddress: int | None = None
    BodyName: str | None = None
    BodyID: int | None = None
    DistanceFromArrivalLS: float | None = None
    WasDiscovered: bool | None = None
    WasMapped: bool | None = None
    WasFootfalled: bool | None = None
    Parents: list[dict[str, int]] | None = None
    SemiMajorAxis: int | float | None = None
    Eccentricity: int | float | None = None
    OrbitalInclination: int | float | None = None
    Periapsis: int | float | None = None
    OrbitalPeriod: int | float | None = None
    AscendingNode: int | float | None = None
    MeanAnomaly: int | float | None = None
    AxialTilt: int | float | None = None
    Rings: list[Ring] | None = None


@dataclass(slots=True, kw_only=True)
class ScanOther(ScanBody):
    """Scan of a body which is not a star, planet or moon. *"""

    PlanetClass: typing.Any | None = None
    StarType: typing.Any | None = None


@dataclass(slots=True, kw_only=True)
class ScanStar(ScanBody):
    """Scan of a star. Can be recognized by the existence of a `StarType` property."""

    PlanetClass: typing.Any | None = None
    StarType: StarType | None = None
    Subclass: int | float | None = None
    StellarMass: float | None = None
    Radius: float | None = None
    AbsoluteMagnitude: int | float | None = None
    RotationPeriod: int | float | None = None
    SurfaceTemperature: float | None = None
    Luminosity: str | None = None
    Age_MY: int | float | None = None


@dataclass(slots=True, kw_only=True)
class ScanPlanetAtmosphereCompositionItem:
    """Nested value object for ScanPlanet.AtmosphereCompositionItem."""

    Name: str | None = None
    Percent: int | float | None = None


@dataclass(slots=True, kw_only=True)
class ScanPlanetMaterialsItem:
    """Nested value object for ScanPlanet.MaterialsItem."""

    Name: str | None = None
    Percent: int | float | None = None


@dataclass(slots=True, kw_only=True)
class ScanPlanetComposition:
    """Nested value object for ScanPlanet.Composition."""

    Ice: int | float | None = None
    Metal: int | float | None = None
    Rock: int | float | None = None


@dataclass(slots=True, kw_only=True)
class ScanPlanet(ScanBody):
    """Scan of a planet or moon. Can be recognized by the existence of a `PlanetClass` property."""

    StarType: typing.Any | None = None
    Radius: float | None = None
    RotationPeriod: int | float | None = None
    SurfaceTemperature: float | None = None
    TidalLock: bool | None = None
    TerraformState: str | None = None
    PlanetClass: PlanetClass | None = None
    Atmosphere: str | None = None
    AtmosphereType: str | None = None
    AtmosphereComposition: list[ScanPlanetAtmosphereCompositionItem] | None = None
    Volcanism: str | None = None
    SurfaceGravity: int | float | None = None
    SurfacePressure: int | float | None = None
    Landable: bool | None = None
    Materials: list[ScanPlanetMaterialsItem] | None = None
    Composition: ScanPlanetComposition | None = None
    ReserveLevel: ReserveLevel | None = None
    MassEM: float | None = None
