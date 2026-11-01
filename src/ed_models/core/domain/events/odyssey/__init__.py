"""Domain events for odyssey category."""

from ed_models.core.domain.events.odyssey.backpack import Backpack, BackpackItem
from ed_models.core.domain.events.odyssey.backpack_change import BackpackChange, ChangedBackpackItem
from ed_models.core.domain.events.odyssey.book_dropship import BookDropship
from ed_models.core.domain.events.odyssey.book_taxi import BookTaxi
from ed_models.core.domain.events.odyssey.buy_micro_resources import (
    BuyMicroResources,
    NewBuyMicroResources,
    OldBuyMicroResources,
)
from ed_models.core.domain.events.odyssey.buy_suit import BuySuit
from ed_models.core.domain.events.odyssey.buy_weapon import BuyWeapon
from ed_models.core.domain.events.odyssey.cancel_dropship import CancelDropship
from ed_models.core.domain.events.odyssey.cancel_taxi import CancelTaxi
from ed_models.core.domain.events.odyssey.collect_items import CollectItems
from ed_models.core.domain.events.odyssey.create_suit_loadout import CreateSuitLoadout
from ed_models.core.domain.events.odyssey.delete_suit_loadout import DeleteSuitLoadout
from ed_models.core.domain.events.odyssey.disembark import Disembark
from ed_models.core.domain.events.odyssey.drop_items import DropItems
from ed_models.core.domain.events.odyssey.dropship_deploy import DropshipDeploy
from ed_models.core.domain.events.odyssey.embark import Embark
from ed_models.core.domain.events.odyssey.fc_materials import ExtendedFCMaterials, FCMaterials
from ed_models.core.domain.events.odyssey.loadout_equip_module import LoadoutEquipModule
from ed_models.core.domain.events.odyssey.rename_suit_loadout import RenameSuitLoadout
from ed_models.core.domain.events.odyssey.scan_organic import ScanOrganic
from ed_models.core.domain.events.odyssey.sell_micro_resources import SellMicroResources
from ed_models.core.domain.events.odyssey.sell_organic_data import SellOrganicData
from ed_models.core.domain.events.odyssey.sell_suit import SellSuit
from ed_models.core.domain.events.odyssey.sell_weapon import SellWeapon
from ed_models.core.domain.events.odyssey.ship_locker import ShipLocker, ShipLockerItem
from ed_models.core.domain.events.odyssey.suit_loadout import SuitLoadout
from ed_models.core.domain.events.odyssey.switch_suit_loadout import SwitchSuitLoadout
from ed_models.core.domain.events.odyssey.trade_micro_resources import TradeMicroResources
from ed_models.core.domain.events.odyssey.transfer_micro_resources import TransferMicroResources
from ed_models.core.domain.events.odyssey.upgrade_suit import UpgradeSuit
from ed_models.core.domain.events.odyssey.upgrade_weapon import UpgradeWeapon
from ed_models.core.domain.events.odyssey.use_consumable import UseConsumable

__all__ = [
    "Backpack",
    "BackpackChange",
    "BackpackItem",
    "BookDropship",
    "BookTaxi",
    "BuyMicroResources",
    "BuySuit",
    "BuyWeapon",
    "CancelDropship",
    "CancelTaxi",
    "ChangedBackpackItem",
    "CollectItems",
    "CreateSuitLoadout",
    "DeleteSuitLoadout",
    "Disembark",
    "DropItems",
    "DropshipDeploy",
    "Embark",
    "ExtendedFCMaterials",
    "FCMaterials",
    "LoadoutEquipModule",
    "NewBuyMicroResources",
    "OldBuyMicroResources",
    "RenameSuitLoadout",
    "ScanOrganic",
    "SellMicroResources",
    "SellOrganicData",
    "SellSuit",
    "SellWeapon",
    "ShipLocker",
    "ShipLockerItem",
    "SuitLoadout",
    "SwitchSuitLoadout",
    "TradeMicroResources",
    "TransferMicroResources",
    "UpgradeSuit",
    "UpgradeWeapon",
    "UseConsumable",
]
