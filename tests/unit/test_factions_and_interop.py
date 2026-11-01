"""Unit tests for factions and interop domain entities.

Governed by ADR 0006 and SDD-007.
"""

from __future__ import annotations

import base64
import gzip
import json

import pytest

from ed_models.core.domain.exceptions import DomainValidationError
from ed_models.core.domain.factions.faction import (
    Allegiance,
    FactionState,
    Government,
    MinorFactionPresence,
)
from ed_models.core.domain.interop.coriolis import serialize_coriolis_loadout
from ed_models.core.domain.interop.trade_dangerous import (
    TradeDangerousMarketRecord,
    format_trade_dangerous,
)


def test_minor_faction_presence_validation() -> None:
    """Verifies that MinorFactionPresence validates name and influence bounds."""
    faction = MinorFactionPresence(
        faction_name="The Dark Wheel",
        allegiance=Allegiance.INDEPENDENT,
        government=Government.DEMOCRACY,
        influence=0.45,
        active_states=(FactionState.BOOM, FactionState.EXPANSION),
    )
    assert faction.faction_name == "The Dark Wheel"
    assert faction.allegiance == Allegiance.INDEPENDENT
    assert faction.influence == 0.45
    assert FactionState.BOOM in faction.active_states

    # Influence bounds validation
    with pytest.raises(DomainValidationError):
        MinorFactionPresence(
            faction_name="Invalid",
            allegiance=Allegiance.FEDERATION,
            government=Government.CORPORATE,
            influence=1.5,
        )

    with pytest.raises(DomainValidationError):
        MinorFactionPresence(
            faction_name="",
            allegiance=Allegiance.FEDERATION,
            government=Government.CORPORATE,
            influence=0.5,
        )


def test_trade_dangerous_formatter_ascii_output() -> None:
    """Verifies that TradeDangerousFormatter produces formatted table string."""
    records = [
        TradeDangerousMarketRecord(
            system_name="Sol",
            station_name="Daedalus",
            market_id=128000000,
            commodity_name="Gold",
            sell_price_cr=45000,
            buy_price_cr=46000,
            demand=1200,
            stock=8500,
        ),
        TradeDangerousMarketRecord(
            system_name="Sol",
            station_name="Daedalus",
            market_id=128000000,
            commodity_name="Silver",
            sell_price_cr=25000,
            buy_price_cr=25500,
            demand=5000,
            stock=12000,
        ),
    ]

    output = format_trade_dangerous(records, "2026-11-01 23:00:00")
    assert "@ System: Sol" in output
    assert "+ Station: Daedalus" in output
    assert "$ MarketId: 128000000" in output
    assert "Gold" in output
    assert "Silver" in output


def test_coriolis_serializer_roundtrip() -> None:
    """Verifies Coriolis loadout compression and URL-safe serialization."""
    loadout = {
        "ship": "Anaconda",
        "components": {
            "standard": {"armour": "128049382"},
        },
    }

    serialized = serialize_coriolis_loadout(loadout)
    assert isinstance(serialized, str)

    assert len(serialized) > 0

    # Verify decompress
    unquoted = serialized.replace("%3D", "=")
    decoded = base64.urlsafe_b64decode(unquoted.encode("utf-8"))
    decompressed = gzip.decompress(decoded).decode("utf-8")
    loaded = json.loads(decompressed)
    assert loaded["ship"] == "Anaconda"
