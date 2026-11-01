"""In-memory test doubles for driven catalog provider ports."""

from __future__ import annotations

from ed_models.core.domain.commodities.commodity import CommodityEntity
from ed_models.core.domain.engineering.blueprint import (
    EngineeringBlueprint,
    ExperimentalEffect,
)
from ed_models.core.domain.engineering.engineer import EngineerEntity
from ed_models.core.domain.ships.hull import ShipHull
from ed_models.core.domain.ships.module import ShipModule
from ed_models.core.ports.driven.commodity_catalog_port import CommodityCatalogProviderPort
from ed_models.core.ports.driven.engineering_catalog_port import EngineeringCatalogProviderPort
from ed_models.core.ports.driven.module_catalog_port import ModuleCatalogProviderPort
from ed_models.core.ports.driven.ship_catalog_port import ShipCatalogProviderPort


class FakeShipCatalogProviderAdapter(ShipCatalogProviderPort):
    """In-memory test double for ShipCatalogProviderPort."""

    def __init__(self, hulls: list[ShipHull] | None = None) -> None:
        self._hulls: dict[str, ShipHull] = {h.model.lower(): h for h in (hulls or [])}

    def get_hull_spec(self, model: str) -> ShipHull | None:
        return self._hulls.get(model.lower())

    def list_all_hulls(self) -> list[ShipHull]:
        return list(self._hulls.values())


class FakeModuleCatalogProviderAdapter(ModuleCatalogProviderPort):
    """In-memory test double for ModuleCatalogProviderPort."""

    def __init__(self, modules: list[ShipModule] | None = None) -> None:
        self._by_id: dict[int, ShipModule] = {m.fdev_id: m for m in (modules or [])}
        self._by_symbol: dict[str, ShipModule] = {m.symbol.lower(): m for m in (modules or [])}

    def get_module_by_id(self, fdev_id: int) -> ShipModule | None:
        return self._by_id.get(fdev_id)

    def get_module_by_symbol(self, symbol: str) -> ShipModule | None:
        return self._by_symbol.get(symbol.lower())


class FakeCommodityCatalogProviderAdapter(CommodityCatalogProviderPort):
    """In-memory test double for CommodityCatalogProviderPort."""

    def __init__(self, commodities: list[CommodityEntity] | None = None) -> None:
        self._by_id: dict[int, CommodityEntity] = {c.fdev_id: c for c in (commodities or [])}
        self._by_symbol: dict[str, CommodityEntity] = {
            c.symbol.lower(): c for c in (commodities or [])
        }

    def get_commodity_by_id(self, fdev_id: int) -> CommodityEntity | None:
        return self._by_id.get(fdev_id)

    def get_commodity_by_symbol(self, symbol: str) -> CommodityEntity | None:
        return self._by_symbol.get(symbol.lower())


class FakeEngineeringCatalogProviderAdapter(EngineeringCatalogProviderPort):
    """In-memory test double for EngineeringCatalogProviderPort."""

    def __init__(
        self,
        blueprints: list[EngineeringBlueprint] | None = None,
        effects: list[ExperimentalEffect] | None = None,
        engineers: list[EngineerEntity] | None = None,
    ) -> None:
        self._blueprints = {b.symbol.lower(): b for b in (blueprints or [])}
        self._effects = {e.symbol.lower(): e for e in (effects or [])}
        self._engineers = {eng.engineer_id: eng for eng in (engineers or [])}

    def get_blueprint(self, symbol: str) -> EngineeringBlueprint | None:
        return self._blueprints.get(symbol.lower())

    def get_experimental_effect(self, symbol: str) -> ExperimentalEffect | None:
        return self._effects.get(symbol.lower())

    def get_engineer(self, engineer_id: int) -> EngineerEntity | None:
        return self._engineers.get(engineer_id)

    def list_engineers(self) -> list[EngineerEntity]:
        return list(self._engineers.values())
