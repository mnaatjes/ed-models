"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class PassengersManifestItem:
    """Nested value object for Passengers.ManifestItem."""

    MissionID: int | None = None
    Type: str | None = None
    VIP: bool | None = None
    Wanted: bool | None = None
    Count: int | None = None


@dataclass(slots=True, kw_only=True)
class Passengers(JournalEvent):
    """List of passengers in the ship. Written at startup when loading the saved game file."""

    Manifest: list[PassengersManifestItem] | None = None
