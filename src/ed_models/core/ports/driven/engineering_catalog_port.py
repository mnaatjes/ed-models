"""Driven port for engineering catalog providers."""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from ed_models.core.domain.engineering.blueprint import (
    EngineeringBlueprint,
    ExperimentalEffect,
)
from ed_models.core.domain.engineering.engineer import EngineerEntity
from ed_models.core.ports.base import DrivenPort


@runtime_checkable
class EngineeringCatalogProviderPort(DrivenPort, Protocol):
    """Port for querying pre-compiled engineering blueprints, effects, and engineers."""

    def get_blueprint(self, symbol: str) -> EngineeringBlueprint | None:
        """Retrieve blueprint specifications by canonical symbol."""
        ...

    def get_experimental_effect(self, symbol: str) -> ExperimentalEffect | None:
        """Retrieve experimental effect specifications by canonical symbol."""
        ...

    def get_engineer(self, engineer_id: int) -> EngineerEntity | None:
        """Retrieve engineer specifications by Frontier engineer ID."""
        ...

    def list_engineers(self) -> list[EngineerEntity]:
        """List all registered engineers."""
        ...
