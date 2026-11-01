# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Authored ADR 0002 defining domain scope boundaries, contract elasticity, and inheritance rules.
- Authored SDD-003 and implemented 4-tier automated boundary enforcement gates (Pre-commit, AST Pytest suite, Import Linter, and CI).
- Authored ADR 0003 establishing offline TypeScript AST extraction pipeline for harvesting `kayahr/ed-journal`.
- Authored SDD-004 specifying extraction pipeline architecture, lexical parsing rules, hoister logic, and code synthesis.
- Implemented `scripts/extract_models.py` build-time code generator in `scripts/`.
- Synthesized base `JournalEvent` (`slots=True`, `kw_only=True`) and 284+ journal event models partitioned across 11 category packages (`carrier`, `combat`, `exploration`, `odyssey`, `other`, `powerplay`, `squadrons`, `startup`, `station`, `trade`, `travel`).
- Synthesized universal domain types (`StarType`, `BodyType`, `StationService`, `StationType`, `PlanetClass`, `PowerState1`, `PowerState2`, `PowerState`) and pure spatial vector `Coordinates3D`.

## [0.1.0] - 2026-11-01

### Added
- Initial project scaffolding initialized from `python-hexagonal-template`.
- Hexagonal architecture directory topology (`core/domain/`, `core/ports/`, `core/use_cases/`, `adapters/`, `bootstrap/`).
- Architecture documentation tree aligned with Unified Process disciplines (`risk/`, `use-cases/`, `adr/`, `designs/`, `rfcs/`, `api/`).
- Migrated foundational ADR 0001 (Pure Domain Architecture, Catalogs & Facade) and SDD-002 (Repository Scaffold and Setup).
- Architectural layer boundary tests enforcing `HEXA-TRUTH-01` through `HEXA-TRUTH-17`.

<!-- Conversation ID: 35fc6240-8370-4435-b40a-d95be1c01c97 -->
