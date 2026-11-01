---
title: "Use-Case Specification: UC-05 Export Station Market Interop"
use_case_id: "UC-05"
status: "approved"
version: "1.0.0"
level: "sea_level"
primary_actor: "Market Exporter (ed-connector)"
created_at: "2026-11-01"
last_updated_at: "2026-11-01"
---

# Use-Case Specification: UC-05 Export Station Market Interop

## 1. Description & Goal
Transforms station commodity inventory records (`Market.json`) into standard external file format strings (Trade Dangerous `.td` and Coriolis loadout JSON) for consumption by local desktop companion tools.

## 2. Actors & Scope
* **Primary Actor:** Desktop connector (`ed-connector`).
* **System Boundary:** `ed-models` driving port facade (`EliteDomainFacade`).

## 3. Preconditions
* A list of `TradeDangerousMarketRecord` items exists in memory.

## 4. Postconditions
* Returns formatted text strings adhering strictly to Trade Dangerous or Coriolis specification with zero filesystem I/O performed.

## 5. Main Success Scenario (Basic Flow)
1. Actor invokes `facade.to_trade_dangerous(records, timestamp)`.
2. The interactor verifies record set is non-empty.
3. The interactor formats header lines (`@ System`, `+ Station`, `$ MarketId`).
4. The interactor formats table entries with strict column width formatting.
5. The complete `.td` file string is returned to the actor for disk writing.
