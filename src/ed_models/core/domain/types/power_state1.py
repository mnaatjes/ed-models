"""Domain enumeration authority generated from kayahr/ed-journal."""

from enum import StrEnum


class PowerState1(StrEnum):
    """Power states in Powerplay 1.0 *"""

    IN_PREPARE_RADIUS = "InPrepareRadius"
    PREPARED = "Prepared"
    EXPLOITED = "Exploited"
    CONTESTED = "Contested"
    CONTROLLED = "Controlled"
    HOME_SYSTEM = "HomeSystem"
    TURMOIL = "Turmoil"
