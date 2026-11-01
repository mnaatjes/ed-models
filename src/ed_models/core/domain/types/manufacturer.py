"""Ship manufacturer taxonomy."""

from enum import StrEnum


class Manufacturer(StrEnum):
    """Canonical spaceship manufacturers in Elite Dangerous."""

    FAULCON_DE_LACY = "Faulcon DeLacy"
    CORE_DYNAMICS = "Core Dynamics"
    GUTAMAYA = "Gutamaya"
    LAKON_SPACEWAYS = "Lakon Spaceways"
    SAUD_KRUGER = "Saud Kruger"
    ZORGON_PETERSON = "Zorgon Peterson"
    UNKNOWN = "Unknown"
