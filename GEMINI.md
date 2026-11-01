# Context & Developer Environment Guide: `ed-models`

## 1. Project Overview & Architecture

`ed-models` is a pure Hexagonal Architecture (Ports and Adapters) domain library providing strongly typed game entities, physics calculators, token normalizers, static catalogs, and journal/status event models for *Elite Dangerous* software fleet integrations (`ed-telemetry`, `ed-connector`, `ed-router`, `ed-schema`).

It contains **zero network transport, zero filesystem I/O, and zero third-party wire protocol dependencies**. It is packaged strictly as an offline library with driving facade ports and in-memory static catalog driven adapters.

### Architectural Layout (`src/ed_models/`)

- `src/ed_models/core/`: The pure internal hexagonal application core.
  - `core/domain/`: Pure domain entities, value objects, and business exceptions (`DomainError`).
    - `domain/types/`: Discrete string enums (`StrEnum`) and bitfields (`IntFlag`) mapped to Frontier specification primitives (`StarType`, `PadSize`, `Allegiance`, `StatusFlags`).
    - `domain/spatial/`: Pure 3D coordinates (`Coordinates3D` with frozen slots) and star system models.
    - `domain/bodies/`: Stellar and planetary physics models (`StarBody`, `PlanetaryBody`).
    - `domain/ships/`: Hull specifications, module ratings, slot layouts, and loadout mechanics.
    - `domain/commodities/`: Canonical trade goods, rare allocations, and category taxonomies.
    - `domain/factions/`: Minor faction presence and BGS political states.
    - `domain/status/`: Cockpit telemetry unpackers (`StatusFlags`, `StatusFlags2`).
    - `domain/interop/`: Pure in-memory serializers (`TradeDangerousMarketRecord`, Coriolis JSON).
    - `domain/events/`: Polymorphic event hierarchy partitioned 1:1 across official Frontier Journal Chapters 2–13 (`startup`, `travel`, `combat`, `exploration`, `trade`, `station`, `powerplay`, `squadrons`, `carrier`, `odyssey`, `other`). All events declare `kw_only=True`.
  - `core/ports/`: Abstract boundary contracts (`typing.Protocol` with `@typing.runtime_checkable`).
    - `core/ports/driving/`: Primary entry ports (`CatalogLookupPort`, `NormalizationPort`, `EventParserPort`, `FlightMechanicsPort`).
    - `core/ports/driven/`: Secondary catalog provider ports (`ShipCatalogProviderPort`, `ModuleCatalogProviderPort`, `CommodityCatalogProviderPort`).
  - `core/use_cases/`: Pure, stateless interactors orchestrating domain lookups and calculations (`LookupShipUseCase`, `NormalizeTokenUseCase`, `ParseJournalEventUseCase`, `CalculateJumpRangeUseCase`).
- `src/ed_models/adapters/`: Technology-specific adapters implementing ports.
  - `adapters/driving/`: Unified facade adapter (`EliteDomainFacade`) implementing driving ports.
  - `adapters/driven/static_catalogs/`: Pre-compiled in-memory lookup adapters ($O(1)$) implementing driven catalog ports.
- `src/ed_models/bootstrap/`: Composition root (`container.py`) wiring driven adapters and use cases into `EliteDomainFacade`.

---

## 2. Python Virtual Environment & Tooling Paths

The project uses a local virtual environment located at `.venv/` in the repository root:

* **Python Interpreter:** `.venv/bin/python`
* **Pytest Test Runner:** `.venv/bin/pytest`
* **Ruff (Linter & Formatter):** `.venv/bin/ruff`
* **MyPy Type Checker:** `.venv/bin/mypy`
* **Import Linter:** `.venv/bin/lint-imports`
* **Bump-My-Version:** `.venv/bin/bump-my-version`

> [!IMPORTANT]
> Always execute commands and verification tools directly through `.venv/bin/<tool>` or via `uv run`.

---

## 3. Standard Verification Commands

All modifications must pass Tier 2 Quality Gates before PR submission or merging:

```bash
# 1. Complete Quality Verification Suite:
.venv/bin/python scripts/verify.py

# 2. Architectural Boundary Gate (verifies Hexagonal isolation invariants):
.venv/bin/pytest tests/architecture/test_boundaries.py
.venv/bin/lint-imports

# 3. Targeted Unit Test Execution:
.venv/bin/pytest tests/unit/

# 4. Ruff Linter & Formatter:
.venv/bin/ruff check .
.venv/bin/ruff format --check .

# 5. Static Type Checking:
.venv/bin/mypy src/ tests/
```

---

## 4. Architectural Rules & Governance Invariants

Governed by [ADR 0001](file:///home/michael/src/github.com/mnaatjes/ed-models/architecture/adr/0001_ed_models_core_game_logic_and_catalog_architecture.md), [SDD-002](file:///home/michael/src/github.com/mnaatjes/ed-models/architecture/designs/SDD-002_ed_models_repository_scaffold_and_hexagonal_setup.md), and `.gemini/rules/hexagonal_invariants.md`:

1. **HEXA-TRUTH-01 (Pure Core Domain Isolation):** Never import adapters, databases, HTTP clients, or external frameworks inside `src/ed_models/core/domain/`.
2. **HEXA-TRUTH-02 (Inward Dependency Direction):** Outer layers depend on inner layers (`adapters` $\rightarrow$ `use_cases` $\rightarrow$ `ports` $\rightarrow$ `domain`). Inner layers must never import outer adapters.
3. **HEXA-TRUTH-03 (Port Abstraction):** All ports in `core/ports/` must be abstract `typing.Protocol` classes without concrete implementation bodies.
4. **HEXA-TRUTH-04 (DTO Boundary Purity):** Port method parameters and return types must be pure immutable value objects or primitives.
5. **HEXA-TRUTH-07 (Business Exception Sovereignty):** All domain exceptions must inherit from `DomainError` in `core/domain/exceptions.py`.
6. **HEXA-TRUTH-14 (Stateless Interactors):** Use cases must be strictly stateless interactors; never mutate instance attributes outside `__init__`.
7. **ADR 0001 Invariant (Zero I/O):** Never perform network I/O (`requests`, `httpx`), disk tailing/watching (`ed-telemetry`), or JSON schema validation rules (`ed-schema`) within `ed-models`.

---

## 5. Agent Conversation & Dialogue Directives

To optimize for operator cognitive load and token efficiency during interactive sessions:

* **ADHD-Friendly Formatting:** Lead directly with actionable findings or next steps. Avoid conversational preambles, introductory filler, and redundant narrative summaries.
* **Structured Bullet Points:** Present options, status lists, and file impacts as clean, grouped bullet points.
* **Token Efficiency:** Keep chat explanations concise and high-signal; avoid repeating code diffs or re-summarizing unchanged file contents.
* **Cognitive Load Reduction:** Clearly separate "what was done" from the "immediate single next action". Break multi-phase tasks into small, explicit increments.
