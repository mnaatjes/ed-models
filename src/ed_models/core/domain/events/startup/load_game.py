"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass
from enum import StrEnum

from ed_models.core.domain.events.base import JournalEvent


class GameMode(StrEnum):
    """The game mode. *"""

    OPEN = "Open"
    SOLO = "Solo"
    GROUP = "Group"


@dataclass(slots=True, kw_only=True)
class LoadGame(JournalEvent):
    """Written at startup when loading from main menu into the game."""

    Commander: str | None = None
    FID: str | None = None
    Horizons: bool | None = None
    Odyssey: bool | None = None
    Ship: str | None = None
    ShipID: int | None = None
    Ship_Localised: str | None = None
    StartLanded: bool | None = None
    StartDead: bool | None = None
    GameMode: GameMode | None = None
    Group: str | None = None
    Credits: int | float | None = None
    Loan: int | float | None = None
    ShipName: str | None = None
    ShipIdent: str | None = None
    FuelLevel: int | None = None
    FuelCapacity: int | None = None
    language: str | None = None
    gameversion: str | None = None
    build: str | None = None
