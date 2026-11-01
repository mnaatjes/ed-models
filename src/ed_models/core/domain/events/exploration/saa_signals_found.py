"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class SAASignalsFoundSignalsItem:
    """Nested value object for SAASignalsFound.SignalsItem."""

    Type: str | None = None
    Type_Localised: str | None = None
    Count: int | None = None


@dataclass(slots=True, kw_only=True)
class SAASignalsFoundGenusesItem:
    """Nested value object for SAASignalsFound.GenusesItem."""

    Genus: str | None = None
    Genus_Localised: str | None = None


@dataclass(slots=True, kw_only=True)
class SAASignalsFound(JournalEvent):
    """Written when using SAA scanner on a planet or rings."""

    SystemAddress: int | None = None
    BodyName: str | None = None
    BodyID: int | None = None
    Signals: list[SAASignalsFoundSignalsItem] | None = None
    Genuses: list[SAASignalsFoundGenusesItem] | None = None
