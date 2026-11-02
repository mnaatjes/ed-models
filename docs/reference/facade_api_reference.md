---
title: "EliteDomainFacade API Reference"
tags: ["docs", "reference", "facade", "api", "ed-models", "diataxis"]
created_at: "2026-11-01"
last_updated_at: "2026-11-01"
---

# EliteDomainFacade API Reference

This document provides a technical specification of [`EliteDomainFacade`](file:///home/michael/src/github.com/mnaatjes/ed-models/src/ed_models/adapters/driving/facade.py), the unified driving facade adapter for `ed-models`.

Governed by [ADR 0001](file:///home/michael/src/github.com/mnaatjes/ed-models/architecture/adr/0001_ed_models_core_game_logic_and_catalog_architecture.md), [ADR 0002](file:///home/michael/src/github.com/mnaatjes/ed-models/architecture/adr/0002_domain_scope_and_boundary_enforcement.md), [ADR 0007](file:///home/michael/src/github.com/mnaatjes/ed-models/architecture/adr/0007_driving_facade_capability_boundaries_and_method_taxonomy.md), and [SDD-008](file:///home/michael/src/github.com/mnaatjes/ed-models/architecture/designs/SDD-008_driving_facade_capability_boundaries_implementation.md).

---

## 1. Instantiation & Factory

### `create_domain_facade() -> EliteDomainFacade`
Convenience factory function instantiating `EliteDomainFacade` with all pre-compiled in-memory static catalogs and use cases wired via the dependency injection composition root.

```python
from ed_models import create_domain_facade

facade = create_domain_facade()
```

---

## 2. Pillar 1: Static Catalog Lookups ($O(1)$)

All lookup methods operate against pre-compiled static in-memory dictionaries with zero network or filesystem I/O.

### Ship Hulls
* **`get_ship(symbol: str) -> ShipHull | None`**
  * **Parameters:** `symbol` (str) — Ship model slug or localized name (case-insensitive, e.g. `"anaconda"`, `"CobraMkIII"`).
  * **Returns:** [`ShipHull`](file:///home/michael/src/github.com/mnaatjes/ed-models/src/ed_models/core/domain/ships/hull.py) specification or `None` if uncataloged.
* **`list_ships() -> list[ShipHull]`**
  * **Returns:** List of all compiled ship hull entities.

### Outfitting Modules
* **`get_module_by_id(fdev_id: int) -> ShipModule | None`**
  * **Parameters:** `fdev_id` (int) — Canonical Frontier module ID (e.g. `128049382`).
  * **Returns:** [`ShipModule`](file:///home/michael/src/github.com/mnaatjes/ed-models/src/ed_models/core/domain/ships/module.py) or `None`.
* **`get_module_by_symbol(symbol: str) -> ShipModule | None`**
  * **Parameters:** `symbol` (str) — Canonical Frontier internal outfitting symbol (case-insensitive, e.g. `"int_hyperdrive_size5_class5"`).
  * **Returns:** [`ShipModule`](file:///home/michael/src/github.com/mnaatjes/ed-models/src/ed_models/core/domain/ships/module.py) or `None`.

### Commodities
* **`get_commodity_by_id(fdev_id: int) -> CommodityEntity | None`**
  * **Parameters:** `fdev_id` (int) — Canonical Frontier market ID.
  * **Returns:** [`CommodityEntity`](file:///home/michael/src/github.com/mnaatjes/ed-models/src/ed_models/core/domain/commodities/commodity.py) or `None`.
* **`get_commodity_by_symbol(symbol: str) -> CommodityEntity | None`**
  * **Parameters:** `symbol` (str) — Canonical trade commodity symbol (case-insensitive, e.g. `"grain"`).
  * **Returns:** [`CommodityEntity`](file:///home/michael/src/github.com/mnaatjes/ed-models/src/ed_models/core/domain/commodities/commodity.py) or `None`.

### Engineering
* **`get_blueprint(symbol: str) -> EngineeringBlueprint | None`**
  * **Parameters:** `symbol` (str) — Canonical blueprint symbol (case-insensitive, e.g. `"fsd_longrange"`).
  * **Returns:** [`EngineeringBlueprint`](file:///home/michael/src/github.com/mnaatjes/ed-models/src/ed_models/core/domain/engineering/blueprint.py) or `None`.
* **`get_experimental_effect(symbol: str) -> ExperimentalEffect | None`**
  * **Parameters:** `symbol` (str) — Canonical experimental effect symbol (e.g. `"special_fsd_massmanager"`).
  * **Returns:** [`ExperimentalEffect`](file:///home/michael/src/github.com/mnaatjes/ed-models/src/ed_models/core/domain/engineering/blueprint.py) or `None`.
* **`get_engineer(engineer_id: int) -> EngineerEntity | None`**
  * **Parameters:** `engineer_id` (int) — Frontier registered engineer ID (e.g. `300000` for Felicity Farseer).
  * **Returns:** [`EngineerEntity`](file:///home/michael/src/github.com/mnaatjes/ed-models/src/ed_models/core/domain/engineering/engineer.py) or `None`.
* **`list_engineers() -> list[EngineerEntity]`**
  * **Returns:** List of all registered Frontier engineers.

---

## 3. Pillar 2: Deterministic Token & Telemetry Normalization

* **`normalize_commodity(token: str) -> CommodityEntity | None`**
  * **Parameters:** `token` (str) — Raw localized token string from journal streams (e.g. `"$grain_name;"`, `"$modularterminals_name;"`).
  * **Returns:** Resolved [`CommodityEntity`](file:///home/michael/src/github.com/mnaatjes/ed-models/src/ed_models/core/domain/commodities/commodity.py) or `None`.
* **`parse_telemetry(*, flags: int, flags2: int = 0, pips: tuple[int, int, int] = (4, 4, 4), fuel_main: float = 0.0, fuel_reservoir: float = 0.0, cargo: int = 0, legal_state: str = "Clean") -> StatusTelemetry`**
  * **Parameters:**
    * `flags` (int): 32-bit integer bitfield from `Status.json`.
    * `flags2` (int): 20-bit integer bitfield (Odyssey on-foot telemetry).
    * `pips` (tuple[int, int, int]): Half-pips tuple `(sys, eng, wpn)` (0 to 8).
    * `fuel_main` (float): Main fuel tank level in metric tons.
    * `fuel_reservoir` (float): Reservoir fuel tank level in metric tons.
    * `cargo` (int): Current cargo tons onboard.
    * `legal_state` (str): Legal status string (e.g. `"Clean"`, `"Wanted"`).
  * **Returns:** Strongly typed [`StatusTelemetry`](file:///home/michael/src/github.com/mnaatjes/ed-models/src/ed_models/core/domain/status/telemetry.py) instance with decomposed bitfield properties (`is_docked`, `is_landed`, `is_supercruise`, `is_on_foot`, `is_in_srv`).
  * **Raises:** [`DomainValidationError`](file:///home/michael/src/github.com/mnaatjes/ed-models/src/ed_models/core/domain/exceptions.py) if numeric constraints are violated.
* **`parse_journal_event(payload: dict[str, Any]) -> JournalEvent`**
  * **Parameters:** `payload` (dict[str, Any]) — Raw parsed JSON dictionary from `Journal.*.log`.
  * **Returns:** Concrete typed subclass of [`JournalEvent`](file:///home/michael/src/github.com/mnaatjes/ed-models/src/ed_models/core/domain/events/base.py) (e.g. `FSDJump`, `Location`, `MarketBuy`). Falls back to base `JournalEvent` on uncataloged events to ensure contract elasticity.

---

## 4. Pillar 3: Pure Mathematical Interactors

* **`calculate_jump_range(params: JumpCalculationParameters) -> JumpCalculationResult`**
  * **Parameters:** [`JumpCalculationParameters`](file:///home/michael/src/github.com/mnaatjes/ed-models/src/ed_models/core/domain/flight/jump.py) specifying FSD optimal mass, rating fuel exponent, fuel multiplier, max fuel per jump, and ship mass configuration (unladen, cargo, fuel).
  * **Returns:** [`JumpCalculationResult`](file:///home/michael/src/github.com/mnaatjes/ed-models/src/ed_models/core/domain/flight/jump.py) with `current_jump_range_ly`, `unladen_jump_range_ly`, `max_jump_range_ly`, and `fuel_consumed`.
* **`format_trade_dangerous(records: list[TradeDangerousMarketRecord], timestamp_str: str) -> str`**
  * **Parameters:**
    * `records` (list[[`TradeDangerousMarketRecord`](file:///home/michael/src/github.com/mnaatjes/ed-models/src/ed_models/core/domain/interop/trade_dangerous.py)]): Market price records.
    * `timestamp_str` (str): Generation timestamp.
  * **Returns:** Fixed-width ASCII formatted Trade Dangerous market ledger string.
* **`serialize_coriolis(loadout: dict[str, Any]) -> str`**
  * **Parameters:** `loadout` (dict[str, Any]) — Ship outfitting loadout dictionary.
  * **Returns:** URL-safe base64 gzip-compressed hash string matching Coriolis.io specifications.
