"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class CommitCrime(JournalEvent):
    Bounty: int | None = None
    CrimeType: str | None = None
    Faction: str | None = None
    Fine: int | float | None = None
    Victim: str | None = None
    Victim_Localised: str | None = None
