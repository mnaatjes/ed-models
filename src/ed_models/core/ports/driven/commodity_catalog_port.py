"""Driven port for market commodity catalog providers."""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from ed_models.core.domain.commodities.commodity import CommodityEntity
from ed_models.core.ports.base import DrivenPort


@runtime_checkable
class CommodityCatalogProviderPort(DrivenPort, Protocol):
    """Port for querying canonical market commodities."""

    def get_commodity_by_id(self, fdev_id: int) -> CommodityEntity | None:
        """Retrieve commodity by Frontier ID."""
        ...

    def get_commodity_by_symbol(self, symbol: str) -> CommodityEntity | None:
        """Retrieve commodity by canonical internal symbol."""
        ...
