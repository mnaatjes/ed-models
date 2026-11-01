"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class PayLegacyFines(JournalEvent):
    Amount: int | None = None
    BrokerPercentage: int | float | None = None
