"""Driven static catalog adapters."""

from ed_models.adapters.driven.static_catalogs.commodities_catalog import (
    StaticCommodityCatalogAdapter,
)
from ed_models.adapters.driven.static_catalogs.modules_catalog import StaticModuleCatalogAdapter
from ed_models.adapters.driven.static_catalogs.ships_catalog import StaticShipCatalogAdapter

__all__ = [
    "StaticCommodityCatalogAdapter",
    "StaticModuleCatalogAdapter",
    "StaticShipCatalogAdapter",
]
