---
title: "Use-Case Specification: UC-02 Hydrate Journal Stream Event"
use_case_id: "UC-02"
status: "approved"
version: "1.0.0"
level: "sea_level"
primary_actor: "Stream Processor (ed-telemetry)"
created_at: "2026-11-01"
last_updated_at: "2026-11-01"
---

# Use-Case Specification: UC-02 Hydrate Journal Stream Event

## 1. Description & Goal
Transforms a validated raw dictionary representing a single line from `Journal.<timestamp>.log` into a strongly typed, routable `JournalEvent` subclass (e.g. `FsdJumpEvent`, `ScanEvent`, `MarketBuyEvent`).

## 2. Actors & Scope
* **Primary Actor:** Log ingestion engine (`ed-telemetry`).
* **System Boundary:** `ed-models` driving port facade (`EliteDomainFacade`).

## 3. Preconditions
* The raw payload dictionary contains valid JSON text pre-validated by `ed-schema`.

## 4. Postconditions
* A concrete Python dataclass inheriting from `JournalEvent(kw_only=True)` is instantiated and returned.

## 5. Main Success Scenario (Basic Flow)
1. Actor passes a dictionary (`payload`) to `facade.parse_journal_event(payload)`.
2. The interactor inspects the `"event"` key (case-insensitively) as the discriminator.
3. The interactor retrieves the corresponding registered event dataclass for that event name.
4. The interactor maps the `"timestamp"` string into a UTC `datetime` object.
5. The concrete event dataclass is instantiated using keyword arguments.
6. The facade returns the strongly typed event instance to the actor.

## 6. Extensions (Alternative Flows)
* **3a. Event Name Unrecognized / New FDev Event:**
  1. The interactor falls back to the generic `JournalEvent(timestamp=ts, event=event_name, extra=payload)`.
  2. The generic event is returned, preserving payload routing capability without dropping messages.
