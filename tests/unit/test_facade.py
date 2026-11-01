"""Unit tests for EliteDomainFacade driving adapter.

Governed by ADR 0007, SDD-008, and hexagonal quality gates.
"""

from __future__ import annotations

from ed_models.bootstrap.container import Container
from ed_models.core.domain.flight.jump import JumpCalculationParameters
from ed_models.core.domain.interop.trade_dangerous import TradeDangerousMarketRecord
from ed_models.core.domain.status.flags import StatusFlags, StatusFlags2


def test_facade_static_catalog_lookups() -> None:
    """Verifies that EliteDomainFacade resolves ships, modules, commodities, and blueprints."""
    container = Container()
    facade = container.build_elite_domain_facade()

    # Ship lookup
    ship = facade.get_ship("anaconda")
    assert ship is not None
    assert ship.name == "Anaconda"

    all_ships = facade.list_ships()
    assert len(all_ships) > 0

    # Module lookup
    module = facade.get_module_by_symbol("int_hyperdrive_size5_class5")
    assert module is not None

    # Commodity lookup
    commodity = facade.get_commodity_by_symbol("grain")
    assert commodity is not None
    assert commodity.name == "Grain"

    # Blueprint lookup
    blueprint = facade.get_blueprint("fsd_longrange")
    assert blueprint is not None
    assert blueprint.name == "Increased Range"

    # Engineer lookup
    engineers = facade.list_engineers()
    assert len(engineers) >= 2


def test_facade_token_normalization_and_telemetry() -> None:
    """Verifies token normalization and telemetry construction via facade."""
    container = Container()
    facade = container.build_elite_domain_facade()

    # Commodity token normalization
    norm = facade.normalize_commodity("$grain_name;")
    assert norm is not None
    assert norm.symbol.lower() == "grain"

    # Telemetry parsing
    telemetry = facade.parse_telemetry(
        flags=int(StatusFlags.DOCKED | StatusFlags.LIGHTS_ON),
        flags2=int(StatusFlags2.ON_FOOT),
        fuel_main=16.0,
        cargo=2,
    )
    assert telemetry.is_docked is True
    assert telemetry.is_on_foot is True
    assert telemetry.cargo == 2

    # Journal event parsing
    event = facade.parse_journal_event(
        {
            "timestamp": "2026-11-01T23:30:00Z",
            "event": "FSDJump",
            "StarSystem": "Sol",
            "SystemAddress": 128000000,
            "JumpDist": 42.15,
        }
    )
    assert event.event == "FSDJump"
    assert getattr(event, "StarSystem", None) == "Sol"
    assert getattr(event, "JumpDist", None) == 42.15


def test_facade_pure_math_and_interop() -> None:
    """Verifies FSD jump calculation and interop serialization via facade."""
    container = Container()
    facade = container.build_elite_domain_facade()

    # Jump range calculation
    params = JumpCalculationParameters(
        fsd_optimal_mass=2700.0,
        fsd_max_fuel_per_jump=8.0,
        fsd_fuel_multiplier=0.012,
        fsd_fuel_power=2.75,
        unladen_mass=450.0,
        cargo_mass=0.0,
        fuel_mass=32.0,
    )
    result = facade.calculate_jump_range(params)
    assert result.current_jump_range_ly > 40.0

    # Trade Dangerous format
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
    td_output = facade.format_trade_dangerous([record], "2026-11-01 23:25:00")
    assert "@ System: Deciat" in td_output

    # Coriolis serialization
    coriolis_str = facade.serialize_coriolis({"ship": "Python", "components": {}})
    assert isinstance(coriolis_str, str)
    assert len(coriolis_str) > 0
