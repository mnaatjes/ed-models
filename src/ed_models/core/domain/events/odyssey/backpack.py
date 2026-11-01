"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class BackpackItem(JournalEvent):
    Name: str | None = None
    Name_Localised: str | None = None
    OwnerID: int | None = None
    Count: int | None = None
    MissionID: int | None = None


@dataclass(slots=True, kw_only=True)
class Backpack(JournalEvent):
    Items: list[BackpackItem] | None = None
    Components: list[BackpackItem] | None = None
    Consumables: list[BackpackItem] | None = None
    Data: list[BackpackItem] | None = None
