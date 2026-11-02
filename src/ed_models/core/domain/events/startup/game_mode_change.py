"""Frontier Player Journal GameModeChange event model."""

from __future__ import annotations

from dataclasses import dataclass

from ed_models.core.domain.events.base import JournalEvent


@dataclass(slots=True, kw_only=True)
class GameModeChange(JournalEvent):
    """Written when game mode switches or loads.

    Example: {"timestamp": "2026-11-02T02:46:20Z", "event": "GameModeChange", "GameMode": "MainGame"}
    """

    GameMode: str = "MainGame"
