"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class Reputation(JournalEvent):
    """Player's reputation on a scale of -100 to +100 with the superpowers. Written at startup after {@link Rank} and {@link Progress}. Thresholds: * -100 to -90: Hostile *  -90 to -35: Unfriendly *  -35 to   4: Neutral *    4 to  35: Cordial *   35 to  90: Friendly *   90 to 100: Allied"""

    Empire: int | float | None = None
    Federation: int | float | None = None
    Independent: int | float | None = None
    Alliance: int | float | None = None
