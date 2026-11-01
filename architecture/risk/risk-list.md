---
title: "Master Risk Register"
tags: ["architecture", "risk", "governance", "boehm", "unified-process"]
created_at: "2026-11-01"
last_updated_at: "2026-11-01"
---

# Master Risk Register

This document tracks and quantifies the architectural, technical, and domain risks for `ed-models` using Barry Boehm's classical Risk Exposure ($RE$) metric:

$$RE = P \times I$$

* **Probability ($P$):** Integer scale `1` (Extremely Unlikely) to `5` (Near Certainty).
* **Impact ($I$):** Integer scale `1` (Negligible / Cosmetic) to `5` (Catastrophic / Outage / Data Corruption).
* **Risk Exposure ($RE$):** Product range `1` to `25`.
  * **Critical Exposure ($RE \ge 16$):** Architectural blocker requiring immediate mitigation.
  * **Moderate Exposure ($9 \le RE \le 15$):** Active monitoring with explicit mitigation plan.
  * **Low Exposure ($RE < 9$):** Documented; managed procedurally.

---

## 1. Active Risk Matrix

| Risk ID | Title | Cat. | $P$ | $I$ | $RE$ | Exposure Level | Status |
| :--- | :--- | :--- | :---: | :---: | :---: | :--- | :--- |
| **RISK-01** | FDev Catalog Drift & Missing Tokens | Domain | 4 | 4 | **16** | 🔴 Critical | Active |
| **RISK-02** | Rigid Enum Deserialization Crashes | Arch | 5 | 3 | **15** | 🟡 Moderate | Active |
| **RISK-03** | Dataclass Inheritance Default Ordering | Code | 5 | 4 | **20** | 🔴 Critical | Mitigated (ADR 0001) |
| **RISK-04** | Stream Ingestion Memory Bloat | Perf | 3 | 4 | **12** | 🟡 Moderate | Active |
| **RISK-05** | Hexagonal Boundary I/O Leakage | Arch | 2 | 5 | **10** | 🟡 Moderate | Active |

---

## 2. Risk Detail & Mitigation Plans

### RISK-01: FDev Catalog Drift & Missing Tokens
* **Description:** Frontier Developments patches *Elite Dangerous* with new ship hulls, outfitting modules, or commodities without prior public schema updates. Static in-memory catalogs in `ed-models` become stale, potentially causing downstream services to fail entity lookups.
* **Scoring:** $P=4, I=4 \rightarrow RE=16$ (Critical).
* **Mitigation Plan:**
  1. Automated update pipeline (Note 0006) pulling upstream community datasets (`FDevIDs`, `modules.json`, `ships.json`) on automated schedules.
  2. Fallback to generic `CommodityEntity` / `ShipHull` records populated with raw token identifiers rather than crashing lookups.
  3. Downstream runtime cache overlays in `ed-connector` to dynamically inject uncataloged items.

### RISK-02: Rigid Enum Deserialization Crashes
* **Description:** Declaring expanding domain sets (such as commodities or engineering blueprints) as rigid Python `StrEnum` classes causes `ValueError: 'new_item' is not a valid Commodity` during JSON hydration of unreleased game items.
* **Scoring:** $P=5, I=3 \rightarrow RE=15$ (Moderate).
* **Mitigation Plan:**
  1. Enforce ADR 0001 Section 4.6 Closed-Set Rule: only bounded vocabularies ($\le 50$ items, e.g. `PadSize`, `Allegiance`, `StarType`) use `StrEnum`.
  2. Open taxonomies (commodities, modules) remain canonical `str` symbols backed by $O(1)$ dictionary lookups.

### RISK-03: Dataclass Inheritance Default Parameter Ordering
* **Description:** In Python dataclass inheritance, a subclass with default-valued fields cannot inherit from a base class with non-default positional fields, throwing `TypeError: non-default argument 'timestamp' follows default argument`.
* **Scoring:** $P=5, I=4 \rightarrow RE=20$ (Critical).
* **Mitigation Plan:**
  * Enforce ADR 0001 Section 4.6 Rule 4: all event base classes (`JournalEvent`) and derived event classes must declare `@dataclass(kw_only=True)`.
  * Verified in test suite via automated boundary tests.

### RISK-04: Stream Ingestion Memory Bloat
* **Description:** Ingesting hundreds of thousands of historical journal entries across multi-year player logs creates massive Python dictionary overhead if dataclasses are instantiated without memory optimization.
* **Scoring:** $P=3, I=4 \rightarrow RE=12$ (Moderate).
* **Mitigation Plan:**
  1. Enforce `@dataclass(slots=True)` across all domain entities, coordinate value objects, and event models to strip `__dict__` overhead.
  2. Value objects (`Coordinates3D`) declare `frozen=True, slots=True`.

### RISK-05: Hexagonal Boundary I/O Leakage
* **Description:** Developers accidentally importing filesystem I/O (`open()`, `pathlib.Path.read_text()`), network clients (`requests`, `httpx`), or telemetry tailers (`ed-telemetry`) into `core/domain/`, violating the pure offline library contract.
* **Scoring:** $P=2, I=5 \rightarrow RE=10$ (Moderate).
* **Mitigation Plan:**
  1. Continuous enforcement via `import-linter` (`.importlinter`) and `pytest-archon` in `tests/architecture/test_boundaries.py`.
  2. Automated quality gates in CI blocking PRs that introduce forbidden imports into `core/`.
