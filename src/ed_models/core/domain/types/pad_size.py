"""Landing pad size requirements."""

from enum import StrEnum


class PadSize(StrEnum):
    """Starport docking pad size classification."""

    SMALL = "Small"
    MEDIUM = "Medium"
    LARGE = "Large"
    NONE = "None"
