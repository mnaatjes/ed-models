"""Commodity domain entity."""

from dataclasses import dataclass

from ed_models.core.domain.exceptions import DomainValidationError
from ed_models.core.domain.types.commodity_category import CommodityCategory


@dataclass(slots=True, kw_only=True)
class CommodityEntity:
    """Trade good and market commodity entity."""

    fdev_id: int
    symbol: str
    name: str
    category: CommodityCategory
    average_price: int
    is_rare: bool = False

    def __post_init__(self) -> None:
        """Validates commodity entity invariants."""
        if not self.symbol or not self.symbol.strip():
            raise DomainValidationError("Commodity symbol cannot be empty.")
