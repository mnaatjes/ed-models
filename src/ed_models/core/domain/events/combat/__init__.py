"""Domain events for combat category."""

from ed_models.core.domain.events.combat.bounty import Bounty
from ed_models.core.domain.events.combat.cap_ship_bond import CapShipBond
from ed_models.core.domain.events.combat.died import Died
from ed_models.core.domain.events.combat.escape_interdiction import EscapeInterdiction
from ed_models.core.domain.events.combat.faction_kill_bond import FactionKillBond
from ed_models.core.domain.events.combat.fighter_destroyed import FighterDestroyed
from ed_models.core.domain.events.combat.heat_damage import HeatDamage
from ed_models.core.domain.events.combat.heat_warning import HeatWarning
from ed_models.core.domain.events.combat.hull_damage import HullDamage
from ed_models.core.domain.events.combat.interdicted import Interdicted
from ed_models.core.domain.events.combat.interdiction import Interdiction
from ed_models.core.domain.events.combat.pvp_kill import PVPKill
from ed_models.core.domain.events.combat.shield_state import ShieldState
from ed_models.core.domain.events.combat.ship_targeted import ShipTargeted
from ed_models.core.domain.events.combat.srv_destroyed import SRVDestroyed
from ed_models.core.domain.events.combat.under_attack import UnderAttack

__all__ = [
    "Bounty",
    "CapShipBond",
    "Died",
    "EscapeInterdiction",
    "FactionKillBond",
    "FighterDestroyed",
    "HeatDamage",
    "HeatWarning",
    "HullDamage",
    "Interdicted",
    "Interdiction",
    "PVPKill",
    "SRVDestroyed",
    "ShieldState",
    "ShipTargeted",
    "UnderAttack",
]
