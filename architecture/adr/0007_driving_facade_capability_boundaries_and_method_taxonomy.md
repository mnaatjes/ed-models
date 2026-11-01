---
title: "ADR 0007: Driving Facade Capability Boundaries and Method Taxonomy"
tags: ["architecture", "adr", "facade", "driving-adapter", "boundaries", "hexagonal-architecture"]
created_at: "2026-11-01"
last_updated_at: "2026-11-01"
---

# ADR 0007: Driving Facade Capability Boundaries and Method Taxonomy

## 1. Context and Problem Statement

`ed-models` serves as the offline domain model and computational authority for the *Elite Dangerous* software fleet (governed by [ADR 0001](file:///home/michael/src/github.com/mnaatjes/ed-models/architecture/adr/0001_ed_models_core_game_logic_and_catalog_architecture.md) and [ADR 0002](file:///home/michael/src/github.com/mnaatjes/ed-models/architecture/adr/0002_domain_scope_and_boundary_enforcement.md)).

As a pure domain library, `ed-models` exposes a driving facade adapter (`EliteDomainFacade`) to consuming packages (`ed-telemetry`, `ed-connector`, `ed-router`, `ed-schema`). However, without formal boundary governance on what methods and behaviors the facade may expose, there is significant risk of:
1. **Scope Creep / Boundary Leakage:** Inadvertently introducing operations that belong in consuming applications, such as dynamic station market caching, route finding algorithms, log file watching, or network queries.
2. **State Pollution:** Storing mutable player session state (e.g. current ship inventory history, active mission tracking) inside an offline reference library.
3. **Ambiguous API Contracts:** Unclear separation between what operations the domain library owns (universal game rules and static catalogs) versus what consuming services must perform.

What operations, methods, and responsibilities are permitted on the user-facing driving facade of `ed-models`, and how are these boundaries machine-enforced?

---

## 2. Decision Drivers

* **Zero-I/O Domain Purity (`HEXA-TRUTH-01`):** The facade must contain zero filesystem, network, or external socket operations.
* **Separation of Universal Rules vs. Dynamic State:** Universal game constants (ship masses, engineering blueprints, FSD formulas) belong in `ed-models`. Contextual runtime state (player inventory, current market stock, journal file cursors) belongs in consuming packages.
* **Predictable Operational Taxonomy:** Every method on the facade must fall into one of three well-defined, deterministic functional classifications.
* **Automated Machine Enforcement:** Invariants must be validated via AST analysis in `tests/architecture/test_boundaries.py` to prevent accidental capability creep.

---

## 3. Considered Options

* **Option 1: Minimal Data-Only Package (No Facade).** Eliminate the facade entirely and force consuming packages to import internal catalogs and use cases directly.
* **Option 2: Active Service Facade.** Allow the facade to manage session history, execute spatial routing algorithms, and provide helper methods that interact with local databases.
* **Option 3: Strict Three-Pillar Stateless Driving Facade (Selected).** Expose a unified facade adapter (`EliteDomainFacade`) strictly constrained to three permitted functional pillars:
  1. *Static Catalog Lookups ($O(1)$ in-memory)*
  2. *Deterministic Token & Event Normalization*
  3. *Pure Mathematical Interactors*

---

## 4. Decision Outcome

**Chosen Option:** **Option 3: Strict Three-Pillar Stateless Driving Facade.**

### 4.1 The Three Permitted Operation Pillars

The driving facade (`EliteDomainFacade`) may expose **only** methods that strictly fall into the following three classifications:

| Pillar | Method Prefix / Pattern | Permitted Signatures & Behaviors | Examples |
| :--- | :--- | :--- | :--- |
| **1. Static Catalog Lookups** | `get_*`, `list_*` | Accepts discrete primitive keys (`str`, `int`). Queries pre-compiled in-memory catalogs in $O(1)$ time. Returns frozen domain entities or `None`. Zero side-effects. | `get_ship(symbol: str) -> ShipHull \| None`<br>`get_module(fdev_id: int) -> ShipModule \| None`<br>`get_commodity(symbol: str) -> CommodityEntity \| None`<br>`get_blueprint(symbol: str) -> EngineeringBlueprint \| None`<br>`list_engineers() -> tuple[EngineerEntity, ...]` |
| **2. Token & Event Normalization** | `normalize_*`, `parse_*` | Accepts raw Frontier tokens (`$modularterminals_name;`) or raw telemetry bitfields/dicts. Transforms input into canonical domain models. Pure and deterministic. | `normalize_commodity(token: str) -> CommodityEntity \| None`<br>`parse_telemetry(flags: int, flags2: int, ...) -> StatusTelemetry` |
| **3. Pure Mathematical Interactors** | `calculate_*`, `format_*`, `serialize_*` | Stateless calculators executing official Frontier formulas or in-memory serialization. Operates strictly on value objects; produces pure outputs. | `calculate_jump_range(params: JumpCalculationParameters) -> JumpCalculationResult`<br>`format_trade_dangerous(records: list[TradeDangerousMarketRecord], ts: str) -> str`<br>`serialize_coriolis(loadout: dict[str, object]) -> str` |

### 4.2 Prohibited Facade Behaviors

The driving facade is **strictly forbidden** from:
1. **Accepting I/O Arguments:** Never accept file paths (`Path`, `str` representing a file), file descriptors, streams, sockets, HTTP request objects, or database connections.
2. **Mutating Internal State:** The facade must be completely stateless after dependency injection in `__init__`.
3. **Galaxy-Scale Querying:** No graph search algorithms, spatial A* pathfinding across 200M systems, or SQLite database querying (owned by `ed-router`).
4. **Log Streaming / Polling:** No file tailing, journal watching, or event listener loops (owned by `ed-telemetry`).

---

## 5. Architectural Machine Enforcement

To guarantee compliance, an automated AST boundary test (`test_facade_driving_adapter_method_boundaries`) in `tests/architecture/test_boundaries.py` audits `EliteDomainFacade`:
1. **Method Name Verification:** All public methods must begin with one of the approved prefixes: `get_`, `list_`, `normalize_`, `parse_`, `calculate_`, `format_`, `serialize_`.
2. **Parameter Whitelist:** Parameters must be primitive types (`str`, `int`, `float`, `bool`) or pure domain value objects / DTOs.
3. **Return Type Whitelist:** Returns must be typed domain entities, value objects, primitives, or `None`. Raw untyped `Any`, `dict`, or stream objects are rejected.

---

## 6. Consequences

### Positive
* **Crystal-Clear Package Boundaries:** Consuming packages know exactly what `ed-models` provides (constants, lookups, formulas) versus what they must implement.
* **Zero Runtime Overhead:** Lookups and calculations remain entirely in-memory and execution-efficient.
* **Continuous Machine Enforcement:** Any developer or agent attempting to add unauthorized methods or I/O calls to the facade will immediately fail the architectural test suite.

### Negative / Trade-offs
* Consuming packages must implement their own state tracking (e.g., maintaining the player's active ship loadout across multiple events).
