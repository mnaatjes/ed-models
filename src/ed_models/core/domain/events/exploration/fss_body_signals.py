"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class FSSBodySignalsSignalsItem:
    """Nested value object for FSSBodySignals.SignalsItem."""

    Type: str | None = None
    Type_Localised: str | None = None
    Count: int | None = None


@dataclass(slots=True, kw_only=True)
class FSSBodySignals(JournalEvent):
    BodyName: str | None = None
    BodyID: int | None = None
    SystemAddress: int | None = None
    Signals: list[FSSBodySignalsSignalsItem] | None = None
