"""Base journal event model.

Governed by ADR 0001, ADR 0002, and SDD-004.
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True, kw_only=True)
class JournalEvent:
    """Base dataclass shared by all Frontier Player Journal events.

    All events must declare slots=True and kw_only=True to prevent inheritance field
    ordering conflicts (RISK-03) and minimize memory footprint (RISK-04).
    """

    timestamp: datetime | str
    event: str
