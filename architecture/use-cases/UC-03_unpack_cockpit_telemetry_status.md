---
title: "Use-Case Specification: UC-03 Unpack Cockpit Telemetry Status"
use_case_id: "UC-03"
status: "approved"
version: "1.0.0"
level: "sea_level"
primary_actor: "Desktop Client / Overlay (ed-connector)"
created_at: "2026-11-01"
last_updated_at: "2026-11-01"
---

# Use-Case Specification: UC-03 Unpack Cockpit Telemetry Status

## 1. Description & Goal
Converts raw 32-bit status bitfields (`Flags` and `Flags2`) and cockpit instrumentation telemetry from `Status.json` into typed boolean properties and domain telemetry models (`ShipStatus`).

## 2. Actors & Scope
* **Primary Actor:** Desktop connector / overlay daemon (`ed-connector`).
* **System Boundary:** `ed-models` driving port facade (`EliteDomainFacade`).

## 3. Preconditions
* `Status.json` was read from disk by `ed-telemetry` and validated.

## 4. Postconditions
* A structured `ShipStatus` dataclass is returned exposing ergonomic boolean accessors (`docked`, `landed`, `gear_down`, `shields_up`, `in_supercruise`).

## 5. Main Success Scenario (Basic Flow)
1. Actor passes raw status dictionary to `facade.parse_status(payload)`.
2. The interactor extracts integer values from `Flags` and `Flags2`.
3. The interactor creates `StatusFlags(flags_int)` and `StatusFlags2(flags2_int)`.
4. The interactor unpacks pips array, fuel capacity, firegroup, and legal state.
5. The interactor populates and returns the immutable `ShipStatus` model.
