---
title: "Domain Architecture and Taxonomy Reference"
tags: ["domain", "architecture", "taxonomy", "reference", "ed-models"]
created_at: "2026-11-02"
last_updated_at: "2026-11-02"
---

# Domain Architecture and Taxonomy Reference

This document provides a comprehensive structural reference of the pure hexagonal domain core within `ed-models` (`src/ed_models/core/domain/`). It details the domain entities, value objects, discrete types, and structural boundaries maintained in the library.

---

## 1. Architectural Invariants

The domain layer of `ed-models` strictly enforces:
- **Zero I/O:** Zero network, zero disk/filesystem access, zero third-party transport dependencies.
- **Pure Entities & Value Objects:** All models are immutable (`frozen=True`) or explicitly bounded domain dataclasses, enums (`StrEnum`, `IntFlag`), or pure typing constructs.
- **Polymorphic Events Hierarchy:** Event models mapped 1:1 to Frontier Journal specifications across Chapters 2–13, deriving from `JournalEvent` with `kw_only=True`.
- **Stateless Mathematical Interactors:** Calculations (e.g. jump range) are executed by isolated use case interactors without domain entity mutation.

---

## 2. Domain Taxonomy & Package Breakdown

```
src/ed_models/core/domain/
├── bodies/          # Stellar and planetary physical properties
├── commodities/     # Trade commodities and market goods
├── engineering/     # Engineers, blueprints, experimental effects
├── events/          # Frontier Journal event hierarchy (Chapters 2–13)
├── factions/        # Minor factions, government types, reputations
├── flight/          # Flight mechanics, jump parameters, FSD physics
├── interop/         # External schema converters (Trade Dangerous, Coriolis)
├── odyssey/         # On-foot suits, weapons, micro-resources
├── ships/           # Hull specifications, module ratings, slot mechanics
├── spatial/         # 3D GalMap coordinates with frozen vector slots
├── status/          # Cockpit telemetry, bitfields, UI status flags
└── types/           # Canonical enums, bitflags, Frontier string constants
```

### 2.1. `types/` (Discrete Enums and Primitive Bitfields)
Provides strongly typed `StrEnum` and `IntFlag` mappings for Frontier specification constants:
- **`StarType` (`star_type.py`):** Canonical stellar classifications (O, B, A, F, G, K, M, L, T, Y, White Dwarfs, Neutron, Black Holes).
- **`PlanetClass` (`planet_class.py`):** Terrestrial and gas giant body classes (High metal content, Earth-like, Ammonia world, Water world, Gas giant types I–V).
- **`StationType` (`station_type.py`):** Orbital and surface ports (Coriolis, Orbis, Ocellus, Outpost, AsteroidBase, SurfaceStation).
- **`StationService` (`station_service.py`):** Available station facilities (Dock, Autodock, Commodities, Contacts, CrewLounge, Outfitting, Shipyard, Refuel, Repair, Rearm).
- **`PadSize` (`pad_size.py`):** Landing pad sizing boundaries (`Small`, `Medium`, `Large`).
- **`Manufacturer` (`manufacturer.py`):** Ship and equipment manufacturers (Faulcon DeLacy, Gutamaya, Core Dynamics, Lakon Spaceways, Zorgon Peterson).
- **`CommodityCategory` (`commodity_category.py`):** Economic categories (Chemicals, Consumer Items, Foods, Industrial Materials, Machinery, Medicines, Metals, Minerals, Technology, Textiles, Weapons).
- **`MicroResource` (`micro_resource.py`):** Odyssey on-foot material categories (Data, Chemical, Item, Tech).
- **`CarrierType` (`carrier_type.py`):** Fleet carrier structural classes.
- **`BodyType` (`body_type.py`):** Body classifications (`Null`, `Star`, `Planet`, `Station`).
- **`PowerState`, `PowerState1`, `PowerState2`:** Powerplay state enums mapping legacy and updated Powerplay 2.0 dynamics.
- **`ConflictFaction`, `ConflictProgress`:** Conflict zones, war progression, and combat bonds.

### 2.2. `spatial/` (3D Spatial Geometry)
- **`Coordinates3D` (`coordinates.py`):** Lightweight immutable 3D Cartesian coordinates `(x, y, z)` in light-years.
  - Declares `__slots__ = ("x", "y", "z")` for $O(1)$ memory allocation.
  - Implements Euclidean distance calculations (`distance_to(other)`).

### 2.3. `bodies/` (Stellar & Planetary Physics)
- **`StarBody` (`star.py`):** Stellar body physics model:
  - Attributes: `name`, `star_type`, `subclass`, `mass_solar`, `radius_solar`, `surface_temp_k`, `age_my`, `is_main_star`, `luminosity`.
- **`PlanetaryBody` (`planet.py`):** Terrestrial and gas giant physics model:
  - Attributes: `name`, `planet_class`, `mass_earth`, `radius_km`, `surface_gravity_g`, `surface_temp_k`, `surface_pressure_atm`, `is_landable`, `volcanism_type`, `atmosphere_type`.

### 2.4. `ships/` (Ship Outfitting & Hull Specifications)
- **`ShipHull` (`hull.py`):** Ship frame and core specification:
  - Attributes: `hull_id`, `name`, `code`, `manufacturer`, `pad_size`, `hull_mass_t`, `base_shield`, `base_armour`, `base_cargo`, `core_slots`, `military_slots`, `optional_slots`.
- **`ShipModule` (`module.py`):** Outfitting module specifications:
  - Attributes: `module_id`, `symbol`, `name`, `category`, `slot_size`, `rating`, `mass_t`, `power_draw_mw`.

### 2.5. `commodities/` (Trade Goods)
- **`Commodity` (`commodity.py`):** Canonical trade item entity:
  - Attributes: `symbol`, `name`, `category`, `average_price`, `is_rare`, `max_allocation`.

### 2.6. `engineering/` (Engineering Blueprints & Experimental Effects)
- **`Engineer` (`engineer.py`):** Workshop engineer entity (`engineer_id`, `name`, `system`, `planet`, `workshop_name`).
- **`Blueprint` (`blueprint.py`):** Engineering modification specifications:
  - Attributes: `blueprint_id`, `name`, `module_category`, `grade`, `modifiers`, `materials_required`.

### 2.7. `factions/` (BGS & Minor Factions)
- **`MinorFaction` (`faction.py`):** Background Simulation (BGS) entity:
  - Attributes: `name`, `allegiance`, `government`, `reputation`, `happiness`, `states`, `influence`.

### 2.8. `status/` (Cockpit Telemetry & Bitfields)
- **`StatusFlags` (`flags.py`):** Primary 32-bit integer bitfield flags (`IntFlag`):
  - Flags: `Docked`, `Landed`, `LandingGearDown`, `ShieldsUp`, `Supercruise`, `FlightAssistOff`, `HardpointsDeployed`, `InWing`, `LightsOn`, `CargoScoopDeployed`, `SilentRunning`, `ScoopingFuel`, `SrvHandbrake`, `SrvTurret`, `SrvUnderShip`, `SrvDriveAssist`, `FsdMassLocked`, `FsdCharging`, `FsdCooldown`, `LowFuel`, `OverHeating`, `HasLatLong`, `IsInDanger`, `BeingInterdicted`, `InMainShip`, `InFighter`, `InSrv`, `AnalysisMode`, `NightVision`, `AltReverse`.
- **`StatusFlags2` (`flags.py`):** Secondary 32-bit integer bitfield flags for Odyssey and extended vehicle states:
  - Flags: `OnFoot`, `InTaxi`, `InMulticrew`, `OnFootInStation`, `OnFootOnPlanet`, `AimDownSight`, `LowOxygen`, `LowHealth`, `Cold`, `Hot`, `VeryCold`, `VeryHot`, `GlideMode`, `OnFootInHangar`, `OnFootSocialSpace`, `OnFootExterior`, `BreathableAtmosphere`.
- **`TelemetryStatus` (`telemetry.py`):** Parsed snapshot model containing unpacked flags, cargo, pips `[sys, eng, wep]`, firegroup, gui_focus, fuel tanks, and coordinates.

### 2.9. `flight/` (Flight Mechanics & Hyperdrive Physics)
- **`JumpParameters` (`jump.py`):** Physics input parameter model for frame shift calculations:
  - Attributes: `fuel_multiplier`, `fuel_power`, `max_fuel_per_jump`, `drive_rating`, `drive_class`, `optimized_mass`.

### 2.10. `interop/` (In-Memory Interoperability Formats)
- **`TradeDangerousMarketRecord` (`trade_dangerous.py`):** Standardizes commodity rows into Trade Dangerous ASCII output lines.
- **`CoriolisSerializer` (`coriolis.py`):** Generates Coriolis.io loadout hashes and import payloads.

### 2.11. `odyssey/` (On-Foot Suits & Equipment)
- **`Suit` (`suit.py`):** On-foot suit specifications (Artemis, Maverick, Dominator, Flight Suit) with shield, battery, and mod slot capacities.

---

## 3. Events Domain Partitioning (`events/`)

Frontier Journal events are strictly categorized into 11 subpackages mapped directly to Chapters 2–13 of the Frontier Journal Manual:

| Package | Chapter Name | Event Count | Primary Domain Responsibility |
|:---|:---|:---:|:---|
| `startup/` | Chapter 2: Startup | 15 | Game initialization, commander state, loadouts, materials, cargo |
| `travel/` | Chapter 3: Travel | 19 | Supercruise, hyperspace jumps, docking, landings, liftoffs |
| `combat/` | Chapter 4: Combat | 16 | Interdictions, attacks, shields, bounties, hull integrity, kills |
| `exploration/` | Chapter 5: Exploration | 18 | Honking, FSS scans, DSS mapping, codex, organic samples, cartography |
| `trade/` | Chapter 6: Trade | 7 | Market transactions, mining refining, cargo collection, asteroid cracking |
| `station/` | Chapter 7: Station Services | 58 | Outfitting, shipyard, missions, engineering crafting, repair, refuel |
| `powerplay/` | Chapter 8: Powerplay | 12 | Power merits, vouchers, salary, delivery, defection, ranking |
| `squadrons/` | Chapter 9: Squadrons | 9 | Squadron creation, applications, promotions, shared bookmarks |
| `carrier/` | Chapter 10: Fleet Carriers | 15 | Carrier purchases, jumps, fuel deposits, trade orders, crew services |
| `odyssey/` | Chapter 11: Odyssey | 32 | On-foot suits, weapons, taxis, dropships, micro-resources, organic data |
| `other/` | Chapters 12 & 13: Other | 57 | Crew, wings, synthesis, voice comms, vehicle switches, music triggers |
| **Total** | | **258** | **Comprehensive Frontier Journal Event Coverage** |
