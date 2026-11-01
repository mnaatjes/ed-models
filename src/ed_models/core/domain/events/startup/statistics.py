"""Frontier Player Journal event model generated from kayahr/ed-journal."""

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class StatisticsBank_Account:
    """Nested value object for Statistics.Bank_Account."""

    Current_Wealth: int | float | None = None
    Spent_On_Ships: int | float | None = None
    Spent_On_Outfitting: int | float | None = None
    Spent_On_Repairs: int | float | None = None
    Spent_On_Fuel: float | None = None
    Spent_On_Ammo_Consumables: int | float | None = None
    Insurance_Claims: int | float | None = None
    Spent_On_Insurance: int | float | None = None
    Owned_Ship_Count: int | None = None
    Spent_On_Suits: int | float | None = None
    Spent_On_Weapons: int | float | None = None
    Spent_On_Suit_Consumables: int | float | None = None
    Suits_Owned: int | float | None = None
    Weapons_Owned: int | float | None = None
    Spent_On_Premium_Stock: int | float | None = None
    Premium_Stock_Bought: int | float | None = None


@dataclass(slots=True, kw_only=True)
class StatisticsCombat:
    """Nested value object for Statistics.Combat."""

    Bounties_Claimed: int | float | None = None
    Bounty_Hunting_Profit: int | None = None
    Combat_Bonds: int | float | None = None
    Combat_Bond_Profits: int | float | None = None
    Assassinations: int | float | None = None
    Assassination_Profits: int | float | None = None
    Highest_Single_Reward: int | None = None
    Skimmers_Killed: int | float | None = None
    OnFoot_Combat_Bonds: int | float | None = None
    OnFoot_Combat_Bonds_Profits: int | float | None = None
    OnFoot_Vehicles_Destroyed: int | float | None = None
    OnFoot_Ships_Destroyed: int | float | None = None
    Dropships_Taken: int | float | None = None
    Dropships_Booked: int | float | None = None
    Dropships_Cancelled: int | float | None = None
    ConflictZone_High: int | float | None = None
    ConflictZone_Medium: int | float | None = None
    ConflictZone_Low: int | float | None = None
    ConflictZone_Total: int | None = None
    ConflictZone_High_Wins: int | float | None = None
    ConflictZone_Medium_Wins: int | float | None = None
    ConflictZone_Low_Wins: int | float | None = None
    ConflictZone_Total_Wins: int | None = None
    Settlement_Defended: int | float | None = None
    Settlement_Conquered: int | float | None = None
    OnFoot_Skimmers_Killed: int | float | None = None
    OnFoot_Scavs_Killed: int | float | None = None


@dataclass(slots=True, kw_only=True)
class StatisticsCrime:
    """Nested value object for Statistics.Crime."""

    Fines: int | float | None = None
    Total_Fines: int | None = None
    Bounties_Received: int | float | None = None
    Total_Bounties: int | None = None
    Highest_Bounty: int | None = None
    Notoriety: int | float | None = None
    Malware_Uploaded: int | float | None = None
    Settlements_State_Shutdown: int | float | None = None
    Production_Sabotage: int | float | None = None
    Production_Theft: int | float | None = None
    Total_Murders: int | None = None
    Citizens_Murdered: int | float | None = None
    Omnipol_Murdered: int | float | None = None
    Guards_Murdered: int | float | None = None
    Data_Stolen: int | float | None = None
    Goods_Stolen: int | float | None = None
    Sample_Stolen: int | float | None = None
    Total_Stolen: int | None = None
    Turrets_Destroyed: int | float | None = None
    Turrets_Overloaded: int | float | None = None
    Turrets_Total: int | None = None
    Value_Stolen_StateChange: int | float | None = None
    Profiles_Cloned: int | float | None = None


@dataclass(slots=True, kw_only=True)
class StatisticsSmuggling:
    """Nested value object for Statistics.Smuggling."""

    Black_Markets_Traded_With: int | float | None = None
    Black_Markets_Profits: int | float | None = None
    Resources_Smuggled: int | float | None = None
    Average_Profit: int | float | None = None
    Highest_Single_Transaction: int | float | None = None


@dataclass(slots=True, kw_only=True)
class StatisticsTrading:
    """Nested value object for Statistics.Trading."""

    Markets_Traded_With: int | float | None = None
    Market_Profits: int | float | None = None
    Resources_Traded: int | float | None = None
    Average_Profit: int | float | None = None
    Highest_Single_Transaction: int | float | None = None
    Data_Sold: int | float | None = None
    Goods_Sold: int | float | None = None
    Assets_Sold: int | float | None = None


@dataclass(slots=True, kw_only=True)
class StatisticsMining:
    """Nested value object for Statistics.Mining."""

    Mining_Profits: int | float | None = None
    Quantity_Mined: int | float | None = None
    Materials_Collected: int | float | None = None


@dataclass(slots=True, kw_only=True)
class StatisticsExploration:
    """Nested value object for Statistics.Exploration."""

    Systems_Visited: int | float | None = None
    Exploration_Profits: int | float | None = None
    Planets_Scanned_To_Level_2: int | None = None
    Planets_Scanned_To_Level_3: int | None = None
    Highest_Payout: int | float | None = None
    Total_Hyperspace_Distance: int | None = None
    Total_Hyperspace_Jumps: int | None = None
    Greatest_Distance_From_Start: float | None = None
    Time_Played: int | float | None = None
    Efficient_Scans: int | float | None = None
    OnFoot_Distance_Travelled: float | None = None
    Shuttle_Journeys: int | float | None = None
    Shuttle_Distance_Travelled: float | None = None
    Spent_On_Shuttles: int | float | None = None
    First_Footfalls: int | float | None = None
    Planet_Footfalls: int | float | None = None
    Settlements_Visited: int | float | None = None


@dataclass(slots=True, kw_only=True)
class StatisticsPassengers:
    """Nested value object for Statistics.Passengers."""

    Passengers_Missions_Bulk: int | float | None = None
    Passengers_Missions_VIP: int | float | None = None
    Passengers_Missions_Delivered: int | float | None = None
    Passengers_Missions_Ejected: int | float | None = None
    Passengers_Missions_Accepted: int | float | None = None
    Passengers_Missions_Disgruntled: int | float | None = None


@dataclass(slots=True, kw_only=True)
class StatisticsSearch_And_Rescue:
    """Nested value object for Statistics.Search_And_Rescue."""

    SearchRescue_Traded: int | float | None = None
    SearchRescue_Profit: int | float | None = None
    SearchRescue_Count: int | None = None
    Salvage_Legal_POI: int | float | None = None
    Salvage_Legal_Settlements: int | float | None = None
    Salvage_Illegal_POI: int | float | None = None
    Salvage_Illegal_Settlements: int | float | None = None
    Maglocks_Opened: int | float | None = None
    Panels_Opened: int | float | None = None
    Settlements_State_FireOut: int | float | None = None
    Settlements_State_Reboot: int | float | None = None


@dataclass(slots=True, kw_only=True)
class StatisticsSquadron:
    """Nested value object for Statistics.Squadron."""

    Squadron_Bank_Credits_Deposited: int | float | None = None
    Squadron_Bank_Credits_Withdrawn: int | float | None = None
    Squadron_Bank_Commodities_Deposited_Num: int | float | None = None
    Squadron_Bank_Commodities_Deposited_Value: int | float | None = None
    Squadron_Bank_Commodities_Withdrawn_Num: int | float | None = None
    Squadron_Bank_Commodities_Withdrawn_Value: int | float | None = None
    Squadron_Bank_PersonalAssets_Deposited_Num: int | float | None = None
    Squadron_Bank_PersonalAssets_Deposited_Value: int | float | None = None
    Squadron_Bank_PersonalAssets_Withdrawn_Num: int | float | None = None
    Squadron_Bank_PersonalAssets_Withdrawn_Value: int | float | None = None
    Squadron_Bank_Ships_Deposited_Num: int | float | None = None
    Squadron_Bank_Ships_Deposited_Value: int | float | None = None
    Squadron_Leaderboard_aegis_highestcontribution: int | float | None = None
    Squadron_Leaderboard_bgs_highestcontribution: int | float | None = None
    Squadron_Leaderboard_bounty_highestcontribution: int | None = None
    Squadron_Leaderboard_colonisation_contribution_highestcontribution: int | float | None = None
    Squadron_Leaderboard_combat_highestcontribution: int | float | None = None
    Squadron_Leaderboard_cqc_highestcontribution: int | float | None = None
    Squadron_Leaderboard_exploration_highestcontribution: int | float | None = None
    Squadron_Leaderboard_mining_highestcontribution: int | float | None = None
    Squadron_Leaderboard_powerplay_highestcontribution: int | float | None = None
    Squadron_Leaderboard_trade_highestcontribution: int | float | None = None
    Squadron_Leaderboard_trade_illicit_highestcontribution: int | float | None = None
    Squadron_Leaderboard_podiums: int | float | None = None


@dataclass(slots=True, kw_only=True)
class StatisticsCrafting:
    """Nested value object for Statistics.Crafting."""

    Count_Of_Used_Engineers: int | None = None
    Recipes_Generated: int | float | None = None
    Recipes_Generated_Rank_1: int | None = None
    Recipes_Generated_Rank_2: int | None = None
    Recipes_Generated_Rank_3: int | None = None
    Recipes_Generated_Rank_4: int | None = None
    Recipes_Generated_Rank_5: int | None = None
    Suit_Mods_Applied: int | float | None = None
    Weapon_Mods_Applied: int | float | None = None
    Suits_Upgraded: int | float | None = None
    Weapons_Upgraded: int | float | None = None
    Suits_Upgraded_Full: int | float | None = None
    Weapons_Upgraded_Full: int | float | None = None
    Suit_Mods_Applied_Full: int | float | None = None
    Weapon_Mods_Applied_Full: int | float | None = None


@dataclass(slots=True, kw_only=True)
class StatisticsCrew:
    """Nested value object for Statistics.Crew."""

    NpcCrew_TotalWages: int | None = None
    NpcCrew_Hired: int | float | None = None
    NpcCrew_Fired: int | float | None = None
    NpcCrew_Died: int | float | None = None


@dataclass(slots=True, kw_only=True)
class StatisticsMulticrew:
    """Nested value object for Statistics.Multicrew."""

    Multicrew_Time_Total: int | None = None
    Multicrew_Credits_Total: int | None = None
    Multicrew_Gunner_Time_Total: int | None = None
    Multicrew_Fighter_Time_Total: int | None = None
    Multicrew_Fines_Total: int | None = None


@dataclass(slots=True, kw_only=True)
class StatisticsCQC:
    """Nested value object for Statistics.CQC."""

    CQC_Credits_Earned: int | float | None = None
    CQC_KD: int | float | None = None
    CQC_Kills: int | float | None = None
    CQC_Time_Played: int | float | None = None
    CQC_WL: int | float | None = None


@dataclass(slots=True, kw_only=True)
class StatisticsMaterial_Trader_Stats:
    """Nested value object for Statistics.Material_Trader_Stats."""

    Encoded_Materials_Traded: int | float | None = None
    Grade_1_Materials_Traded: int | float | None = None
    Grade_2_Materials_Traded: int | float | None = None
    Grade_3_Materials_Traded: int | float | None = None
    Grade_4_Materials_Traded: int | float | None = None
    Grade_5_Materials_Traded: int | float | None = None
    Materials_Traded: int | float | None = None
    Trades_Completed: int | float | None = None
    Raw_Materials_Traded: int | float | None = None
    Assets_Traded_In: int | float | None = None
    Assets_Traded_Out: int | float | None = None


@dataclass(slots=True, kw_only=True)
class StatisticsTG_ENCOUNTERS:
    """Nested value object for Statistics.TG_ENCOUNTERS."""

    TG_ENCOUNTER_KILLED: int | None = None
    TG_ENCOUNTER_IMPRINT: int | None = None
    TG_ENCOUNTER_TOTAL: int | None = None
    TG_ENCOUNTER_TOTAL_LAST_SYSTEM: str | None = None
    TG_ENCOUNTER_TOTAL_LAST_TIMESTAMP: str | None = None
    TG_ENCOUNTER_TOTAL_LAST_SHIP: str | None = None
    TG_SCOUT_COUNT: int | None = None


@dataclass(slots=True, kw_only=True)
class StatisticsFLEETCARRIER:
    """Nested value object for Statistics.FLEETCARRIER."""

    FLEETCARRIER_EXPORT_TOTAL: int | None = None
    FLEETCARRIER_IMPORT_TOTAL: int | None = None
    FLEETCARRIER_TRADEPROFIT_TOTAL: int | None = None
    FLEETCARRIER_TRADESPEND_TOTAL: int | None = None
    FLEETCARRIER_STOLENPROFIT_TOTAL: int | None = None
    FLEETCARRIER_STOLENSPEND_TOTAL: int | None = None
    FLEETCARRIER_DISTANCE_TRAVELLED: float | None = None
    FLEETCARRIER_TOTAL_JUMPS: int | None = None
    FLEETCARRIER_SHIPYARD_SOLD: int | float | None = None
    FLEETCARRIER_SHIPYARD_PROFIT: int | float | None = None
    FLEETCARRIER_OUTFITTING_SOLD: int | float | None = None
    FLEETCARRIER_OUTFITTING_PROFIT: int | float | None = None
    FLEETCARRIER_REARM_TOTAL: int | None = None
    FLEETCARRIER_REFUEL_TOTAL: int | None = None
    FLEETCARRIER_REFUEL_PROFIT: float | None = None
    FLEETCARRIER_REPAIRS_TOTAL: int | None = None
    FLEETCARRIER_VOUCHERS_REDEEMED: int | float | None = None
    FLEETCARRIER_VOUCHERS_PROFIT: int | float | None = None


@dataclass(slots=True, kw_only=True)
class StatisticsExobiology:
    """Nested value object for Statistics.Exobiology."""

    Organic_Genus_Encountered: int | None = None
    Organic_Species_Encountered: int | None = None
    Organic_Variant_Encountered: int | None = None
    Organic_Data_Profits: int | float | None = None
    Organic_Data: int | float | None = None
    First_Logged_Profits: int | float | None = None
    First_Logged: int | float | None = None
    Organic_Systems: int | float | None = None
    Organic_Planets: int | float | None = None
    Organic_Genus: int | float | None = None
    Organic_Species: int | float | None = None


@dataclass(slots=True, kw_only=True)
class Statistics(JournalEvent):
    """The information displayed in the statistics panel on the right side of the cockpit. Written at startup. Note: Times are in seconds."""

    Bank_Account: StatisticsBank_Account | None = None
    Combat: StatisticsCombat | None = None
    Crime: StatisticsCrime | None = None
    Smuggling: StatisticsSmuggling | None = None
    Trading: StatisticsTrading | None = None
    Mining: StatisticsMining | None = None
    Exploration: StatisticsExploration | None = None
    Passengers: StatisticsPassengers | None = None
    Search_And_Rescue: StatisticsSearch_And_Rescue | None = None
    Squadron: StatisticsSquadron | None = None
    Crafting: StatisticsCrafting | None = None
    Crew: StatisticsCrew | None = None
    Multicrew: StatisticsMulticrew | None = None
    CQC: StatisticsCQC | None = None
    Material_Trader_Stats: StatisticsMaterial_Trader_Stats | None = None
    TG_ENCOUNTERS: StatisticsTG_ENCOUNTERS | None = None
    FLEETCARRIER: StatisticsFLEETCARRIER | None = None
    Exobiology: StatisticsExobiology | None = None
