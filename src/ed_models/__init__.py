"""Package root for ed-models.

Exposes the unified driving facade, container composition root, and primary domain models.
Governed by ADR 0001, ADR 0002, ADR 0007, and SDD-008.
"""

from __future__ import annotations

from ed_models.adapters.driving.facade import EliteDomainFacade
from ed_models.bootstrap.container import Container
from ed_models.core.domain.bodies import PlanetaryBody, StarBody
from ed_models.core.domain.commodities.commodity import CommodityEntity
from ed_models.core.domain.engineering import (
    EngineerEntity,
    EngineeringBlueprint,
    ExperimentalEffect,
)
from ed_models.core.domain.events.base import JournalEvent
from ed_models.core.domain.events.parser import parse_journal_event
from ed_models.core.domain.factions.faction import (
    Allegiance,
    FactionState,
    Government,
    MinorFactionPresence,
)
from ed_models.core.domain.flight.jump import (
    JumpCalculationParameters,
    JumpCalculationResult,
)
from ed_models.core.domain.interop.coriolis import serialize_coriolis_loadout
from ed_models.core.domain.interop.trade_dangerous import (
    TradeDangerousMarketRecord,
    format_trade_dangerous,
)
from ed_models.core.domain.odyssey.suit import SuitEntity, SuitWeaponEntity
from ed_models.core.domain.ships.hull import ShipHull
from ed_models.core.domain.ships.module import ShipModule
from ed_models.core.domain.spatial.coordinates import Coordinates3D
from ed_models.core.domain.status.flags import StatusFlags, StatusFlags2
from ed_models.core.domain.status.telemetry import StatusTelemetry

__version__ = "0.1.0"


def create_domain_facade() -> EliteDomainFacade:
    """Convenience factory function instantiating the unified EliteDomainFacade."""
    container = Container()
    return container.build_elite_domain_facade()


__all__ = [
    # Facade & Factory
    "EliteDomainFacade",
    "create_domain_facade",
    "Container",
    # Ships & Modules
    "ShipHull",
    "ShipModule",
    # Commodities
    "CommodityEntity",
    # Telemetry & Status
    "StatusFlags",
    "StatusFlags2",
    "StatusTelemetry",
    # Celestial Bodies
    "Coordinates3D",
    "StarBody",
    "PlanetaryBody",
    # Engineering
    "EngineeringBlueprint",
    "ExperimentalEffect",
    "EngineerEntity",
    # Odyssey
    "SuitEntity",
    "SuitWeaponEntity",
    # Flight Physics
    "JumpCalculationParameters",
    "JumpCalculationResult",
    # Factions & BGS
    "MinorFactionPresence",
    "Allegiance",
    "Government",
    "FactionState",
    # Interop Formats
    "TradeDangerousMarketRecord",
    "format_trade_dangerous",
    "serialize_coriolis_loadout",
    # Journal Events
    "JournalEvent",
    "parse_journal_event",
]
