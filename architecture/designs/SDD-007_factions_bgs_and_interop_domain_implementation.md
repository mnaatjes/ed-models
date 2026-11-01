---
title: "SDD-007: Factions BGS and Interop Domain Implementation"
tags: ["sdd", "architecture", "factions", "bgs", "interop", "coriolis", "trade-dangerous"]
created_at: "2026-11-01"
last_updated_at: "2026-11-01"
---

# SDD-007: Factions BGS and Interop Domain Implementation

## 1. Executive Summary & Traceability

In accordance with [ADR 0006: Factions BGS and Interop Domain Models Architecture](file:///home/michael/src/github.com/mnaatjes/ed-models/architecture/adr/0006_factions_bgs_and_interop_domain_models.md) and [ADR 0001](file:///home/michael/src/github.com/mnaatjes/ed-models/architecture/adr/0001_ed_models_core_game_logic_and_catalog_architecture.md), this Software Design Document specifies the implementation of:

1. **Minor Faction & BGS Domain Models:** `MinorFactionPresence`, `Allegiance`, `Government`, and `FactionState` in `src/ed_models/core/domain/factions/`.
2. **Community Interop Formats:** `TradeDangerousMarketRecord`, `TradeDangerousFormatter`, and `CoriolisSerializer` in `src/ed_models/core/domain/interop/`.

### Traceability Links
* **Governing ADRs:** [ADR 0001](file:///home/michael/src/github.com/mnaatjes/ed-models/architecture/adr/0001_ed_models_core_game_logic_and_catalog_architecture.md), [ADR 0002](file:///home/michael/src/github.com/mnaatjes/ed-models/architecture/adr/0002_domain_scope_and_boundary_enforcement.md), [ADR 0006](file:///home/michael/src/github.com/mnaatjes/ed-models/architecture/adr/0006_factions_bgs_and_interop_domain_models.md).
* **Governing Invariants:** `HEXA-TRUTH-01` (Zero I/O in core), `HEXA-TRUTH-04` (DTO purity), `HEXA-TRUTH-10` (Immutability where applicable).

---

## 2. Data Structure Specifications

### 2.1 Factions Subsystem (`core/domain/factions/`)

#### Enums
* **`Allegiance(StrEnum)`**: `FEDERATION = "Federation"`, `EMPIRE = "Empire"`, `ALLIANCE = "Alliance"`, `INDEPENDENT = "Independent"`, `PILOTS_FEDERATION = "PilotsFederation"`, `NONE = "None"`.
* **`Government(StrEnum)`**: `ANARCHY = "Anarchy"`, `COMMUNISM = "Communism"`, `CONFEDERACY = "Confederacy"`, `COOPERATIVE = "Cooperative"`, `CORPORATE = "Corporate"`, `DEMOCRACY = "Democracy"`, `DICTATORSHIP = "Dictatorship"`, `FEUDAL = "Feudal"`, `PATRONAGE = "Patronage"`, `PRISON_COLONY = "PrisonColony"`, `THEOCRACY = "Theocracy"`, `ENGINEER = "Engineer"`, `NONE = "None"`.
* **`FactionState(StrEnum)`**: `NONE = "None"`, `BOOM = "Boom"`, `BUST = "Bust"`, `CIVIL_LIBERTY = "CivilLiberty"`, `CIVIL_UNREST = "CivilUnrest"`, `CIVIL_WAR = "CivilWar"`, `ELECTION = "Election"`, `EXPANSION = "Expansion"`, `FAMINE = "Famine"`, `INVESTMENT = "Investment"`, `LOCKDOWN = "Lockdown"`, `OUTBREAK = "Outbreak"`, `RETREAT = "Retreat"`, `WAR = "War"`, `DROUGHT = "Drought"`, `INCURSION = "Incursion"`, `PIRATE_ATTACK = "PirateAttack"`, `BLIGHT = "Blight"`, `COLD_WAR = "ColdWar"`, `COLONISATION = "Colonisation"`, `HISTORIC_EVENT = "HistoricEvent"`, `INFRASTRUCTURE_FAILURE = "InfrastructureFailure"`, `NATURAL_DISASTER = "NaturalDisaster"`, `PUBLIC_HOLIDAY = "PublicHoliday"`, `REVOLUTION = "Revolution"`, `TECHNOLOGICAL_LEAP = "TechnologicalLeap"`, `TERRORISM = "Terrorism"`, `TRADE_WAR = "TradeWar"`, `THARGOID_PROBING = "Thargoid_Probing"`, `THARGOID_HARVEST = "Thargoid_Harvest"`.

#### Entities
* **`MinorFactionPresence(dataclass, slots=True, kw_only=True)`**:
  - `faction_name: str`
  - `allegiance: Allegiance`
  - `government: Government`
  - `influence: float` (Validated: $0.0 \le \text{influence} \le 1.0$)
  - `active_states: tuple[FactionState, ...]`
  - `pending_states: tuple[FactionState, ...]`
  - `recovering_states: tuple[FactionState, ...]`
  - `happiness: str | None`
  - `squadron_faction: bool`

### 2.2 Interop Subsystem (`core/domain/interop/`)

#### Trade Dangerous Record
* **`TradeDangerousMarketRecord(dataclass, frozen=True, slots=True)`**:
  - `system_name: str`
  - `station_name: str`
  - `market_id: int`
  - `commodity_name: str`
  - `sell_price_cr: int`
  - `buy_price_cr: int`
  - `demand: int`
  - `stock: int`

#### Formatters & Serializers
* **`TradeDangerousFormatter.format_td(records: list[TradeDangerousMarketRecord], timestamp_str: str) -> str`**:
  - Generates the standard ASCII fixed-width table format used by the Trade Dangerous command-line utility.
* **`CoriolisSerializer.serialize_loadout(loadout: dict[str, object]) -> str`**:
  - Encodes a ship loadout dictionary to a gzip-compressed, URL-safe base64 string matching Coriolis.io specifications.

---

## 3. Verification and Quality Gates

1. **Linter & Formatting:** `ruff check . && ruff format --check .` (0 errors).
2. **Boundary Compliance:** `pytest tests/architecture/test_boundaries.py` (verifies zero I/O imports in `core/domain/`).
3. **Type Safety:** `mypy src/ tests/` (strict mode, zero errors).
4. **Unit Verification:** Validates `MinorFactionPresence` validation guards, Trade Dangerous text formatting, and Coriolis gzip roundtrips.
