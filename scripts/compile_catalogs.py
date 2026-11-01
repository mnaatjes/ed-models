#!/usr/bin/env python3
"""Offline Static Catalog Harvester and Code Synthesizer.

Extracts authoritative ship hulls, outfitting modules, and market commodities from
EDCD/EDDI and EDMarketConnector, synthesizing pure in-memory driven adapters in
src/ed_models/adapters/driven/static_catalogs/.

Governed by ADR 0001, ADR 0004, and SDD-005.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

MANUFACTURER_MAP = {
    "FaulconDeLacy": "Manufacturer.FAULCON_DE_LACY",
    "CoreDynamics": "Manufacturer.CORE_DYNAMICS",
    "Gutamaya": "Manufacturer.GUTAMAYA",
    "LakonSpaceways": "Manufacturer.LAKON_SPACEWAYS",
    "SaudKruger": "Manufacturer.SAUD_KRUGER",
    "ZorgonPeterson": "Manufacturer.ZORGON_PETERSON",
}

PAD_SIZE_MAP = {
    "Small": "PadSize.SMALL",
    "Medium": "PadSize.MEDIUM",
    "Large": "PadSize.LARGE",
    "None": "PadSize.NONE",
}

CATEGORY_MAP = {
    "Chemicals": "CommodityCategory.CHEMICALS",
    "ConsumerItems": "CommodityCategory.CONSUMER_ITEMS",
    "Foods": "CommodityCategory.FOODS",
    "IndustrialMaterials": "CommodityCategory.INDUSTRIAL_MATERIALS",
    "LegalDrugs": "CommodityCategory.LEGAL_DRUGS",
    "Machinery": "CommodityCategory.MACHINERY",
    "Medicines": "CommodityCategory.MEDICINES",
    "Metals": "CommodityCategory.METALS",
    "Minerals": "CommodityCategory.MINERALS",
    "Salvage": "CommodityCategory.SALVAGE",
    "Slaves": "CommodityCategory.SLAVES",
    "Technology": "CommodityCategory.TECHNOLOGY",
    "Textiles": "CommodityCategory.TEXTILES",
    "Waste": "CommodityCategory.WASTE",
    "Weapons": "CommodityCategory.WEAPONS",
    "NonMarketable": "CommodityCategory.NON_MARKETABLE",
    "Unknown": "CommodityCategory.UNKNOWN",
}


def compile_ships(eddi_dir: Path, edmc_dir: Path, target_dir: Path) -> None:
    """Compile ships catalog from EDDI ShipDefinitions.cs and EDMC ships.json."""
    ships_json_path = edmc_dir / "ships.json"
    edmc_masses: dict[str, float] = {}
    if ships_json_path.exists():
        with ships_json_path.open(encoding="utf-8") as f:
            data = json.load(f)
            for k, v in data.items():
                edmc_masses[k.lower()] = float(v.get("hullMass", 0.0))

    eddi_ships_path = eddi_dir / "DataDefinitions" / "ShipDefinitions.cs"
    content = eddi_ships_path.read_text(encoding="utf-8")

    lines = [
        '"""Pre-compiled in-memory static ship catalog adapter."""\n',
        "from ed_models.core.domain.ships.hull import ShipHull",
        "from ed_models.core.domain.types.manufacturer import Manufacturer",
        "from ed_models.core.domain.types.pad_size import PadSize",
        "from ed_models.core.ports.driven.ship_catalog_port import ShipCatalogProviderPort\n\n",
        "_HULLS: dict[str, ShipHull] = {",
    ]

    hulls_emitted = 0
    for line in content.splitlines():
        if "new(" not in line:
            continue
        m = re.search(r'new\(\s*"([^"]+)",\s*Manufacturer\.(\w+),\s*"([^"]+)"', line)
        pad = re.search(r"LandingPadSize\.(\w+)", line)
        reserve = re.search(r"([\d\.]+)M\s*\)", line)
        if not m:
            continue

        model = m.group(1)
        mfr_raw = m.group(2)
        name = m.group(3)
        pad_raw = pad.group(1) if pad else "None"
        reserve_fuel = float(reserve.group(1)) if reserve else 0.0

        mfr_py = MANUFACTURER_MAP.get(mfr_raw, "Manufacturer.UNKNOWN")
        pad_py = PAD_SIZE_MAP.get(pad_raw, "PadSize.NONE")
        hull_mass = edmc_masses.get(model.lower(), edmc_masses.get(name.lower(), 100.0))

        lines.append(f'    "{model.lower()}": ShipHull(')
        lines.append(f'        model="{model}",')
        lines.append(f'        name="{name}",')
        lines.append(f"        manufacturer={mfr_py},")
        lines.append(f"        pad_size={pad_py},")
        lines.append(f"        hull_mass={hull_mass},")
        lines.append(f"        reserve_fuel_capacity={reserve_fuel},")
        lines.append("    ),")
        hulls_emitted += 1

    lines.append("}\n\n")

    lines.extend(
        [
            "class StaticShipCatalogAdapter(ShipCatalogProviderPort):",
            '    """In-memory static catalog provider for ship hull specifications."""\n',
            "    def get_hull_spec(self, model: str) -> ShipHull | None:",
            "        return _HULLS.get(model.lower())\n",
            "    def list_all_hulls(self) -> list[ShipHull]:",
            "        return list(_HULLS.values())\n",
        ]
    )

    out_file = target_dir / "ships_catalog.py"
    out_file.write_text("\n".join(lines), encoding="utf-8")
    print(f"[SHIPS] Synthesized {hulls_emitted} ship hulls into {out_file.name}")


def compile_commodities(eddi_dir: Path, target_dir: Path) -> None:
    """Compile commodity catalog from EDDI CommodityDefinition.cs."""
    comm_path = eddi_dir / "DataDefinitions" / "CommodityDefinition.cs"
    content = comm_path.read_text(encoding="utf-8")

    pattern = (
        r"public\s+static\s+readonly\s+CommodityDefinition\s+\w+\s*=\s*"
        r'new\(\s*(\d+|null)\s*,\s*"([^"]+)"\s*,\s*(\w+)\s*,\s*([\d\.\-]+)\s*,\s*(true|false)'
    )
    matches = list(re.finditer(pattern, content))

    lines = [
        '"""Pre-compiled in-memory static commodity catalog adapter."""\n',
        "from ed_models.core.domain.commodities.commodity import CommodityEntity",
        "from ed_models.core.domain.types.commodity_category import CommodityCategory",
        "from ed_models.core.ports.driven.commodity_catalog_port import CommodityCatalogProviderPort\n\n",
        "_COMMODITIES_BY_ID: dict[int, CommodityEntity] = {}",
        "_COMMODITIES_BY_SYMBOL: dict[str, CommodityEntity] = {\n",
    ]

    emitted = 0
    for m in matches:
        raw_id = m.group(1)
        symbol = m.group(2)
        category_raw = m.group(3)
        avg_price = int(float(m.group(4)))
        is_rare = m.group(5) == "true"

        fdev_id = int(raw_id) if raw_id != "null" else 0
        cat_py = CATEGORY_MAP.get(category_raw, "CommodityCategory.UNKNOWN")

        lines.append(f'    "{symbol.lower()}": CommodityEntity(')
        lines.append(f"        fdev_id={fdev_id},")
        lines.append(f'        symbol="{symbol}",')
        lines.append(f'        name="{symbol}",')
        lines.append(f"        category={cat_py},")
        lines.append(f"        average_price={avg_price},")
        lines.append(f"        is_rare={is_rare},")
        lines.append("    ),")
        emitted += 1

    lines.append("}\n")
    lines.append(
        "for _c in _COMMODITIES_BY_SYMBOL.values():\n"
        "    if _c.fdev_id > 0:\n"
        "        _COMMODITIES_BY_ID[_c.fdev_id] = _c\n\n"
    )

    lines.extend(
        [
            "class StaticCommodityCatalogAdapter(CommodityCatalogProviderPort):",
            '    """In-memory static catalog provider for commodities with safe fallback."""\n',
            "    def get_commodity_by_id(self, fdev_id: int) -> CommodityEntity | None:",
            "        return _COMMODITIES_BY_ID.get(fdev_id)\n",
            "    def get_commodity_by_symbol(self, symbol: str) -> CommodityEntity | None:",
            "        clean_symbol = symbol.lower().strip('$').rstrip(';').removesuffix('_name')",
            "        match = _COMMODITIES_BY_SYMBOL.get(clean_symbol)",
            "        if match is not None:",
            "            return match",
            "        # Fallback for uncataloged items to prevent crashes (RISK-02)",
            "        return CommodityEntity(",
            "            fdev_id=0,",
            "            symbol=symbol,",
            "            name=symbol,",
            "            category=CommodityCategory.UNKNOWN,",
            "            average_price=0,",
            "        )\n",
        ]
    )

    out_file = target_dir / "commodities_catalog.py"
    out_file.write_text("\n".join(lines), encoding="utf-8")
    print(f"[COMMODITIES] Synthesized {emitted} commodities into {out_file.name}")


def compile_modules(eddi_dir: Path, edmc_dir: Path, target_dir: Path) -> None:
    """Compile modules catalog from EDDI ModuleDefinitions.cs and EDMC modules.json."""
    edmc_path = edmc_dir / "modules.json"
    edmc_masses: dict[str, float] = {}
    if edmc_path.exists():
        with edmc_path.open(encoding="utf-8") as f:
            data = json.load(f)
            for k, v in data.items():
                edmc_masses[k.lower()] = float(v.get("mass", 0.0))

    eddi_path = eddi_dir / "DataDefinitions" / "ModuleDefinitions.cs"
    content = eddi_path.read_text(encoding="utf-8")

    pattern = r'new\(\s*"([^"]+)",\s*"([^"]+)",\s*(\d+),\s*"([^"]+)",\s*([\d\-]+)'
    matches = list(re.finditer(pattern, content))

    lines = [
        '"""Pre-compiled in-memory static outfitting module catalog adapter."""\n',
        "from ed_models.core.domain.ships.module import ShipModule",
        "from ed_models.core.ports.driven.module_catalog_port import ModuleCatalogProviderPort\n\n",
        "_MODULES_BY_SYMBOL: dict[str, ShipModule] = {\n",
    ]

    emitted = 0
    for idx, m in enumerate(matches, start=128000000):
        symbol = m.group(1)
        name = m.group(2)
        class_num = int(m.group(3))
        rating = m.group(4)
        mass = edmc_masses.get(symbol.lower(), 0.0)

        lines.append(f'    "{symbol.lower()}": ShipModule(')
        lines.append(f"        fdev_id={idx},")
        lines.append(f'        symbol="{symbol}",')
        lines.append(f'        name="{name}",')
        lines.append(f"        class_num={class_num},")
        lines.append(f'        rating="{rating}",')
        lines.append(f"        mass={mass},")
        lines.append("    ),")
        emitted += 1

    lines.append("}\n")
    lines.append(
        "_MODULES_BY_ID: dict[int, ShipModule] = {_m.fdev_id: _m for _m in _MODULES_BY_SYMBOL.values()}\n\n"
    )

    lines.extend(
        [
            "class StaticModuleCatalogAdapter(ModuleCatalogProviderPort):",
            '    """In-memory static catalog provider for outfitting modules."""\n',
            "    def get_module_by_id(self, fdev_id: int) -> ShipModule | None:",
            "        return _MODULES_BY_ID.get(fdev_id)\n",
            "    def get_module_by_symbol(self, symbol: str) -> ShipModule | None:",
            "        return _MODULES_BY_SYMBOL.get(symbol.lower())\n",
        ]
    )

    out_file = target_dir / "modules_catalog.py"
    out_file.write_text("\n".join(lines), encoding="utf-8")
    print(f"[MODULES] Synthesized {emitted} outfitting modules into {out_file.name}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Compile static catalogs for ed-models.")
    parser.add_argument(
        "--eddi",
        type=Path,
        default=Path("/home/michael/src/github.com/EDCD/EDDI"),
        help="Path to EDDI repository",
    )
    parser.add_argument(
        "--edmc",
        type=Path,
        default=Path("/home/michael/src/github.com/mnaatjes/EDMarketConnector"),
        help="Path to EDMarketConnector repository",
    )
    parser.add_argument(
        "--target",
        type=Path,
        default=Path("src/ed_models/adapters/driven/static_catalogs"),
        help="Target adapters directory",
    )
    args = parser.parse_args()

    args.target.mkdir(parents=True, exist_ok=True)
    compile_ships(args.eddi, args.edmc, args.target)
    compile_commodities(args.eddi, args.target)
    compile_modules(args.eddi, args.edmc, args.target)

    init_file = args.target / "__init__.py"
    init_file.write_text(
        '"""Driven static catalog adapters."""\n\n'
        "from ed_models.adapters.driven.static_catalogs.commodities_catalog import StaticCommodityCatalogAdapter\n"
        "from ed_models.adapters.driven.static_catalogs.modules_catalog import StaticModuleCatalogAdapter\n"
        "from ed_models.adapters.driven.static_catalogs.ships_catalog import StaticShipCatalogAdapter\n\n"
        "__all__ = [\n"
        '    "StaticCommodityCatalogAdapter",\n'
        '    "StaticModuleCatalogAdapter",\n'
        '    "StaticShipCatalogAdapter",\n'
        "]\n",
        encoding="utf-8",
    )
    print(f"[COMPLETED] Static catalogs compiled into {args.target}")


if __name__ == "__main__":
    main()
