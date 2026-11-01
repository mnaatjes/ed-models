"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class CrewMemberRoleChange(JournalEvent):
    Crew: str | None = None
    Role: str | None = None
    Telepresence: bool | None = None
