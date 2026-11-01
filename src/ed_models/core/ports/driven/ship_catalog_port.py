"""Driven port for ship hull catalog providers."""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from ed_models.core.domain.ships.hull import ShipHull
from ed_models.core.ports.base import DrivenPort


@runtime_checkable
class ShipCatalogProviderPort(DrivenPort, Protocol):
    """Port for querying pre-compiled ship hull metadata."""

    def get_hull_spec(self, model: str) -> ShipHull | None:
        """Retrieve hull specifications by model name or symbol."""
        ...

    def list_all_hulls(self) -> list[ShipHull]:
        """List all compiled ship hulls."""
        ...
