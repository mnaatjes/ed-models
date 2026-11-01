---
title: "ADR 0003: TypeScript Model Extraction and Domain Transformation Pipeline"
tags: ["architecture", "adr", "extraction", "transformation", "ed-journal", "ast", "domain-models"]
created_at: "2026-11-01"
last_updated_at: "2026-11-01"
---

# ADR 0003: TypeScript Model Extraction and Domain Transformation Pipeline

## 1. Context and Problem Statement

`ed-models` serves as the pure, offline domain logic and static data model authority for the *Elite Dangerous* software fleet (governed by [ADR 0001](file:///home/michael/src/github.com/mnaatjes/ed-models/architecture/adr/0001_ed_models_core_game_logic_and_catalog_architecture.md) and [ADR 0002](file:///home/michael/src/github.com/mnaatjes/ed-models/architecture/adr/0002_domain_scope_and_boundary_enforcement.md)).

Frontier Developments' Player Journal specification defines approximately 269 discrete event payloads across 12 functional categories, alongside companion JSON snapshots (`Market.json`, `Outfitting.json`, `Shipyard.json`, `NavRoute.json`, `FCMaterials.json`). Manually hand-authoring and maintaining these models in Python is inefficient, prone to schema drift, and diverges from established community codifications.

The repository `kayahr/ed-journal` (`/home/michael/src/github.com/kayahr/ed-journal`) maintains an exhaustive, typed codification of all 269 journal events and 11 universal type enumerations in TypeScript interfaces, along with historical test payloads across journal revisions v1–v37 (as documented in [Note 0012](file:///home/michael/src/github.com/mnaatjes/ed-integration-smoke/architecture/notes/0012_harvested_game_events_and_codification_repositories.md)).

How should `ed-models` ingest, transform, and structure models extracted from `kayahr/ed-journal` into Python domain models while strictly adhering to hexagonal boundary invariants, zero I/O constraints, and type-safety gates?

---

## 2. Decision Drivers

* **Boundary Invariant Compliance:** Generated Python code must strictly conform to [ADR 0002](file:///home/michael/src/github.com/mnaatjes/ed-models/architecture/adr/0002_domain_scope_and_boundary_enforcement.md) (`HEXA-TRUTH-01` through `HEXA-TRUTH-17`, `RISK-01` through `RISK-05`), including zero I/O imports, `@dataclass(slots=True, kw_only=True)`, and frozen value objects.
* **Structural Purity & Subdomain Partitioning:** Universal primitives must live in `src/ed_models/core/domain/types/` and must never import events (`HEXA-TRUTH-06`). Journal events must map 1:1 to their functional categories (`startup`, `travel`, `combat`, `exploration`, `trade`, `station`, `powerplay`, `squadrons`, `carrier`, `odyssey`, `other`).
* **Companion Snapshot Specialization:** Standalone JSON snapshot files (`ExtendedMarket`, `ExtendedShipyard`, etc.) must be modeled as pure domain value objects or event extensions, decoupled from filesystem monitors or transport clients.
* **Deterministic Code Generation Tooling:** The translation pipeline must be offline, deterministic, automated, and maintainable without introducing third-party runtime dependencies into `ed-models`.
* **Zero I/O at Runtime:** The compilation/extraction process must execute strictly as an offline development/build tool (or external sandbox script); no TypeScript parser, Node.js runtime, or disk-scraping mechanism may exist within the production `ed-models` runtime package.

---

## 3. Considered Options

* **Option 1: Manual Python Translation.** Hand-transcribing all 269 TypeScript interfaces into Python dataclasses.
* **Option 2: Runtime JSON Schema Validation (`jsonschema` / `pydantic`).** Ingesting raw JSON and validating dynamically at runtime using external validation frameworks.
* **Option 3: Deterministic AST/Regex Code Generator Tooling.** Developing a specialized, offline code extraction and transformation script that reads `kayahr/ed-journal/src/main/events/`, parses TypeScript interfaces, maps types to idiomatic Python 3.12+ constructs, and emits pure dataclasses directly into `src/ed_models/core/domain/`.

---

## 4. Decision Outcome

**Chosen Option:** **Option 3: Deterministic AST/Regex Code Generator Tooling.**

We establish a dedicated offline extraction pipeline to harvest TypeScript models from `kayahr/ed-journal` and synthesize them into pure Python domain models.

### 4.1 Transformation & Mapping Specifications

#### 4.1.1 Primitive & Composite Type Mappings

| TypeScript Construct (`ed-journal`) | Python Domain Construct (`ed-models`) | Architectural Rules |
| :--- | :--- | :--- |
| `string` | `str` | Built-in immutable primitive |
| `number` (integer semantics: ID, Count) | `int` | Built-in primitive |
| `number` (floating-point: Dist, Fuel) | `float` | Built-in primitive |
| `boolean` | `bool` | Built-in primitive |
| `[number, number, number]` (`StarPos`) | `Coordinates3D` | Frozen value object with `(x: float, y: float, z: float)` |
| `Array<T>` / `T[]` | `list[T]` or `tuple[T, ...]` | Immutable tuples for value objects; typed lists for event payloads |
| `Record<string, T>` | `dict[str, T]` | Built-in generic mapping |
| `Union String Literals` (`"A" \| "B"`) | `StrEnum` | Discrete string enum under `core/domain/types/` |
| `JournalEvent<"Name">` interface | `@dataclass(slots=True, kw_only=True)` | Extends `JournalEvent` base class in `core/domain/events/base.py` |
| `Nested anonymous interfaces` | Standalone nested `@dataclass` | Extracted and hoisted as explicit child value objects |
| Optional properties (`field?: T`) | `field: T \| None = None` | Explicit union with `None` and default `None` |

#### 4.1.2 Directory and Namespace Destination Topology

```text
kayahr/ed-journal/src/main/events/
├── types/
│   ├── BodyType.ts           ──▶ src/ed_models/core/domain/types/body_type.py (StrEnum)
│   ├── StarType.ts           ──▶ src/ed_models/core/domain/types/star_type.py (StrEnum)
│   ├── StationService.ts     ──▶ src/ed_models/core/domain/types/station_service.py (StrEnum)
│   └── ...                   ──▶ src/ed_models/core/domain/types/*.py
├── travel/
│   ├── FSDJump.ts            ──▶ src/ed_models/core/domain/events/travel/fsd_jump.py
│   ├── Location.ts           ──▶ src/ed_models/core/domain/events/travel/location.py
│   └── ...
├── station/
│   ├── Market.ts             ──▶ src/ed_models/core/domain/events/station/market.py
│   └── ...
└── [category]/               ──▶ src/ed_models/core/domain/events/[category]/*.py
```

#### 4.1.3 Companion Snapshot Specialization

Companion snapshots (`Market.json`, `Outfitting.json`, `Shipyard.json`, `NavRoute.json`, `FCMaterials.json`) represent detailed state dumps triggered concurrently with an event.

- In `kayahr/ed-journal`, these are modeled as `ExtendedMarket`, `ExtendedShipyard`, etc.
- In `ed-models`, these shall be codifying under `src/ed_models/core/domain/events/[category]/` as dedicated snapshot domain dataclasses (e.g., `MarketSnapshot`, `OutfittingSnapshot`, `NavRouteSnapshot`) inheriting from or composing the base trigger event.
- The hydration and serialization of these snapshots are pure in-memory operations conforming to `HEXA-TRUTH-01` (zero file reading/watching inside `ed-models`).

### 4.2 Pipeline Architecture & Operational Mechanics

1. **Extraction Pipeline Location:**
   - The extraction generator script resides in development tooling (`scripts/extract_models.py` or within `ed-integration-smoke/scripts/`) and is **never packaged** into the production distribution wheel of `ed-models`.
2. **Deterministic Output:**
   - Running the extraction script outputs source code into `src/ed_models/core/domain/` with standard file headers, clean imports, and explicit type hints.
3. **Automated Enforcement Verification:**
   - Every generated file is immediately subjected to Downstream Quality Gates:
     - `ruff check . --fix` and `ruff format .`
     - `.venv/bin/mypy src/ tests/`
     - `pytest tests/architecture/test_boundaries.py` (verifying `slots=True`, `kw_only=True`, zero I/O imports, frozen value objects)
     - `lint-imports` (verifying boundary isolation across domain subpackages)

---

## 5. Consequences

### Positive

* **Rapid & Exhaustive Domain Codification:** Instantly brings 269 strongly typed events into `ed-models` without human transcription errors.
* **Community Alignment:** Retains exact field names, casing, and semantic hierarchies harmonized with `kayahr/ed-journal` and Frontier specifications.
* **Architectural Invariant Guarantee:** Generated code is verified by Gate 1–Gate 4 boundary gates before being merged.
* **Zero Runtime Overhead:** No external runtime dependencies (`pydantic`, `jsonschema`) or I/O libraries are introduced into `ed-models`.

### Negative & Mitigations

* **TypeScript AST Parsing Nuances:**
  * *Risk:* Complex nested interfaces or intersection types (`&`) in TypeScript may challenge naive regex translators.
  * *Mitigation:* Employ a robust parsing strategy (using a TypeScript AST parser via Node.js CLI script emitting intermediate JSON AST, or structured regex/parser in Python) that outputs canonical AST nodes.
* **Frontier Specification Errata:**
  * *Risk:* Occasional journal payloads from Frontier contain undocumented fields or variable types (e.g. integer or string IDs).
  * *Mitigation:* Fields with dynamic types are mapped to `Any` or union types (`int | str`), and events allow optional keyword initialization with `None` defaults for non-universal keys.

---

## 6. References

* [ADR 0001: ed-models Pure Domain Architecture, Catalog Codification, and Driving Facade](file:///home/michael/src/github.com/mnaatjes/ed-models/architecture/adr/0001_ed_models_core_game_logic_and_catalog_architecture.md)
* [ADR 0002: Domain Scope and Boundary Enforcement Mechanics](file:///home/michael/src/github.com/mnaatjes/ed-models/architecture/adr/0002_domain_scope_and_boundary_enforcement.md)
* [SDD-003: Domain Scope and Boundary Enforcement Implementation](file:///home/michael/src/github.com/mnaatjes/ed-models/architecture/designs/SDD-003_domain_scope_and_boundary_enforcement_implementation.md)
* [Note 0012: Harvested Game Event Repositories & Codification Authorities](file:///home/michael/src/github.com/mnaatjes/ed-integration-smoke/architecture/notes/0012_harvested_game_events_and_codification_repositories.md)
* Repository `kayahr/ed-journal`: `/home/michael/src/github.com/kayahr/ed-journal`
