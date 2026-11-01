"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class NavBeaconScan(JournalEvent):
    """Written when scanning a navigation beacon, before the scan data for all the bodies in the system is written into the journal."""

    NumBodies: int | float | None = None
    SystemAddress: int | None = None
