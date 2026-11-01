"""Driven port for outfitting module catalog providers."""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from ed_models.core.domain.ships.module import ShipModule
from ed_models.core.ports.base import DrivenPort


@runtime_checkable
class ModuleCatalogProviderPort(DrivenPort, Protocol):
    """Port for querying outfitting modules."""

    def get_module_by_id(self, fdev_id: int) -> ShipModule | None:
        """Retrieve module by Frontier ID."""
        ...

    def get_module_by_symbol(self, symbol: str) -> ShipModule | None:
        """Retrieve module by internal symbol."""
        ...
