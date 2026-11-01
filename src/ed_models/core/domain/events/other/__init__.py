"""Domain events for other category."""

from ed_models.core.domain.events.other.afmu_repairs import AfmuRepairs
from ed_models.core.domain.events.other.approach_settlement import ApproachSettlement
from ed_models.core.domain.events.other.cargo_transfer import CargoTransfer
from ed_models.core.domain.events.other.change_crew_role import ChangeCrewRole
from ed_models.core.domain.events.other.cockpit_breached import CockpitBreached
from ed_models.core.domain.events.other.colonisation_construction_depot import (
    ColonisationConstructionDepot,
    ColonisationConstructionResource,
)
from ed_models.core.domain.events.other.colonisation_contribution import (
    ColonisationContribution,
    ColonisationContributionResource,
)
from ed_models.core.domain.events.other.commit_crime import CommitCrime
from ed_models.core.domain.events.other.continued import Continued
from ed_models.core.domain.events.other.crew_launch_fighter import CrewLaunchFighter
from ed_models.core.domain.events.other.crew_member_joins import CrewMemberJoins
from ed_models.core.domain.events.other.crew_member_quits import CrewMemberQuits
from ed_models.core.domain.events.other.crew_member_role_change import CrewMemberRoleChange
from ed_models.core.domain.events.other.crime_victim import CrimeVictim
from ed_models.core.domain.events.other.data_scanned import DataScanned
from ed_models.core.domain.events.other.datalink_scan import DatalinkScan
from ed_models.core.domain.events.other.datalink_voucher import DatalinkVoucher
from ed_models.core.domain.events.other.dock_fighter import DockFighter
from ed_models.core.domain.events.other.dock_srv import DockSRV
from ed_models.core.domain.events.other.end_crew_session import EndCrewSession
from ed_models.core.domain.events.other.fighter_rebuilt import FighterRebuilt
from ed_models.core.domain.events.other.friends import Friends
from ed_models.core.domain.events.other.fuel_scoop import FuelScoop
from ed_models.core.domain.events.other.jet_cone_boost import JetConeBoost
from ed_models.core.domain.events.other.jet_cone_damage import JetConeDamage
from ed_models.core.domain.events.other.join_a_crew import JoinACrew
from ed_models.core.domain.events.other.kick_crew_member import KickCrewMember
from ed_models.core.domain.events.other.launch_drone import LaunchDrone
from ed_models.core.domain.events.other.launch_fighter import LaunchFighter
from ed_models.core.domain.events.other.launch_srv import LaunchSRV
from ed_models.core.domain.events.other.module_info import ExtendedModuleInfo, ModuleInfo
from ed_models.core.domain.events.other.music import Music
from ed_models.core.domain.events.other.npc_crew_paid_wage import NpcCrewPaidWage
from ed_models.core.domain.events.other.npc_crew_rank import NpcCrewRank
from ed_models.core.domain.events.other.promotion import Promotion
from ed_models.core.domain.events.other.prospected_asteroid import ProspectedAsteroid
from ed_models.core.domain.events.other.quit_a_crew import QuitACrew
from ed_models.core.domain.events.other.reboot_repair import RebootRepair
from ed_models.core.domain.events.other.receive_text import ReceiveText
from ed_models.core.domain.events.other.repair_drone import RepairDrone
from ed_models.core.domain.events.other.reservoir_replenished import ReservoirReplenished
from ed_models.core.domain.events.other.resupply import Resupply
from ed_models.core.domain.events.other.resurrect import Resurrect
from ed_models.core.domain.events.other.scanned import Scanned
from ed_models.core.domain.events.other.self_destruct import SelfDestruct
from ed_models.core.domain.events.other.send_text import SendText
from ed_models.core.domain.events.other.shutdown import Shutdown
from ed_models.core.domain.events.other.status import LegalState, Status
from ed_models.core.domain.events.other.supercruise_destination_drop import (
    SupercruiseDestinationDrop,
)
from ed_models.core.domain.events.other.synthesis import Synthesis
from ed_models.core.domain.events.other.systems_shutdown import SystemsShutdown
from ed_models.core.domain.events.other.uss_drop import USSDrop
from ed_models.core.domain.events.other.vehicle_switch import VehicleSwitch
from ed_models.core.domain.events.other.wing_add import WingAdd
from ed_models.core.domain.events.other.wing_invite import WingInvite
from ed_models.core.domain.events.other.wing_join import WingJoin
from ed_models.core.domain.events.other.wing_leave import WingLeave

__all__ = [
    "AfmuRepairs",
    "ApproachSettlement",
    "CargoTransfer",
    "ChangeCrewRole",
    "CockpitBreached",
    "ColonisationConstructionDepot",
    "ColonisationConstructionResource",
    "ColonisationContribution",
    "ColonisationContributionResource",
    "CommitCrime",
    "Continued",
    "CrewLaunchFighter",
    "CrewMemberJoins",
    "CrewMemberQuits",
    "CrewMemberRoleChange",
    "CrimeVictim",
    "DataScanned",
    "DatalinkScan",
    "DatalinkVoucher",
    "DockFighter",
    "DockSRV",
    "EndCrewSession",
    "ExtendedModuleInfo",
    "FighterRebuilt",
    "Friends",
    "FuelScoop",
    "JetConeBoost",
    "JetConeDamage",
    "JoinACrew",
    "KickCrewMember",
    "LaunchDrone",
    "LaunchFighter",
    "LaunchSRV",
    "LegalState",
    "ModuleInfo",
    "Music",
    "NpcCrewPaidWage",
    "NpcCrewRank",
    "Promotion",
    "ProspectedAsteroid",
    "QuitACrew",
    "RebootRepair",
    "ReceiveText",
    "RepairDrone",
    "ReservoirReplenished",
    "Resupply",
    "Resurrect",
    "Scanned",
    "SelfDestruct",
    "SendText",
    "Shutdown",
    "Status",
    "SupercruiseDestinationDrop",
    "Synthesis",
    "SystemsShutdown",
    "USSDrop",
    "VehicleSwitch",
    "WingAdd",
    "WingInvite",
    "WingJoin",
    "WingLeave",
]
