---
title: "ADR 0005: Harvesting and Codification of Remaining Game Domains"
tags: ["architecture", "adr", "harvesting", "status-telemetry", "engineering", "celestial-bodies", "odyssey", "flight-mechanics"]
created_at: "2026-11-01"
last_updated_at: "2026-11-01"
---

# ADR 0005: Harvesting and Codification of Remaining Game Domains

## 1. Context and Problem Statement

Following the successful codification of the streaming journal event plane ([ADR 0003](file:///home/michael/src/github.com/mnaatjes/ed-models/architecture/adr/0003_typescript_model_extraction_and_transformation_pipeline.md)) and static ship/module/commodity catalogs ([ADR 0004](file:///home/michael/src/github.com/mnaatjes/ed-models/architecture/adr/0004_static_catalogs_and_domain_entity_codification.md)), five critical domain subsystems remain uncodified or fragmented in `ed-models`:

1. **Cockpit Telemetry Flags & Bitmasks:** The continuous cockpit state broadcast (`Status.json`) exposes a 32-bit `Flags` bitfield and a 20-bit `Flags2` bitfield representing critical flight, planetary, and vehicle states (e.g., Docked, Landed, InSRV, Supercruise, FSD Jump, Night Vision, Glide Mode).
2. **Engineering Blueprints & Experimental Effects:** Modification grades 1–5, ingredient material recipes, attribute modifiers, and experimental weapon/module effects.
3. **Celestial Bodies & Planetary Physics:** Star classifications, planetary surface types, atmospheric compositions, ring systems, orbital parameters, and surface gravity calculation mechanics.
4. **Odyssey On-Foot Assets & Loadouts:** Suits (Flight, Artemis, Maverick, Dominator), on-foot weaponry, slot capacities, and engineering modifications.
5. **Flight Mechanics & Jump Physics:** Exact Frame Shift Drive (FSD) jump range formulas, fuel consumption curves, supercruise acceleration limits, and cargo mass penalty equations.

Without these domains codified:
- `ed-telemetry` cannot decompose continuous cockpit telemetry flags into typed domain indicators.
- `ed-router` cannot verify route jump leg feasibility against vessel FSD mechanics, fuel constraints, and cargo mass.
- Downstream tools cannot validate engineering recipes, planetary landing criteria (gravity vs. thruster limits), or Odyssey loadouts.

To maintain deterministic reproducibility without introducing runtime I/O dependencies, where are these missing models located, what form do they take, and how will `ed-models` deterministically extract, compile, and integrate them via `scripts/` tooling?

---

## 2. Decision Drivers

* **Zero-I/O Runtime Boundary (`HEXA-TRUTH-01`):** All models and static data must exist as pure Python structures. Zero file reading, network calls, or third-party serialization libraries at runtime.
* **Hexagonal Boundary Enforcement (`HEXA-TRUTH-02`, `HEXA-TRUTH-03`):** Core entities reside in `core/domain/`, interactors in `core/use_cases/`, boundary contracts in `core/ports/`, and catalogs in `adapters/driven/static_catalogs/`.
* **Authoritative Source Provenance:** Every domain entity and catalog entry must trace back to vetted community authorities (`EDCD/EDDI`, `Lombra/elite-api-docs`, `EDMarketConnector`, `Coriolis`, `kayahr/ed-journal`).
* **Deterministic Build Pipelines:** Build scripts in `scripts/` must run offline, transform source files into typed Python code with complete validation, and format cleanly under Ruff and MyPy.

---

## 3. Reference Authorities & Source Data Formats

The remaining game domains are distributed across vetted peer repositories in specific technical formats:

| Domain Subsystem | Reference Authority & File Path | Source Format | Target `ed-models` Subsystem |
| :--- | :--- | :--- | :--- |
| **Cockpit Telemetry Flags** | `Lombra/elite-api-docs/docs/Status File.md`<br>`EDCD/EDDI/DataDefinitions/Status.cs` | Markdown table & C# `enum : ulong` | `core/domain/status/flags.py`<br>`core/domain/status/telemetry.py` |
| **Engineering Blueprints** | `EDCD/EDDI/DataDefinitions/Blueprint.cs`<br>`EDCD/EDDI/DataDefinitions/BlueprintTemplate.cs`<br>`EDCD/EDDI/DataDefinitions/Engineer.cs` | C# class definitions with 969 modification templates & static dictionaries | `core/domain/engineering/`<br>`adapters/driven/static_catalogs/engineering_catalog.py` |
| **Celestial Bodies Physics** | `EDCD/EDDI/DataDefinitions/Body.cs`<br>`EDCD/EDDI/DataDefinitions/BodySolidComposition.cs`<br>`EDCD/EDDI/DataDefinitions/BodyType.cs` | C# object definitions & Frontier Journal Chapter 5 (Exploration) | `core/domain/bodies/star.py`<br>`core/domain/bodies/planet.py`<br>`core/domain/spatial/` |
| **Odyssey Suits & Weapons** | `EDCD/EDDI/DataDefinitions/Suit.cs`<br>`EDCD/EDDI/DataDefinitions/SuitMod.cs`<br>`kayahr/ed-journal/src/main/events/odyssey/` | C# data definitions & TypeScript event schemas | `core/domain/types/suit.py`<br>`core/domain/odyssey/` |
| **Flight Mechanics Math** | `EDMarketConnector/edshipyard.py`<br>`EDCD/EDDI/DataDefinitions/ShipDefinitions.cs` | Python math expressions & Frontier physics formulas | `core/use_cases/calculate_jump_range.py`<br>`core/ports/driving/flight_mechanics_port.py` |

---

## 4. Deterministic Integration Pipelines (`scripts/`)

To preserve zero runtime I/O, extraction and code generation logic will reside exclusively in the developer tooling directory (`scripts/`):

1. **Telemetry & Bitfield Compilation (`scripts/compile_telemetry_flags.py`):**
   - Parses bit definitions from `Status File.md` and `Status.cs`.
   - Generates standard `enum.IntFlag` classes (`StatusFlags`, `StatusFlags2`) decorated with property accessors for all 52 known discrete flags.
   - Generates the high-level `StatusTelemetry` domain entity in `core/domain/status/`.

2. **Engineering Blueprint Extraction (`scripts/compile_engineering_catalog.py`):**
   - Employs AST or regex parsing against `Blueprint.cs` and `BlueprintTemplate.cs` to ingest modification templates, grade multipliers, experimental effects, and engineer locations.
   - Generates frozen in-memory dictionaries in `adapters/driven/static_catalogs/engineering_catalog.py` implementing `EngineeringCatalogProviderPort`.

3. **Celestial Body Entity Codification (`scripts/compile_celestial_models.py`):**
   - Extracts stellar types, planetary composition taxonomies, and atmosphere classes from `Body.cs`.
   - Author pure frozen dataclasses `StarBody` and `PlanetaryBody` in `core/domain/bodies/` with calculated properties (surface gravity in $g$, orbital period in days).

4. **Odyssey Suits & Equipment (`scripts/compile_odyssey_catalog.py`):**
   - Ingests suit specifications, base shield/health values, and mod slot capacities from `Suit.cs` and `SuitMod.cs`.
   - Author `SuitEntity` and `SuitWeaponEntity` in `core/domain/odyssey/` with driven static catalogs.

5. **Flight Mechanics Interactor (`core/use_cases/calculate_jump_range.py`):**
   - Transcribes verified FSD jump equations from `edshipyard.py` into a pure stateless interactor:
     $$D = \left( \frac{F_{\text{opt}} \cdot M_{\text{fsd}}}{M_{\text{total}}} \right)^{\frac{1}{P}} \cdot \left( \frac{C_{\text{fuel}}}{f_{\text{max}}} \right)$$
   - Validates jump calculations against known baseline tests from `EDMarketConnector` and Coriolis.

---

## 5. Consequences

### Positive
* **100% Domain Completeness:** Captures all remaining major gameplay mechanics (telemetry, engineering, bodies, Odyssey, jump physics) within `ed-models`.
* **Zero Runtime Overhead:** Catalogs remain in-memory pre-compiled Python structures; lookups execute in $O(1)$ time with zero disk or network I/O.
* **Strict Quality & Architectural Conformance:** All new driven ports declare matching `tests/doubles/` fakes and inherit `DrivenPort`; boundary tests verify hexagonal isolation.
* **Verified Provenance:** Data models directly reflect canonical Frontier IDs and community-tested schemas from EDDI and EDMC.

### Negative / Trade-offs
* **Initial Codification Effort:** Requires authoring robust C#/Markdown parsers in `scripts/` to convert definitions into pristine Python syntax.
* **Catalog Size Growth:** Adding 969 engineering blueprints and recipes will increase `adapters/driven/static_catalogs/` memory footprint by approximately ~1.2 MB (still well within the $< 5$ MB target budget).

---

## 6. Compliance and Invariant Verification

1. **`HEXA-TRUTH-01` & `HEXA-TRUTH-02`:** Verified via `pytest tests/architecture/test_boundaries.py` and `lint-imports`. No outer adapter or I/O library imported in `core/domain/`.
2. **`HEXA-TRUTH-03` & `HEXA-TRUTH-07`:** All secondary ports inherit `DrivenPort` from `core.ports.base`; exceptions inherit `DomainError`.
3. **`HEXA-TRUTH-14`:** `CalculateJumpRangeUseCase` is strictly stateless, accepting pure parameters and returning typed `JumpCalculationResult`.
