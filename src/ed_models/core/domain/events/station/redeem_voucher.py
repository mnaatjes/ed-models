"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class RedeemVoucherFactionsItem:
    """Nested value object for RedeemVoucher.FactionsItem."""

    Amount: int | None = None
    Faction: str | None = None


@dataclass(slots=True, kw_only=True)
class RedeemVoucher(JournalEvent):
    Amount: int | None = None
    BrokerPercentage: int | float | None = None
    Faction: str | None = None
    Factions: list[RedeemVoucherFactionsItem] | None = None
    Type: str | None = None
