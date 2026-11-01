"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class ColonisationContributionResource(JournalEvent):
    Name: str | None = None
    Name_Localised: str | None = None
    Amount: int | None = None


@dataclass(slots=True, kw_only=True)
class ColonisationContribution(JournalEvent):
    MarketID: int | None = None
    Contributions: list[ColonisationContributionResource] | None = None
