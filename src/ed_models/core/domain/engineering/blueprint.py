"""Engineering blueprint and experimental effect domain entities.

Governed by ADR 0005 and SDD-006.
"""

from dataclasses import dataclass

from ed_models.core.domain.exceptions import DomainValidationError


@dataclass(slots=True, kw_only=True)
class RecipeIngredient:
    """Ingredient required for an engineering modification or experimental effect."""

    material_symbol: str
    name: str
    count: int

    def __post_init__(self) -> None:
        if not self.material_symbol or not self.material_symbol.strip():
            raise DomainValidationError("Material symbol cannot be empty.")
        if self.count <= 0:
            raise DomainValidationError(f"Ingredient count must be positive: {self.count}")


@dataclass(slots=True, kw_only=True)
class AttributeModifier:
    """Attribute modification rule within an engineering recipe."""

    attribute_name: str
    is_positive: bool
    multiplier: float

    def __post_init__(self) -> None:
        if not self.attribute_name or not self.attribute_name.strip():
            raise DomainValidationError("Attribute name cannot be empty.")


@dataclass(slots=True, kw_only=True)
class BlueprintGrade:
    """Grade specification (1 to 5) of an engineering blueprint."""

    grade: int
    ingredients: tuple[RecipeIngredient, ...]
    modifiers: tuple[AttributeModifier, ...]

    def __post_init__(self) -> None:
        if not 1 <= self.grade <= 5:
            raise DomainValidationError(f"Blueprint grade must be between 1 and 5: {self.grade}")
        if not self.ingredients:
            raise DomainValidationError("Blueprint grade must specify at least one ingredient.")


@dataclass(slots=True, kw_only=True)
class EngineeringBlueprint:
    """Engineering modification blueprint."""

    symbol: str
    name: str
    target_modules: tuple[str, ...]
    grades: dict[int, BlueprintGrade]

    def __post_init__(self) -> None:
        if not self.symbol or not self.symbol.strip():
            raise DomainValidationError("Blueprint symbol cannot be empty.")
        if not self.name or not self.name.strip():
            raise DomainValidationError("Blueprint name cannot be empty.")
        if not self.grades:
            raise DomainValidationError("Blueprint must declare at least one grade.")


@dataclass(slots=True, kw_only=True)
class ExperimentalEffect:
    """Experimental modification effect."""

    symbol: str
    name: str
    target_modules: tuple[str, ...]
    ingredients: tuple[RecipeIngredient, ...]
    modifiers: tuple[AttributeModifier, ...]

    def __post_init__(self) -> None:
        if not self.symbol or not self.symbol.strip():
            raise DomainValidationError("Experimental effect symbol cannot be empty.")
        if not self.name or not self.name.strip():
            raise DomainValidationError("Experimental effect name cannot be empty.")
