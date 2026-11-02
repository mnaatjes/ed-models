---
title: "How to Use EliteDomainFacade"
tags: ["docs", "how-to", "facade", "ed-models", "diataxis", "examples"]
created_at: "2026-11-01"
last_updated_at: "2026-11-01"
---

# How to Use EliteDomainFacade

This practical guide demonstrates how to consume the [`EliteDomainFacade`](file:///home/michael/src/github.com/mnaatjes/ed-models/src/ed_models/adapters/driving/facade.py) from application services (`ed-telemetry`, `ed-connector`, `ed-router`).

---

## 1. Initializing the Facade

Import and instantiate the facade via the top-level convenience factory:

```python
from ed_models import create_domain_facade

facade = create_domain_facade()
```

---

## 2. Querying Pre-Compiled Static Catalogs

Lookups execute in $O(1)$ time against static in-memory data structures without network requests:

```python
# Look up a ship hull specification
hull = facade.get_ship("anaconda")
if hull:
    print(f"Ship: {hull.name}, Base Mass: {hull.hull_mass}t, Pad: {hull.pad_size}")

# Look up an outfitting module by Frontier ID
module = facade.get_module_by_id(128049382)
if module:
    print(f"Module: {module.name}, Rating: {module.rating}, Mass: {module.mass}t")

# Look up an engineering modification blueprint
blueprint = facade.get_blueprint("fsd_longrange")
if blueprint:
    grade_5 = blueprint.grades.get(5)
    print(f"Blueprint: {blueprint.name}, Grade 5 Ingredients: {len(grade_5.ingredients) if grade_5 else 0}")
```

---

## 3. Deserializing Live Journal Streams

Transform raw event payloads from `Journal.*.log` into typed, validated Python dataclasses:

```python
raw_payload = {
    "timestamp": "2026-11-01T23:30:00Z",
    "event": "FSDJump",
    "StarSystem": "Deciat",
    "SystemAddress": 6683103214041,
    "JumpDist": 42.15,
    "FuelUsed": 3.8,
}

event = facade.parse_journal_event(raw_payload)

print(f"Received Event: {event.event}")
# Fields are strongly typed
if hasattr(event, "StarSystem"):
    print(f"Arrived at: {event.StarSystem}, Jump Distance: {event.JumpDist} ly")
```

---

## 4. Unpacking Cockpit Telemetry (`Status.json`)

Decode continuous cockpit telemetry bitmasks into ergonomic boolean properties:

```python
from ed_models import StatusFlags, StatusFlags2

# Raw bits from Status.json
raw_flags = int(StatusFlags.DOCKED | StatusFlags.LIGHTS_ON | StatusFlags.SHIELDS_UP)
raw_flags2 = int(StatusFlags2.ON_FOOT)

telemetry = facade.parse_telemetry(
    flags=raw_flags,
    flags2=raw_flags2,
    pips=(4, 4, 4),
    fuel_main=32.0,
    cargo=4,
)

print(f"Docked: {telemetry.is_docked}")
print(f"On Foot: {telemetry.is_on_foot}")
print(f"In Supercruise: {telemetry.is_supercruise}")
```

---

## 5. Calculating FSD Jump Range

Evaluate exact Newtonian jump physics for vessel loadouts:

```python
from ed_models import JumpCalculationParameters

params = JumpCalculationParameters(
    fsd_optimal_mass=2700.0,
    fsd_max_fuel_per_jump=8.0,
    fsd_fuel_multiplier=0.012,
    fsd_fuel_power=2.75,
    unladen_mass=450.0,
    cargo_mass=32.0,
    fuel_mass=32.0,
)

result = facade.calculate_jump_range(params)

print(f"Current Jump Range: {result.current_jump_range_ly} ly")
print(f"Unladen Jump Range: {result.unladen_jump_range_ly} ly")
print(f"Max Jump Range: {result.max_jump_range_ly} ly")
print(f"Fuel Consumed: {result.fuel_consumed} t")
```

---

## 6. Exporting Community Formats

Generate community interchange formats in-memory with zero disk writes:

```python
# 1. Trade Dangerous ASCII export
from ed_models import TradeDangerousMarketRecord

record = TradeDangerousMarketRecord(
    system_name="Deciat",
    station_name="Garay Terminal",
    market_id=128000001,
    commodity_name="Gold",
    sell_price_cr=45000,
    buy_price_cr=46000,
    demand=500,
    stock=1200,
)
td_output = facade.format_trade_dangerous([record], "2026-11-01 23:30:00")
print(td_output)

# 2. Coriolis URL hash export
loadout_dict = {
    "ship": "Anaconda",
    "components": {"standard": {"armour": "128049382"}},
}
url_hash = facade.serialize_coriolis(loadout_dict)
print(f"Coriolis URL: https://coriolis.io/outfit/{url_hash}")
```
