"""Domain value object generated from kayahr/ed-journal."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True, kw_only=True)
class MicroResource:
    Name: str | None = None
    Name_Localised: str | None = None
    Category: str | None = None
    Count: int | None = None
