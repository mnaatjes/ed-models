"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class ScanBaryCentre(JournalEvent):
    """Written when scanning a body of a binary pair. YOu will now get an event detailing the orbital parameters of their barycenter."""

    StarSystem: str | None = None
    SystemAddress: int | None = None
    BodyID: int | None = None
    SemiMajorAxis: int | float | None = None
    Eccentricity: int | float | None = None
    OrbitalInclination: int | float | None = None
    Periapsis: int | float | None = None
    OrbitalPeriod: int | float | None = None
    AscendingNode: int | float | None = None
    MeanAnomaly: int | float | None = None
