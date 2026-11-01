"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class FactionKillBond(JournalEvent):
    """Written when player is rewarded for taking part in a combat zone."""

    Reward: int | None = None
    AwardingFaction: str | None = None
    AwardingFaction_Localised: str | None = None
    VictimFaction: str | None = None
    VictimFaction_Localised: str | None = None
