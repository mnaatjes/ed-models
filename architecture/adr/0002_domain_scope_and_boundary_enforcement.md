---
title: "ADR 0002: Domain Scope and Boundary Enforcement Mechanics"
tags: ["adr", "ed-models", "boundaries", "hexagonal-architecture", "quality-gates", "dataclasses", "typing"]
created_at: "2026-11-01"
last_updated_at: "2026-11-01"
---

# ADR 0002: Domain Scope and Boundary Enforcement Mechanics

* **Status:** Accepted
* **Date:** 2026-11-01
* **Deciders:** Michael Naatjes, Antigravity Agent
* **Consulted:** [ADR 0001](file:///home/michael/src/github.com/mnaatjes/ed-models/architecture/adr/0001_ed_models_core_game_logic_and_catalog_architecture.md), [Master Risk Register](file:///home/michael/src/github.com/mnaatjes/ed-models/architecture/risk/risk-list.md), [Hexagonal Invariants Directives](file:///home/michael/.gemini/rules/hexagonal_invariants.md)

---

## 1. Context and Problem Statement

[ADR 0001](file:///home/michael/src/github.com/mnaatjes/ed-models/architecture/adr/0001_ed_models_core_game_logic_and_catalog_architecture.md) established `ed-models` as a pure, zero-I/O Hexagonal domain library with pre-compiled static catalogs and a unified driving facade. However, moving from architectural vision to concrete codification—specifically when extracting and transforming 269 event and domain entities from reference codebases like `kayahr/ed-journal`—introduces critical risks documented in the [Master Risk Register](file:///home/michael/src/github.com/mnaatjes/ed-models/architecture/risk/risk-list.md):

1. **RISK-01 & RISK-02:** Deserialization crashes when using rigid enums on expanding game taxonomies, or unhandled token drift during game updates.
2. **RISK-03:** Python dataclass inheritance collisions (`TypeError: non-default argument follows default argument`) across base and derived event hierarchies.
3. **RISK-04:** Severe memory bloat when streaming multi-gigabyte journal archives without memory-optimized layouts.
4. **RISK-05:** Accidental leakage of network clients, filesystem calls, or schema validation engines into pure domain layers.

We need explicit, deterministic architectural boundary rules and automated enforcement mechanisms (via Pytest, Import Linter, Pre-Commit, and CI) governing how domain entities, types, events, and snapshots are structured and hydrated.

---

## 2. Decision Drivers

* **Zero-I/O Domain Purity:** Standard library only; no external serialization or HTTP frameworks inside `src/ed_models/core/`.
* **High-Throughput Stream Performance:** Low memory footprint and instant object allocation across 100k+ event streams.
* **Resilience to Game Patches:** Graceful degradation on uncataloged game items rather than runtime crashes.
* **Automated Enforcement:** Continuous validation through linters, unit tests, and CI pipelines to prevent human error.

---

## 3. Considered Options

* **Option 1: Ad-Hoc Dataclass Authoring with Pydantic.** Use Pydantic v2 models for parsing, alias mapping, and validation.
* **Option 2: Unenforced Standard Dataclasses with Loose Types.** Standard `@dataclass` without inheritance controls or boundary linting.
* **Option 3: Codified Pure Dataclasses with Multi-Layered Automated Boundary Enforcement (Selected).** Pure Python standard library dataclasses adhering strictly to deterministic type mapping, mandatory inheritance qualifiers, and verified via `import-linter`, `pytest-archon`, and CI gates.

---

## 4. Decision Outcome

**Chosen Option:** **Option 3: Codified Pure Dataclasses with Multi-Layered Automated Boundary Enforcement.**

### 4.1 Internal Domain Partitioning & Placement Boundaries

1. **`core/domain/types/` vs. `core/domain/events/` Isolation (`HEXA-TRUTH-06`):**
   * Shared enums (`StarType`, `BodyType`, `StationService`, `PadSize`, `Allegiance`, `LegalState`) MUST reside strictly in `src/ed_models/core/domain/types/`.
   * Under no circumstances may an enum be declared inside an event subpackage.
   * **Dependency Direction:** `core/domain/events/` MAY import from `core/domain/types/`, but `core/domain/types/` MUST have **ZERO** imports from `events/`.
2. **Snapshot Decoupling Strategy:**
   * Streaming trigger events in `Journal.*.log` (e.g. `Market` with just ID, station, system) are modeled as discrete events in `core/domain/events/station.py` (`MarketEvent`).
   * Companion snapshot files (`Market.json`, `Outfitting.json`, `Shipyard.json`, `NavRoute.json`, `Backpack.json`) represent deep starport state and are modeled as distinct Snapshot models (e.g. `MarketSnapshot`, `OutfittingSnapshot`, `NavRouteSnapshot`) containing complete item inventories.
3. **Entity Composition over Ephemeral Structs:**
   * Permanent game entities (`ShipHull`, `ShipModule`, `CommodityEntity`, `Coordinates3D`) reside in their dedicated domain packages (`ships/`, `commodities/`, `spatial/`).
   * Event dataclasses in `events/` must reference or compose these canonical domain models rather than inventing transient duplicate structs.

### 4.2 Contract Elasticity Boundary (Open vs. Closed Taxonomies)

To eliminate deserialization crashes caused by upstream Frontier game updates (`RISK-02`):
1. **The Closed Boundary ($\le 50$ items):**
   * Frontier-defined discrete constants with fixed semantics (`Allegiance`, `StarType`, `BodyType`, `PadSize`) are permitted as strongly typed `enum.StrEnum` members.
2. **The Open Boundary ($> 100$ items):**
   * Expanding game taxonomies (Commodities, Engineering Blueprints, Suit Consumables) MUST NEVER be modeled as closed Python enums. They are bounded as canonical string symbols (`str`) backed by $O(1)$ catalog lookup dictionaries.
   * If a journal event emits an uncataloged commodity or blueprint, the boundary parser hydrates the record with a fallback token rather than throwing a `ValueError` crash.

### 4.3 Polymorphic Event Hierarchy & Inheritance Boundary

To guarantee safe object instantiation without default-argument parameter ordering collisions (`RISK-03`):
1. **Mandatory Keyword-Only Boundary:**
   * Base class `JournalEvent(timestamp: datetime, event: str)` and all derived event subclasses MUST declare `@dataclass(kw_only=True)`.
   * Non-keyword positional instantiation across the event boundary is strictly prohibited.
2. **Memory Overhead Invariants (`RISK-04`):**
   * All event models and domain entities MUST declare `@dataclass(slots=True)` to strip per-instance `__dict__` overhead during massive log stream processing.
   * Pure value objects (`Coordinates3D`) MUST declare `@dataclass(frozen=True, slots=True)` enforcing mathematical immutability (`HEXA-TRUTH-10`).

### 4.4 Library Storage vs. External Fleet Scope Boundary

In accordance with ADR 0001 Section 4.4, `ed-models` enforces an absolute storage scope boundary:
1. **Strictly Permitted Inside `ed-models`:**
   * Pure entity blueprints, mathematical formulas (jump range, distance), and static metadata catalogs (~48 ship hulls, ~800 module specs, ~450 commodity definitions) packaged directly as in-memory code tables ($< 2$ MB total distribution).
2. **Strictly Excluded & Delegated to Fleet Services:**
   * The 200M star system galactic database $\rightarrow$ delegated to `ed-router` and Spansh.
   * Live starport commodity prices and stock states $\rightarrow$ delegated to `ed-connector` (local SQLite/Redis cache) and `ed-schema` (EDDN).
   * Host log tailing, directory watching, and OS file handles $\rightarrow$ delegated to `ed-telemetry`.
   * Network requests, HTTP transports, and CAPI OAuth $\rightarrow$ delegated to `ed-transport`.

---

## 5. Automated Boundary Enforcement Architecture

To guarantee these rules are never violated, enforcement is distributed across four automated quality layers:

```mermaid
flowchart TD
    Dev["Developer / Agent Code Change"] --> PreCommit[".pre-commit-config.yaml\n(Ruff Lint, Format, Toml/Yaml check)"]
    PreCommit --> PytestLocal["Pytest Architecture Suite\n(test_boundaries.py)"]
    PytestLocal --> ImportLinter[".importlinter\n(Layer & Forbidden Contracts)"]
    ImportLinter --> CIPipeline[".github/workflows/ci.yml\n(Full Matrix Verification)"]
    CIPipeline --> Merge["Main Branch Protected Merge"]
```

### 5.1 Enforcement Mechanics Matrix

| Layer | Tool / Mechanism | Governed Boundary / Invariant | Failure Action |
| :--- | :--- | :--- | :--- |
| **Layer 1: Pre-Commit** | `ruff`, `end-of-file-fixer`, `trailing-whitespace` | Code hygiene, type annotations (`list[T]` vs `List[T]`), import sorting | Block local commit |
| **Layer 2: Architecture Pytest** | `pytest tests/architecture/test_boundaries.py` | `HEXA-TRUTH-01` (Core Domain Isolation), `HEXA-TRUTH-03` (Port Protocol Integrity), `HEXA-TRUTH-07` (Exception Sovereignty) | Test suite failure (`pytest` non-zero exit) |
| **Layer 3: Structural Linter** | `import-linter` (`.importlinter`) | Dependency layering (`bootstrap` $\rightarrow$ `adapters` $\rightarrow$ `use_cases` $\rightarrow$ `ports` $\rightarrow$ `domain`) and absolute isolation of `core/domain/` | Build failure (`lint-imports` non-zero exit) |
| **Layer 4: CI Quality Gate** | `.github/workflows/ci.yml` | Full regression: `pytest`, `mypy --strict`, `ruff check`, `import-linter` across Python versions | Block PR merge |

### 5.2 Specific `.importlinter` Contract Additions

The `.importlinter` configuration enforces:
1. **Core Domain Isolation:** `src/ed_models/core/domain/` may not import `core/ports/`, `core/use_cases/`, `adapters/`, or `bootstrap/`.
2. **Types-to-Events Directionality:** `src/ed_models/core/domain/types/` may not import `src/ed_models/core/domain/events/`.
3. **Zero I/O Bypass:** No imports of `httpx`, `requests`, `urllib`, `socket`, `sqlite3`, or `ed_telemetry` anywhere inside `core/`.

---

## 6. Pros and Cons of the Selected Option

### Pros
* **Bulletproof Determinism:** Eliminates runtime crashes from unknown items, dataclass inheritance ordering, or missing localized fields.
* **Optimal Performance:** `slots=True` ensures high throughput and minimal RAM footprint when streaming historical player journals.
* **Continuous Machine Enforcement:** Invariants are caught locally before code reaches the remote repository.
* **Full Compliance with Fleet Architecture:** Seamless integration with `ed-schema` (validation) and `ed-telemetry` (ingestion).

### Cons
* **Requires Explicit Mapping:** Deserializer must maintain a field-mapping table between Frontier `PascalCase` and Python `snake_case`.

---

## 7. Implementation Roadmap

1. **Verify Boundary Suite:** Ensure `tests/architecture/test_boundaries.py` asserts `types` vs `events` isolation and `kw_only=True` constraints.
2. **Implement SDD-003:** Author extraction script converting `kayahr/ed-journal` TypeScript models according to this ADR's translation matrix.
3. **Execute Static Catalog Compilation:** Compile static catalogs into `adapters/driven/static_catalogs/` adhering to open-set symbol rules.
