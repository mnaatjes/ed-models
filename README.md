# ed-models

[![Version](https://img.shields.io/badge/version-v0.1.0-blue.svg)](CHANGELOG.md)

Pure hexagonal domain models, game-logic calculators, and static catalogs for Elite Dangerous fleet integrations

## Architectural Governance
This service is architected in accordance with Hexagonal Architecture (Ports and Adapters).
* Core Domain logic resides in `src/ed_models/core/` with ZERO external infrastructure dependencies.
* Architectural boundaries are enforced deterministically via `import-linter` and `pytest-archon`.

## Quickstart

Run quality verification gates:
```bash
uv run python scripts/verify.py
```
