"""Coriolis ship loadout serialization and URL hashing.

Governed by ADR 0001, ADR 0006, and SDD-007.
"""

from __future__ import annotations

import base64
import gzip
import io
import json
from typing import Any


def serialize_coriolis_loadout(loadout: dict[str, Any]) -> str:
    """Compresses and base64-encodes loadout JSON for Coriolis URL hash."""
    raw_json = json.dumps(
        loadout,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")

    if not raw_json:
        return ""

    out = io.BytesIO()
    with gzip.GzipFile(fileobj=out, mode="w") as f:
        f.write(raw_json)

    return base64.urlsafe_b64encode(out.getvalue()).decode().replace("=", "%3D")
