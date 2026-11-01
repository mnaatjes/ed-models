"""Domain enumeration authority generated from kayahr/ed-journal."""

from enum import StrEnum


class BodyType(StrEnum):
    """Body types. *"""

    PLANET = "Planet"
    STATION = "Station"
    STAR = "Star"
    PLANETARY_RING = "PlanetaryRing"
    ASTEROID_CLUSTER = "AsteroidCluster"
    NULL = "Null"
    STELLAR_RING = "StellarRing"
    RING = "Ring"
