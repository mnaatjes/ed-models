"""Domain events for station category."""

from ed_models.core.domain.events.station.buy_ammo import BuyAmmo
from ed_models.core.domain.events.station.buy_drones import BuyDrones
from ed_models.core.domain.events.station.cargo_depot import CargoDepot
from ed_models.core.domain.events.station.community_goal import CommunityGoal
from ed_models.core.domain.events.station.community_goal_discard import CommunityGoalDiscard
from ed_models.core.domain.events.station.community_goal_join import CommunityGoalJoin
from ed_models.core.domain.events.station.community_goal_reward import CommunityGoalReward
from ed_models.core.domain.events.station.crew_assign import CrewAssign
from ed_models.core.domain.events.station.crew_fire import CrewFire
from ed_models.core.domain.events.station.crew_hire import CrewHire
from ed_models.core.domain.events.station.engineer_apply import EngineerApply
from ed_models.core.domain.events.station.engineer_contribution import EngineerContribution
from ed_models.core.domain.events.station.engineer_craft import EngineerCraft
from ed_models.core.domain.events.station.engineer_legacy_convert import EngineerLegacyConvert
from ed_models.core.domain.events.station.engineer_progress import (
    Engineer,
    EngineerBase,
    EngineerProgress,
    EngineerProgressState,
    LockedEngineer,
    UnlockedEngineer,
)
from ed_models.core.domain.events.station.fetch_remote_module import FetchRemoteModule
from ed_models.core.domain.events.station.market import ExtendedMarket, Market
from ed_models.core.domain.events.station.mass_module_store import MassModuleStore
from ed_models.core.domain.events.station.material_trade import MaterialTrade
from ed_models.core.domain.events.station.mission_abandoned import MissionAbandoned
from ed_models.core.domain.events.station.mission_accepted import MissionAccepted
from ed_models.core.domain.events.station.mission_completed import MissionCompleted
from ed_models.core.domain.events.station.mission_failed import MissionFailed
from ed_models.core.domain.events.station.mission_redirected import MissionRedirected
from ed_models.core.domain.events.station.module_buy import ModuleBuy
from ed_models.core.domain.events.station.module_buy_and_store import ModuleBuyAndStore
from ed_models.core.domain.events.station.module_retrieve import ModuleRetrieve
from ed_models.core.domain.events.station.module_sell import ModuleSell
from ed_models.core.domain.events.station.module_sell_remote import ModuleSellRemote
from ed_models.core.domain.events.station.module_store import ModuleStore
from ed_models.core.domain.events.station.module_swap import ModuleSwap
from ed_models.core.domain.events.station.outfitting import ExtendedOutfitting, Outfitting
from ed_models.core.domain.events.station.pay_bounties import PayBounties
from ed_models.core.domain.events.station.pay_fines import PayFines
from ed_models.core.domain.events.station.pay_legacy_fines import PayLegacyFines
from ed_models.core.domain.events.station.redeem_voucher import RedeemVoucher
from ed_models.core.domain.events.station.refuel_all import RefuelAll
from ed_models.core.domain.events.station.refuel_partial import RefuelPartial
from ed_models.core.domain.events.station.repair import Repair
from ed_models.core.domain.events.station.repair_all import RepairAll
from ed_models.core.domain.events.station.restock_vehicle import RestockVehicle
from ed_models.core.domain.events.station.scientific_research import ScientificResearch
from ed_models.core.domain.events.station.search_and_rescue import SearchAndRescue
from ed_models.core.domain.events.station.sell_drones import SellDrones
from ed_models.core.domain.events.station.sell_ship_on_rebuy import SellShipOnRebuy
from ed_models.core.domain.events.station.set_user_ship_name import SetUserShipName
from ed_models.core.domain.events.station.ship_redeemed import ShipRedeemed
from ed_models.core.domain.events.station.shipyard import ExtendedShipyard, Shipyard
from ed_models.core.domain.events.station.shipyard_bank_deposit import ShipyardBankDeposit
from ed_models.core.domain.events.station.shipyard_buy import ShipyardBuy
from ed_models.core.domain.events.station.shipyard_new import ShipyardNew
from ed_models.core.domain.events.station.shipyard_redeem import ShipyardRedeem
from ed_models.core.domain.events.station.shipyard_sell import ShipyardSell
from ed_models.core.domain.events.station.shipyard_swap import ShipyardSwap
from ed_models.core.domain.events.station.shipyard_transfer import ShipyardTransfer
from ed_models.core.domain.events.station.stored_modules import StoredModules
from ed_models.core.domain.events.station.stored_ships import StoredShips
from ed_models.core.domain.events.station.technology_broker import TechnologyBroker

__all__ = [
    "BuyAmmo",
    "BuyDrones",
    "CargoDepot",
    "CommunityGoal",
    "CommunityGoalDiscard",
    "CommunityGoalJoin",
    "CommunityGoalReward",
    "CrewAssign",
    "CrewFire",
    "CrewHire",
    "Engineer",
    "EngineerApply",
    "EngineerBase",
    "EngineerContribution",
    "EngineerCraft",
    "EngineerLegacyConvert",
    "EngineerProgress",
    "EngineerProgressState",
    "ExtendedMarket",
    "ExtendedOutfitting",
    "ExtendedShipyard",
    "FetchRemoteModule",
    "LockedEngineer",
    "Market",
    "MassModuleStore",
    "MaterialTrade",
    "MissionAbandoned",
    "MissionAccepted",
    "MissionCompleted",
    "MissionFailed",
    "MissionRedirected",
    "ModuleBuy",
    "ModuleBuyAndStore",
    "ModuleRetrieve",
    "ModuleSell",
    "ModuleSellRemote",
    "ModuleStore",
    "ModuleSwap",
    "Outfitting",
    "PayBounties",
    "PayFines",
    "PayLegacyFines",
    "RedeemVoucher",
    "RefuelAll",
    "RefuelPartial",
    "Repair",
    "RepairAll",
    "RestockVehicle",
    "ScientificResearch",
    "SearchAndRescue",
    "SellDrones",
    "SellShipOnRebuy",
    "SetUserShipName",
    "ShipRedeemed",
    "Shipyard",
    "ShipyardBankDeposit",
    "ShipyardBuy",
    "ShipyardNew",
    "ShipyardRedeem",
    "ShipyardSell",
    "ShipyardSwap",
    "ShipyardTransfer",
    "StoredModules",
    "StoredShips",
    "TechnologyBroker",
    "UnlockedEngineer",
]
