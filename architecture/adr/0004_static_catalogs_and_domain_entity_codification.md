---
title: "ADR 0004: Static Catalogs and Domain Entity Codification Architecture"
tags: ["architecture", "adr", "catalogs", "ships", "modules", "commodities", "domain-entities", "fdev-ids"]
created_at: "2026-11-01"
last_updated_at: "2026-11-01"
---

# ADR 0004: Static Catalogs and Domain Entity Codification Architecture

## 1. Context and Problem Statement

`ed-models` serves as the offline domain model and computational authority for the *Elite Dangerous* software fleet (governed by [ADR 0001](file:///home/michael/src/github.com/mnaatjes/ed-models/architecture/adr/0001_ed_models_core_game_logic_and_catalog_architecture.md) and [ADR 0002](file:///home/michael/src/github.com/mnaatjes/ed-models/architecture/adr/0002_domain_scope_and_boundary_enforcement.md)).

While the streaming event plane is fully codified (284+ event models across 11 categories synthesized from `kayahr/ed-journal`), the domain currently lacks core persistent game entities (`ShipHull`, `ShipModule`, `CommodityEntity`) and their underlying static catalogs. Without these entities:
1. Use cases (`LookupShipUseCase`, `NormalizeTokenUseCase`, `CalculateJumpRangeUseCase`) cannot resolve vessels, module masses, or commodity taxonomy.
2. Event payloads containing internal Frontier IDs (`MarketID`, `SystemAddress`, ship IDs, module IDs) cannot hydrate into rich domain objects.
3. Fleet services (`ed-telemetry`, `ed-connector`, `ed-router`) lack an offline, in-memory reference authority for hull masses, landing pad requirements, and trade commodities.

Authoritative codifications exist locally in community repositories:
- `EDCD/EDDI` (`DataDefinitions/ShipDefinitions.cs`, `CommodityDefinition.cs`, `ModuleDefinitions.cs`)
- `EDMarketConnector` (`ships.json`, `modules.json`, `util_ships.py`, `outfitting.py`)

How should `ed-models` codify domain entities and compile static catalogs to guarantee $O(1)$ in-memory lookups while strictly preserving zero I/O runtime constraints and hexagonal boundary purity?

---

## 2. Decision Drivers

* **Zero-I/O Runtime Invariant (`HEXA-TRUTH-01`):** Shipping wheel package must have zero disk reading, zero network transport, and zero database drivers. Catalogs must be compiled as in-memory Python data structures.
* **Pure Hexagonal Decoupling (`HEXA-TRUTH-02`, `HEXA-TRUTH-03`):** Core domain entities (`core/domain/`) must define pure business concepts; static catalog lookup dictionaries must reside in driven adapters (`adapters/driven/static_catalogs/`) implementing driven ports (`core/ports/driven/`).
* **Contract Elasticity & Fallback (`RISK-02`):** Discrete Frontier constants ($\le 50$) use `StrEnum` (e.g., `Manufacturer`, `PadSize`, `CommodityCategory`). Expanding taxonomies ($> 100$, like commodities and modules) must be resilient to uncataloged IDs with graceful fallback rather than runtime deserialization crashes.
* **Low Memory Footprint & High Performance (`RISK-04`):** Entity dataclasses must declare `slots=True`, and static catalogs must provide $O(1)$ key lookup by canonical symbol and Frontier ID. Total compiled catalog memory must remain $< 2$ MB.

---

## 3. Considered Options

* **Option 1: Runtime SQLite/JSON Loading.** Distribute JSON or SQLite database files in `src/ed_models/` and load them on startup via disk I/O.
* **Option 2: External HTTP/API Resolution.** Query EDDN, Spansh, or Coriolis web APIs dynamically when lookups occur.
* **Option 3: Offline Pre-Compiled In-Memory Python Adapters (Selected).** Author pure domain dataclasses in `core/domain/` and implement an offline build tool (`scripts/compile_catalogs.py`) that extracts and compiles catalogs from `EDCD/EDDI` and `EDMC` into pure frozen in-memory dictionaries in `adapters/driven/static_catalogs/`.

---

## 4. Decision Outcome

**Chosen Option:** **Option 3: Offline Pre-Compiled In-Memory Python Adapters.**

### 4.1 Domain Entity Specifications (`src/ed_models/core/domain/`)

#### 1. Ships Subdomain (`core/domain/ships/`)
- `ShipHull`: Slotted dataclass representing base hull specifications.
  - Fields: `model: str`, `name: str`, `manufacturer: Manufacturer`, `pad_size: PadSize`, `hull_mass: float`, `reserve_fuel_capacity: float`, `military_slots: dict[str, int]`.
- `ShipModule`: Slotted dataclass representing outfitting components.
  - Fields: `fdev_id: int`, `symbol: str`, `name: str`, `class_num: int`, `rating: str`, `mass: float`, `power_draw: float | None = None`.
- Supporting Enums in `core/domain/types/`: `Manufacturer` (`FaulconDeLacy`, `CoreDynamics`, `Gutamaya`, `LakonSpaceways`, `SaudKruger`, `ZorgonPeterson`).

#### 2. Commodities Subdomain (`core/domain/commodities/`)
- `CommodityEntity`: Slotted dataclass representing canonical trade goods.
  - Fields: `fdev_id: int`, `symbol: str`, `name: str`, `category: CommodityCategory`, `average_price: int`, `is_rare: bool = False`.
- Supporting Enums in `core/domain/types/`: `CommodityCategory` (`Chemicals`, `ConsumerItems`, `Foods`, `IndustrialMaterials`, `LegalDrugs`, `Machinery`, `Medicines`, `Metals`, `Minerals`, `Salvage`, `Slaves`, `Technology`, `Textiles`, `Waste`, `Weapons`, `NonMarketable`, `Unknown`).

#### 3. Cockpit Telemetry & Bitfields (`core/domain/status/`)
- Pure bitfield unpackers extracting boolean telemetry states from raw 32-bit `Flags` and `Flags2` integers into strongly typed dataclasses without I/O dependencies.

### 4.2 Secondary Driven Catalog Ports (`core/ports/driven/`)

Boundary protocols defining secondary catalog providers:
- `ShipCatalogProviderPort`: `get_hull_spec(model: str) -> ShipHull | None`
- `ModuleCatalogProviderPort`: `get_module_by_id(fdev_id: int) -> ShipModule | None`, `get_module_by_symbol(symbol: str) -> ShipModule | None`
- `CommodityCatalogProviderPort`: `get_commodity_by_id(fdev_id: int) -> CommodityEntity | None`, `get_commodity_by_symbol(symbol: str) -> CommodityEntity | None`

### 4.3 Driven In-Memory Adapters (`adapters/driven/static_catalogs/`)

Pre-compiled Python lookup tables executing with zero I/O and zero latency:
- `ships_catalog.py`: Maps ~48 ship models to `ShipHull` entities.
- `modules_catalog.py`: Maps ~1,169 outfitting modules to `ShipModule` entities indexed by `fdev_id` and normalized `symbol`.
- `commodities_catalog.py`: Maps ~450 trade goods to `CommodityEntity` entities indexed by `fdev_id` and normalized `symbol`.

### 4.4 Compilation Tooling Architecture (`scripts/compile_catalogs.py`)

- Resides strictly in `scripts/`, never packaged into the runtime distribution wheel.
- Ingests:
  - `EDCD/EDDI`: `ShipDefinitions.cs`, `CommodityDefinition.cs`, `ModuleDefinitions.cs`
  - `EDMarketConnector`: `ships.json`, `modules.json`
- Synthesizes formatted Python catalog modules directly into `src/ed_models/adapters/driven/static_catalogs/`.

---

## 5. Consequences

### Positive

* **Zero-Latency In-Memory Lookups:** Lookups execute in $O(1)$ time ($< 1\,\mu\text{s}$) with zero disk or network overhead.
* **Strict Hexagonal Purity:** Domain entities remain completely pure; catalogs are isolated as driven adapters.
* **Offline Fleet Portability:** Software fleet packages (`ed-telemetry`, `ed-connector`, `ed-router`) run offline anywhere without database initialization.
* **Community Alignment:** Leverages authoritative mappings vetted by EDCD (Elite Dangerous Community Developers).

### Negative & Mitigations

* **Catalog Maintenance Over Game Patches:**
  * *Risk:* Upstream game updates introduce new ships, modules, or commodities.
  * *Mitigation:* Re-running `scripts/compile_catalogs.py` updates catalogs deterministically in seconds; unknown commodities fallback to `CommodityCategory.Unknown` with zero crashes.

---

## 6. References

* [ADR 0001: ed-models Pure Domain Architecture, Catalog Codification, and Driving Facade](file:///home/michael/src/github.com/mnaatjes/ed-models/architecture/adr/0001_ed_models_core_game_logic_and_catalog_architecture.md)
* [ADR 0002: Domain Scope and Boundary Enforcement Mechanics](file:///home/michael/src/github.com/mnaatjes/ed-models/architecture/adr/0002_domain_scope_and_boundary_enforcement.md)
* [ADR 0003: TypeScript Model Extraction and Domain Transformation Pipeline](file:///home/michael/src/github.com/mnaatjes/ed-models/architecture/adr/0003_typescript_model_extraction_and_transformation_pipeline.md)
* Repository `EDCD/EDDI`: `/home/michael/src/github.com/EDCD/EDDI`
* Repository `EDMarketConnector`: `/home/michael/src/github.com/mnaatjes/EDMarketConnector`
