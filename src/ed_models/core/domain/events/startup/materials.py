"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class Material(JournalEvent):
    """A single material. *"""

    Count: int | None = None
    Name: str | None = None
    Name_Localised: str | None = None


@dataclass(slots=True, kw_only=True)
class Materials(JournalEvent):
    """Written at startup when loading from main menu into the game. Indicates the number of materials in the player's inventory."""

    Raw: list[Material] | None = None
    Encoded: list[Material] | None = None
    Manufactured: list[Material] | None = None
