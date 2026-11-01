---
title: "ADR 0003: Event Model Extraction Pipeline and Static Catalog Compilation"
tags: ["adr", "ed-models", "codegen", "extraction", "catalogs", "ed-journal"]
created_at: "2026-11-01"
last_updated_at: "2026-11-01"
---

# ADR 0003: Event Model Extraction Pipeline and Static Catalog Compilation

* **Status:** Accepted
* **Date:** 2026-11-01
* **Deciders:** Michael Naatjes, Antigravity Agent
* **Consulted:** [ADR 0001](file:///home/michael/src/github.com/mnaatjes/ed-models/architecture/adr/0001_ed_models_core_game_logic_and_catalog_architecture.md), [ADR 0002](file:///home/michael/src/github.com/mnaatjes/ed-models/architecture/adr/0002_domain_scope_and_boundary_enforcement.md), [Master Risk Register](file:///home/michael/src/github.com/mnaatjes/ed-models/architecture/risk/risk-list.md)

---

## 1. Context and Problem Statement

To fulfill the requirements of ADR 0001 and ADR 0002, `ed-models` must codify:
1. **~150+ concrete Journal, Snapshot, and Status event dataclasses** partitioned across Frontier Developments' 12 official specification chapters.
2. **~800 outfitting modules, 48 ship hull profiles, and ~450 commodity definitions** as static, pre-compiled in-memory lookup catalogs.

The open-source repository `kayahr/ed-journal` (`/home/michael/src/github.com/kayahr/ed-journal`) contains 269 strongly typed TypeScript event and type definitions. Manually authoring and maintaining these models in Python is highly labor-intensive, error-prone, and unsustainable across future Elite Dangerous updates. Conversely, parsing raw JSON/CSV datafiles at runtime violates the zero-disk-I/O and sub-10ms bootstrap latency requirements.

We need an automated, reproducible extraction and compilation architecture.

---

## 2. Decision Drivers

* **Zero-Touch Runtime Latency:** Zero disk parsing or JSON unmarshaling at library initialization ($O(1)$ lookups via pre-compiled Python dictionaries).
* **Extraction Reproducibility:** Automated scripts capable of re-running against newer versions of `kayahr/ed-journal` or community datasets.
* **Strict Conformance to ADR 0002:** Mandatory `@dataclass(slots=True, kw_only=True)`, closed-set `StrEnum` mapping, and pure core domain isolation (`HEXA-TRUTH-01`).
* **Test Traceability:** Empirical round-trip verification against actual historical game logs.

---

## 3. Considered Options

* **Option 1: Manual Transpilation.** Manually rewrite all 269 TypeScript files into Python dataclasses.
* **Option 2: Runtime JSON Datafile Bundling.** Bundle raw JSON datafiles inside the Python wheel and load them into memory upon package import using `json.loads()`.
* **Option 3: Automated Build-Time AST/Regex Extraction & Code Generation (Selected).** Author build-time generator scripts in `scripts/` that translate `kayahr/ed-journal` TypeScript AST/tokens into Python dataclasses, and compile CSV/JSON data into frozen Python dictionaries in `adapters/driven/static_catalogs/`.

---

## 4. Decision Outcome

**Chosen Option:** **Option 3: Automated Build-Time AST/Regex Extraction & Code Generation.**

### 4.1 Event & Type Extraction Pipeline (`scripts/extract_ed_journal_models.py`)

A build-time translation utility reads `/home/michael/src/github.com/kayahr/ed-journal/src/main/events/` and generates clean Python source code adhering to ADR 0002:

```mermaid
flowchart TD
    TS["kayahr/ed-journal/src/main/events/ (269 .ts files)"] --> Extractor["scripts/extract_ed_journal_models.py"]

    Extractor -->|Types & Enums (types/*.ts)| DomainTypes["src/ed_models/core/domain/types/\n(bodies.py, economy.py, allegiance.py)"]
    Extractor -->|Telemetry Bitfields (other/Status.ts)| DomainStatus["src/ed_models/core/domain/status/\n(status.py: StatusFlags, StatusFlags2)"]
    Extractor -->|Journal Events (12 Chapter Dirs)| DomainEvents["src/ed_models/core/domain/events/\n(startup.py, travel.py, combat.py, ...)"]
    Extractor -->|Snapshot Models (Market, Outfitting, etc.)| DomainSnapshots["src/ed_models/core/domain/events/\n(MarketSnapshot, NavRouteSnapshot, ...)"]
```

#### Extraction Routing Rules:
1. **`events/types/*.ts` $\rightarrow$ `core/domain/types/`:**
   * String unions (`type StationService = ...`) map to `class StationService(StrEnum):`.
   * Enums are partitioned logically: `bodies.py` (`StarType`, `PlanetClass`), `economy.py` (`StationType`, `StationService`), `allegiance.py` (`PowerState`).
2. **`events/other/Status.ts` $\rightarrow$ `core/domain/status/`:**
   * `const Flag` and `const Flag2` bitmasks map to `class StatusFlags(IntFlag):` and `class StatusFlags2(IntFlag):`.
   * The status payload maps to `class ShipStatus:` with slotted boolean properties.
3. **Chapters 2–13 $\rightarrow$ `core/domain/events/<chapter>.py`:**
   * TypeScript interfaces (`interface FSDJump extends JournalEvent<"FSDJump">`) map to `@dataclass(slots=True, kw_only=True) class FsdJumpEvent(JournalEvent):`.
   * PascalCase fields convert to snake_case attributes with default `None` for optional fields.
   * `_Localised` companion keys map to `name_localised: str | None = None`.

### 4.2 Static Catalog Compilation Pipeline (`scripts/compile_static_catalogs.py`)

Community reference datafiles are compiled directly into static Python source modules in `src/ed_models/adapters/driven/static_catalogs/`:

1. **Ships (`ships.json` $\rightarrow$ `static_catalogs/ships.py`):**
   * Generates `SHIP_HULL_CATALOG: dict[str, ShipHull]` containing all 48 flyable ships, base mass, pad size, and default slot layouts.
2. **Modules (`modules.json` $\rightarrow$ `static_catalogs/modules.py`):**
   * Generates `MODULE_CATALOG: dict[int, ShipModule]` indexed by FDev module ID containing class, rating, mass, and power draw.
3. **Commodities (`commodities.csv` / `FDevIDs` $\rightarrow$ `static_catalogs/commodities.py`):**
   * Generates `COMMODITY_CATALOG: dict[str, CommodityEntity]` indexed by canonical symbol and ID.

### 4.3 Verification & Quality Assurance Strategy

1. **Zero-Syntax Failure Gate:** All generated files must pass `.venv/bin/ruff check .` and `.venv/bin/mypy src/ tests/`.
2. **Boundary Gate:** Generated code must satisfy `tests/architecture/test_boundaries.py` ensuring `events/` never cross-import into `types/` or violate layer boundaries.
3. **Ingestion Fidelity Test:** Execute test against sample logs in `kayahr/ed-journal/src/test/data/` verifying that 100% of journal events hydrate into concrete dataclasses without falling back to raw generic dictionaries.

---

## 5. Pros and Cons of the Selected Option

### Pros
* **Full Automation:** Re-generating the domain models after an Elite Dangerous update takes seconds.
* **Guaranteed Determinism:** Code generation script enforces ADR 0002 rules uniformly across all 269 models.
* **Instantaneous Runtime Loading:** Zero runtime file parsing or JSON decode delays; catalogs load into memory at CPython bytecode import speed.

### Cons
* **Initial Tooling Overhead:** Requires building and validating the extraction regex/AST parser script.
