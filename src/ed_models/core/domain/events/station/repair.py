"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class Repair(JournalEvent):
    Cost: int | None = None
    Item: str | None = None
    Item_Localised: str | None = None
    Items: list[str] | None = None
