"""Polymorphic Journal event registry and deserialization engine.

Governed by ADR 0001, ADR 0007, and SDD-008.
"""

from __future__ import annotations

from typing import Any

import ed_models.core.domain.events as ev_module
from ed_models.core.domain.events.base import JournalEvent

_EVENT_REGISTRY: dict[str, type[JournalEvent]] = {}

for attr_name in dir(ev_module):
    if attr_name.startswith("_"):
        continue
    candidate = getattr(ev_module, attr_name)
    if (
        isinstance(candidate, type)
        and issubclass(candidate, JournalEvent)
        and candidate is not JournalEvent
    ):
        # Register both exact class name and lowercase (e.g. "fsdjump" -> FsdJump)
        _EVENT_REGISTRY[candidate.__name__.lower()] = candidate


def parse_journal_event(payload: dict[str, Any]) -> JournalEvent:
    """Instantiates a strongly typed JournalEvent from a raw Frontier event dictionary.

    If the event type is uncataloged or missing, falls back to a base JournalEvent instance
    to prevent deserialization crashes during Frontier game patches.
    """
    event_name = str(payload.get("event", "JournalEvent"))
    lookup_key = event_name.lower().replace("_", "")

    cls = _EVENT_REGISTRY.get(lookup_key, _EVENT_REGISTRY.get(event_name.lower(), JournalEvent))

    # Match attributes to class slots / fields
    fields: dict[str, Any] = {}
    valid_keys = getattr(cls, "__annotations__", {})

    for k, v in payload.items():
        if k in valid_keys:
            fields[k] = v

    if "timestamp" not in fields and "timestamp" in payload:
        fields["timestamp"] = payload["timestamp"]
    elif "timestamp" not in fields:
        fields["timestamp"] = ""

    if "event" not in fields:
        fields["event"] = event_name

    return cls(**fields)
