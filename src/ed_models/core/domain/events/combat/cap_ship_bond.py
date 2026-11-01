"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class CapShipBond(JournalEvent):
    """Written when the player has been rewarded for a capital ship combat."""

    Reward: int | None = None
    AwardingFaction: str | None = None
    AwardingFaction_Localised: str | None = None
    VictimFaction: str | None = None
    VictimFaction_Localised: str | None = None
