---
title: "Use-Case Specification: UC-01 Normalize Frontier Tokens"
use_case_id: "UC-01"
status: "approved"
version: "1.0.0"
level: "sea_level"
primary_actor: "Fleet Ingestion Consumer (ed-telemetry / ed-connector)"
created_at: "2026-11-01"
last_updated_at: "2026-11-01"
---

# Use-Case Specification: UC-01 Normalize Frontier Tokens

## 1. Description & Goal
Resolves raw, internal Frontier Developments string tokens (e.g. `$grain_name;`, `$modularterminals_name;`, `"empire_trader"`) or localized game strings into strongly typed, canonical domain entities (`CommodityEntity`, `ShipHull`).

## 2. Actors & Scope
* **Primary Actor:** Calling service (`ed-telemetry`, `ed-connector`, or `ed-router`).
* **System Boundary:** `ed-models` driving port facade (`EliteDomainFacade`).

## 3. Preconditions
* Static catalogs are pre-compiled and initialized in `ed-models` memory.

## 4. Postconditions
* Caller receives an immutable canonical domain record or fallback object with zero exceptions.

## 5. Main Success Scenario (Basic Flow)
1. Actor invokes `facade.normalize_commodity(token)` passing a raw Frontier string.
2. The interactor trims surrounding `$` prefixes and `;` suffixes, stripping case sensitivity.
3. The interactor queries the in-memory static catalog adapter for the sanitized key.
4. The catalog returns the canonical `CommodityEntity(id=..., symbol=..., category=...)`.
5. The facade returns the entity to the actor.

## 6. Extensions (Alternative Flows)
* **3a. Token Not Found in Static Catalog:**
  1. The interactor attempts localized lookup in secondary dictionary.
  2. If still unmapped, the interactor constructs a synthetic fallback `CommodityEntity(id=0, symbol=sanitized_token, category=CommodityCategory.UNKNOWN)`.
  3. The facade returns the fallback entity without raising a runtime exception.
