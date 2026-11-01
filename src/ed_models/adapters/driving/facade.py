"""Unified driving facade adapter for ed-models.

Governed by ADR 0001, ADR 0002, ADR 0007, and SDD-008.
"""

from __future__ import annotations

import re
from typing import Any

from ed_models.core.domain.commodities.commodity import CommodityEntity
from ed_models.core.domain.engineering.blueprint import (
    EngineeringBlueprint,
    ExperimentalEffect,
)
from ed_models.core.domain.engineering.engineer import EngineerEntity
from ed_models.core.domain.events.base import JournalEvent
from ed_models.core.domain.events.parser import parse_journal_event
from ed_models.core.domain.flight.jump import (
    JumpCalculationParameters,
    JumpCalculationResult,
)
from ed_models.core.domain.interop.coriolis import serialize_coriolis_loadout
from ed_models.core.domain.interop.trade_dangerous import (
    TradeDangerousMarketRecord,
    format_trade_dangerous,
)
from ed_models.core.domain.ships.hull import ShipHull
from ed_models.core.domain.ships.module import ShipModule
from ed_models.core.domain.status.flags import StatusFlags, StatusFlags2
from ed_models.core.domain.status.telemetry import StatusTelemetry
from ed_models.core.ports.driven.commodity_catalog_port import CommodityCatalogProviderPort
from ed_models.core.ports.driven.engineering_catalog_port import EngineeringCatalogProviderPort
from ed_models.core.ports.driven.module_catalog_port import ModuleCatalogProviderPort
from ed_models.core.ports.driven.ship_catalog_port import ShipCatalogProviderPort
from ed_models.core.use_cases.execute_jump_calculation import ExecuteJumpCalculationUseCase

_CLEAN_TOKEN_RE = re.compile(r"^\$?([a-zA-Z0-9_]+?)(?:_name)?(?:;)?$")


class EliteDomainFacade:
    """Unified stateless driving entry point for static lookups, normalization, and math."""

    def __init__(
        self,
        ship_catalog: ShipCatalogProviderPort,
        module_catalog: ModuleCatalogProviderPort,
        commodity_catalog: CommodityCatalogProviderPort,
        engineering_catalog: EngineeringCatalogProviderPort,
        jump_calculator: ExecuteJumpCalculationUseCase,
    ) -> None:
        self._ship_catalog = ship_catalog
        self._module_catalog = module_catalog
        self._commodity_catalog = commodity_catalog
        self._engineering_catalog = engineering_catalog
        self._jump_calculator = jump_calculator

    # --- Pillar 1: Static Catalog Lookups (O(1)) ---

    def get_ship(self, symbol: str) -> ShipHull | None:
        """Retrieves ship hull specification by model or symbol."""
        return self._ship_catalog.get_hull_spec(symbol)

    def list_ships(self) -> list[ShipHull]:
        """Lists all compiled ship hulls."""
        return self._ship_catalog.list_all_hulls()

    def get_module_by_id(self, fdev_id: int) -> ShipModule | None:
        """Retrieves ship outfitting module by Frontier ID."""
        return self._module_catalog.get_module_by_id(fdev_id)

    def get_module_by_symbol(self, symbol: str) -> ShipModule | None:
        """Retrieves ship outfitting module by canonical symbol."""
        return self._module_catalog.get_module_by_symbol(symbol)

    def get_commodity_by_id(self, fdev_id: int) -> CommodityEntity | None:
        """Retrieves trade commodity by Frontier ID."""
        return self._commodity_catalog.get_commodity_by_id(fdev_id)

    def get_commodity_by_symbol(self, symbol: str) -> CommodityEntity | None:
        """Retrieves trade commodity by canonical symbol."""
        return self._commodity_catalog.get_commodity_by_symbol(symbol)

    def get_blueprint(self, symbol: str) -> EngineeringBlueprint | None:
        """Retrieves engineering blueprint by canonical symbol."""
        return self._engineering_catalog.get_blueprint(symbol)

    def get_experimental_effect(self, symbol: str) -> ExperimentalEffect | None:
        """Retrieves engineering experimental effect by canonical symbol."""
        return self._engineering_catalog.get_experimental_effect(symbol)

    def get_engineer(self, engineer_id: int) -> EngineerEntity | None:
        """Retrieves engineer details by Frontier engineer ID."""
        return self._engineering_catalog.get_engineer(engineer_id)

    def list_engineers(self) -> list[EngineerEntity]:
        """Lists all registered Frontier engineers."""
        return self._engineering_catalog.list_engineers()

    # --- Pillar 2: Deterministic Token & Telemetry Normalization ---

    def normalize_commodity(self, token: str) -> CommodityEntity | None:
        """Normalizes an internal Frontier token to a canonical CommodityEntity."""
        if not token:
            return None
        match = _CLEAN_TOKEN_RE.match(token.strip())
        lookup_key = match.group(1).lower() if match else token.strip().lower()
        return self._commodity_catalog.get_commodity_by_symbol(lookup_key)

    def parse_telemetry(
        self,
        *,
        flags: int,
        flags2: int = 0,
        pips: tuple[int, int, int] = (4, 4, 4),
        fuel_main: float = 0.0,
        fuel_reservoir: float = 0.0,
        cargo: int = 0,
        legal_state: str = "Clean",
    ) -> StatusTelemetry:
        """Constructs a validated StatusTelemetry entity from raw cockpit flags."""
        return StatusTelemetry(
            flags=StatusFlags(flags),
            flags2=StatusFlags2(flags2),
            pips=pips,
            fuel_main=fuel_main,
            fuel_reservoir=fuel_reservoir,
            cargo=cargo,
            legal_state=legal_state,
        )

    def parse_journal_event(self, payload: dict[str, Any]) -> JournalEvent:
        """Parses a raw Frontier journal payload into a typed JournalEvent instance."""
        return parse_journal_event(payload)

    # --- Pillar 3: Pure Mathematical Interactors ---

    def calculate_jump_range(self, params: JumpCalculationParameters) -> JumpCalculationResult:
        """Calculates vessel Frame Shift Drive jump range based on Newtonian physics."""
        return self._jump_calculator.execute(params)

    def format_trade_dangerous(
        self, records: list[TradeDangerousMarketRecord], timestamp_str: str
    ) -> str:
        """Formats records as a Trade Dangerous ASCII market dump."""
        return format_trade_dangerous(records, timestamp_str)

    def serialize_coriolis(self, loadout: dict[str, Any]) -> str:
        """Compresses and encodes a ship loadout for Coriolis URL hashes."""
        return serialize_coriolis_loadout(loadout)
