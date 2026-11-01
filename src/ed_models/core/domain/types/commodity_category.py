"""Commodity category classification."""

from enum import StrEnum


class CommodityCategory(StrEnum):
    """Canonical trade commodity categories."""

    CHEMICALS = "Chemicals"
    CONSUMER_ITEMS = "ConsumerItems"
    FOODS = "Foods"
    INDUSTRIAL_MATERIALS = "IndustrialMaterials"
    LEGAL_DRUGS = "LegalDrugs"
    MACHINERY = "Machinery"
    MEDICINES = "Medicines"
    METALS = "Metals"
    MINERALS = "Minerals"
    SALVAGE = "Salvage"
    SLAVES = "Slaves"
    TECHNOLOGY = "Technology"
    TEXTILES = "Textiles"
    WASTE = "Waste"
    WEAPONS = "Weapons"
    NON_MARKETABLE = "NonMarketable"
    UNKNOWN = "Unknown"
