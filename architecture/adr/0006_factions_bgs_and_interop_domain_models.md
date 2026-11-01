---
title: "ADR 0006: Factions BGS and Interop Domain Models Architecture"
tags: ["architecture", "adr", "factions", "bgs", "interop", "coriolis", "trade-dangerous"]
created_at: "2026-11-01"
last_updated_at: "2026-11-01"
---

# ADR 0006: Factions BGS and Interop Domain Models Architecture

## 1. Context and Problem Statement

Following the codification of static ship/module/commodity catalogs ([ADR 0004](file:///home/michael/src/github.com/mnaatjes/ed-models/architecture/adr/0004_static_catalogs_and_domain_entity_codification.md)) and physical/telemetry domains ([ADR 0005](file:///home/michael/src/github.com/mnaatjes/ed-models/architecture/adr/0005_harvesting_and_codification_of_remaining_game_domains.md)), two critical domain packages remain empty in `ed-models`:

1. **Background Simulation (BGS) & Minor Factions (`core/domain/factions/`):** Star system presence, political allegiances, government structures, influence levels, and dynamic system states (economic, security, conflict, movement).
2. **Offline Interoperability Formats (`core/domain/interop/`):** Pure in-memory generation of community interchange formats (Trade Dangerous `.td` price records and Coriolis URL-safe loadout compression).

Without these models:
- Star system models and jump events cannot strongly type minor faction presences or evaluate BGS political changes.
- Downstream tools (`ed-router`, `ed-connector`) cannot serialize ship configurations or starport trade dumps into universal community interchange representations without pulling in external utility libraries.

Where are the authoritative references for these models, what form do they take, and how will `ed-models` codify them in compliance with hexagonal zero-I/O invariants?

---

## 2. Decision Drivers

* **Pure Domain Invariants (`HEXA-TRUTH-01`):** All models must be pure in-memory representations. Zero disk I/O, zero network sockets, and zero HTTP clients.
* **Format Compatibility:** Interop serializers must strictly generate valid Trade Dangerous format v2 text and Coriolis URL-safe gzip-base64 hashes without filesystem writes.
* **Frontier Canonical Accuracy:** BGS states, allegiances, and governments must match official Frontier Journal schemas and community reference standards (`EDCD/EDDI`, `EDMarketConnector`).
* **Self-Validating Dataclasses:** All entities must enforce attribute bounds (influence between 0.0 and 1.0, non-empty names) via `__post_init__` guards.

---

## 3. Reference Authorities & Data Formats

1. **Minor Factions & BGS:**
   * **Source Authority:** `EDCD/EDDI/DataDefinitions/Faction.cs` & `FactionState.cs`.
   * **Source Format:** C# classes and localized resource definitions.
   * **Codification Target:** `src/ed_models/core/domain/factions/` (`MinorFactionPresence`, `FactionState`, `Allegiance`, `Government`, `Happiness`).
2. **Coriolis Loadout Serialization:**
   * **Source Authority:** `EDMarketConnector/plugins/common_coreutils.py` (`shipyard_url_common`).
   * **Source Format:** Python standard library `json`, `gzip`, and `base64`.
   * **Codification Target:** `src/ed_models/core/domain/interop/coriolis.py` (`CoriolisSerializer`).
3. **Trade Dangerous Market Records:**
   * **Source Authority:** `architecture/adr/0001_ed_models_core_game_logic_and_catalog_architecture.md` (§4.5.6) & Trade Dangerous documentation.
   * **Source Format:** Fixed-width ASCII tabular price ledger.
   * **Codification Target:** `src/ed_models/core/domain/interop/trade_dangerous.py` (`TradeDangerousMarketRecord`, `TradeDangerousFormatter`).

---

## 4. Deterministic Codification Architecture

1. **Factions Subsystem:**
   * Implement discrete `StrEnum` types for `Allegiance` (`Federation`, `Empire`, `Alliance`, `Independent`, `PilotsFederation`), `Government` (`Democracy`, `Corporate`, `Anarchy`, `Patronage`, `Communism`, `Feudal`, `Dictatorship`, `Theocracy`, `PrisonColony`, `Engineer`), and `FactionState` (covering all 30+ official economic, security, and conflict states).
   * Implement `MinorFactionPresence(dataclass, slots=True, kw_only=True)` capturing `faction_name`, `influence` ($0.0 \dots 1.0$), `reputation`, `active_states`, `pending_states`, and `recovering_states`.
2. **Interop Subsystem:**
   * Implement `TradeDangerousMarketRecord(dataclass, frozen=True, slots=True)` capturing `system_name`, `station_name`, `market_id`, `commodity_name`, `sell_price_cr`, `buy_price_cr`, `demand`, and `stock`.
   * Implement pure in-memory string formatting utilities that produce deterministic outputs without writing to disk.

---

## 5. Consequences

### Positive
* **100% Completion of Planned Domain Scaffold:** All domain directories articulated in ADR 0001 are fully implemented and verified.
* **Deterministic Interoperability:** Tools can export Coriolis URLs and Trade Dangerous manifests entirely in-memory with zero runtime dependencies.
* **Strict Quality Conformance:** All new models pass AST boundary tests, `import-linter` contracts, strict MyPy type checking, and pre-commit hooks.

### Negative / Trade-offs
* None; both additions are lightweight, offline, and contain zero runtime dependencies.
