"""Trade Dangerous market records and text formatting.

Governed by ADR 0001, ADR 0006, and SDD-007.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class TradeDangerousMarketRecord:
    """Individual commodity price and supply/demand record."""

    system_name: str
    station_name: str
    market_id: int
    commodity_name: str
    sell_price_cr: int
    buy_price_cr: int
    demand: int
    stock: int


def format_trade_dangerous(records: list[TradeDangerousMarketRecord], timestamp_str: str) -> str:
    """Formats records as Trade Dangerous ASCII market dump."""
    if not records:
        return ""

    first = records[0]
    lines = [
        "# Trade Dangerous Market Export",
        f"# Generated at {timestamp_str}",
        f"@ System: {first.system_name}",
        f"+ Station: {first.station_name}",
        f"$ MarketId: {first.market_id}",
        "# Commodity               Sell        Buy       Demand      Stock",
    ]

    for r in records:
        lines.append(
            f"{r.commodity_name:<24} {r.sell_price_cr:>8} {r.buy_price_cr:>10} {r.demand:>12} {r.stock:>10}"
        )

    return "\n".join(lines) + "\n"
