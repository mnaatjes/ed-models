#!/usr/bin/env python3
"""TypeScript Model Extraction and Domain Transformation Pipeline.

Extracts event models and enumerations from `kayahr/ed-journal` TypeScript source files
and synthesizes pure Python domain models conforming to Hexagonal Architecture boundaries
and ADR 0001, ADR 0002, ADR 0003, and SDD-004.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path


@dataclass(slots=True)
class FieldSpec:
    name: str
    type_annotation: str
    is_optional: bool
    default_value: str | None = None
    docstring: str | None = None


@dataclass(slots=True)
class DataclassSpec:
    name: str
    category: str
    parent_class: str | None
    docstring: str | None
    fields: list[FieldSpec] = field(default_factory=list)
    nested_classes: list[DataclassSpec] = field(default_factory=list)


@dataclass(slots=True)
class EnumSpec:
    name: str
    docstring: str | None
    members: list[tuple[str, str]]  # (python_name, raw_value)


KNOWN_INT_FIELDS = {
    "count",
    "id",
    "marketid",
    "systemaddress",
    "bodyid",
    "suitid",
    "loadoutid",
    "weaponid",
    "missionid",
    "wondays",
    "tier",
    "rank",
    "level",
    "boostused",
    "total",
    "amount",
    "cost",
    "price",
    "bounty",
    "reward",
    "score",
    "progress",
    "size",
    "capacity",
    "wasted",
    "reputation",
    "remainingports",
    "population",
    "allocated",
    "standard",
}


def to_snake_case(name: str) -> str:
    """Convert PascalCase or camelCase to snake_case."""
    s1 = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", name)
    s2 = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s1)
    return s2.lower()


def clean_docstring(raw_doc: str | None) -> str | None:
    """Clean JSDoc comment into Python docstring."""
    if not raw_doc:
        return None
    lines = []
    for line in raw_doc.splitlines():
        line = re.sub(r"^\s*\* ? ?", "", line).strip()
        if line and not line.startswith("@"):
            lines.append(line)
    if not lines:
        return None
    text = " ".join(lines).strip()
    return text.replace('"""', "'''").replace('"', "'")


def extract_enums_from_ts(content: str) -> list[EnumSpec]:
    """Extract string union types from TypeScript type definitions."""
    enums: list[EnumSpec] = []
    pattern = r"(?:/\*\*([^*]*\*(?:[^/*][^*]*\*)*)/)?\s*export\s+type\s+(\w+)\s*=\s*([^;]+);"
    for match in re.finditer(pattern, content):
        doc = clean_docstring(match.group(1))
        name = match.group(2)
        body = match.group(3).strip()

        literals = re.findall(r'"([^"]+)"', body)
        if literals:
            members = []
            for lit in literals:
                safe_name = re.sub(r"[^a-zA-Z0-9_]", "_", lit)
                if safe_name[0].isdigit():
                    safe_name = f"VALUE_{safe_name}"
                member_id = re.sub(r"(?<!^)(?=[A-Z])", "_", safe_name).upper()
                member_id = re.sub(r"__+", "_", member_id).strip("_")
                if not member_id:
                    member_id = "UNKNOWN"
                members.append((member_id, lit))
            enums.append(EnumSpec(name=name, docstring=doc, members=members))
    return enums


def extract_interfaces(content: str) -> list[tuple[str, str | None, str | None, str]]:
    """Extract TypeScript interfaces: (name, extends, doc, body)."""
    pattern = (
        r"(?:/\*\*([^*]*\*(?:[^/*][^*]*\*)*)/)?\s*"
        r"export\s+interface\s+(\w+)(?:\s+extends\s+([^{]+))?\s*\{"
    )
    matches = list(re.finditer(pattern, content))
    interfaces = []
    for m in matches:
        start = m.end()
        depth = 1
        pos = start
        while pos < len(content) and depth > 0:
            if content[pos] == "{":
                depth += 1
            elif content[pos] == "}":
                depth -= 1
            pos += 1
        body = content[start : pos - 1]
        doc = clean_docstring(m.group(1))
        name = m.group(2)
        extends = m.group(3).strip() if m.group(3) else None
        interfaces.append((name, extends, doc, body))
    return interfaces


def parse_interface_statements(body: str) -> list[str]:
    """Split interface body into statements respecting nested brackets and braces."""
    cleaned = re.sub(r"//.*$", "", body, flags=re.MULTILINE)
    statements = []
    current: list[str] = []
    depth = 0
    in_comment = False
    i = 0
    while i < len(cleaned):
        char = cleaned[i]
        if cleaned[i : i + 2] == "/*":
            in_comment = True
            current.append(cleaned[i : i + 2])
            i += 2
            continue
        if cleaned[i : i + 2] == "*/" and in_comment:
            in_comment = False
            current.append(cleaned[i : i + 2])
            i += 2
            continue
        if in_comment:
            current.append(char)
            i += 1
            continue

        if char in "{[(":
            depth += 1
            current.append(char)
        elif char in "}])":
            depth -= 1
            current.append(char)
        elif char in (";", ",") and depth == 0:
            stmt = "".join(current).strip()
            if stmt:
                statements.append(stmt)
            current = []
        else:
            current.append(char)
        i += 1

    if current and "".join(current).strip():
        statements.append("".join(current).strip())

    return statements


class ModelGenerator:
    """Orchestrates parsing and synthesis of Python domain models."""

    def __init__(self, source_dir: Path, target_dir: Path) -> None:
        self.source_dir = source_dir
        self.target_dir = target_dir
        self.known_enums: set[str] = set()
        self.known_types: set[str] = set()
        self.type_to_module: dict[str, str] = {}
        self.declared_aliases: dict[str, str] = {}

    def scan_all_types(self) -> None:
        """First pass: Discover all exported types, enums, and interfaces across all files."""
        types_source = self.source_dir / "types"
        for ts_path in types_source.glob("*.ts"):
            content = ts_path.read_text(encoding="utf-8")
            enums = extract_enums_from_ts(content)
            for e in enums:
                self.known_enums.add(e.name)
                self.type_to_module[e.name] = f"ed_models.core.domain.types.{to_snake_case(e.name)}"

            ifaces = extract_interfaces(content)
            for name, _, _, _ in ifaces:
                self.known_types.add(name)
                self.type_to_module[name] = f"ed_models.core.domain.types.{to_snake_case(name)}"

        self.known_types.add("PowerState")
        self.type_to_module["PowerState"] = "ed_models.core.domain.types.power_state"

        for ts_path in self.source_dir.rglob("*.ts"):
            if "types" in ts_path.parts:
                continue
            content = ts_path.read_text(encoding="utf-8")
            enums = extract_enums_from_ts(content)
            cat_name = ts_path.parent.name
            mod_name = to_snake_case(ts_path.stem)
            for e in enums:
                self.known_enums.add(e.name)
                self.type_to_module[e.name] = f"ed_models.core.domain.events.{cat_name}.{mod_name}"

            ifaces = extract_interfaces(content)
            for name, _, _, _ in ifaces:
                self.known_types.add(name)
                self.type_to_module[name] = f"ed_models.core.domain.events.{cat_name}.{mod_name}"

    def map_ts_type(
        self,
        ts_type: str,
        field_name: str,
        parent_name: str,
        hoisted_classes: list[DataclassSpec],
    ) -> str:
        """Map TypeScript type annotation to Python type annotation."""
        ts_type = ts_type.strip()

        # Handle never types from TypeScript discriminated unions
        if ts_type == "never":
            return "typing.Any"

        # Handle StarPos coordinates
        if "number, number, number" in ts_type or (field_name == "StarPos" and "[" in ts_type):
            return "Coordinates3D"

        # Complex Scan Parents mapped types
        if "Parents" in field_name or "Exclude<BodyType" in ts_type:
            return "list[dict[str, int]]"

        # Normalize string | number
        if ts_type in ("string | number", "number | string"):
            return "str | int | float"

        # Handle GuiFocus in Status
        if ts_type == "GuiFocus":
            return "int"

        # Handle Array types
        array_match = re.match(r"^(?:Array<(.+)>|(.+)\[\])$", ts_type, flags=re.DOTALL)
        if array_match:
            inner_type = array_match.group(1) or array_match.group(2)
            mapped_inner = self.map_ts_type(
                inner_type.strip(), f"{field_name}Item", parent_name, hoisted_classes
            )
            return f"list[{mapped_inner}]"

        # Handle inline anonymous object interfaces: { ... }
        if ts_type.startswith("{") and ts_type.endswith("}"):
            nested_class_name = f"{parent_name}{field_name}"
            nested_body = ts_type[1:-1].strip()
            nested_fields = self.parse_fields(nested_body, nested_class_name, hoisted_classes)
            nested_spec = DataclassSpec(
                name=nested_class_name,
                category="",
                parent_class=None,
                docstring=f"Nested value object for {parent_name}.{field_name}.",
                fields=nested_fields,
            )
            hoisted_classes.append(nested_spec)
            return nested_class_name

        # Handle Record<string, T>
        record_match = re.match(r"^Record<string,\s*(.+)>$", ts_type, flags=re.DOTALL)
        if record_match:
            val_type = self.map_ts_type(
                record_match.group(1), f"{field_name}Value", parent_name, hoisted_classes
            )
            return f"dict[str, {val_type}]"

        # Primitives
        if ts_type in ("string", "string | null"):
            return "str"
        if ts_type == "boolean":
            return "bool"
        if ts_type in ("number", "number | bigint", "ID"):
            lower_name = field_name.lower()
            if any(term in lower_name for term in KNOWN_INT_FIELDS):
                return "int"
            if any(
                term in lower_name for term in ("dist", "fuel", "mass", "radius", "temp", "speed")
            ):
                return "float"
            return "int | float"

        # Handle any
        if ts_type == "any":
            return "typing.Any"

        # Engineer progress subtype specialization: retain EngineerProgressState
        if field_name == "Progress" and parent_name in ("LockedEngineer", "UnlockedEngineer"):
            return "EngineerProgressState"

        # Known enums & types
        if ts_type in self.known_enums or ts_type in self.known_types:
            return ts_type

        # String union literal inline
        if '"' in ts_type and "|" in ts_type:
            return "str"

        # Literal string inline (e.g. Progress: "Unlocked")
        if re.match(r'^"[^"]+"$', ts_type):
            return "str"

        clean_name = re.sub(r"[^a-zA-Z0-9_]", "", ts_type)
        return clean_name if clean_name else "typing.Any"

    def parse_fields(
        self,
        body: str,
        parent_name: str,
        hoisted_classes: list[DataclassSpec],
    ) -> list[FieldSpec]:
        """Parse field specifications from interface body."""
        statements = parse_interface_statements(body)
        fields: list[FieldSpec] = []

        for stmt in statements:
            doc_match = re.search(r"/\*\*([^*]*\*(?:[^/*][^*]*\*)*)/\s*", stmt)
            doc = clean_docstring(doc_match.group(1)) if doc_match else None
            code = re.sub(r"/\*\*([^*]*\*(?:[^/*][^*]*\*)*)/\s*", "", stmt).strip()

            m = re.match(r"^(\w+)(\??)\s*:\s*(.+)$", code, flags=re.DOTALL)
            if not m:
                continue

            fname = m.group(1)
            is_opt = m.group(2) == "?"
            raw_type = m.group(3).strip()

            if fname in ("timestamp", "event") and parent_name not in (
                "ConflictFaction",
                "MicroResource",
            ):
                continue

            py_type = self.map_ts_type(raw_type, fname, parent_name, hoisted_classes)
            type_ann = f"{py_type} | None"
            default_val = "None"

            fields.append(
                FieldSpec(
                    name=fname,
                    type_annotation=type_ann,
                    is_optional=is_opt,
                    default_value=default_val,
                    docstring=doc,
                )
            )

        return fields

    def generate_types(self) -> None:
        """Process and generate types from types/ directory."""
        types_source = self.source_dir / "types"
        types_target = self.target_dir / "types"
        types_target.mkdir(parents=True, exist_ok=True)

        all_types: list[str] = []

        for ts_path in types_source.glob("*.ts"):
            content = ts_path.read_text(encoding="utf-8")
            enums = extract_enums_from_ts(content)

            for enum_spec in enums:
                snake_name = to_snake_case(enum_spec.name)
                all_types.append(enum_spec.name)
                out_path = types_target / f"{snake_name}.py"

                code = [
                    '"""Domain enumeration authority generated from kayahr/ed-journal."""\n',
                    "from enum import StrEnum\n\n\n",
                    f"class {enum_spec.name}(StrEnum):",
                ]
                if enum_spec.docstring:
                    code.append(f'    """{enum_spec.docstring}"""\n')

                for member_name, raw_val in enum_spec.members:
                    code.append(f'    {member_name} = "{raw_val}"')
                code.append("\n")

                out_path.write_text("\n".join(code), encoding="utf-8")

            ifaces = extract_interfaces(content)
            for name, _extends, doc, body in ifaces:
                snake_name = to_snake_case(name)
                all_types.append(name)
                out_path = types_target / f"{snake_name}.py"

                hoisted: list[DataclassSpec] = []
                fields = self.parse_fields(body, name, hoisted)

                lines = [
                    '"""Domain value object generated from kayahr/ed-journal."""\n',
                    "from dataclasses import dataclass\n\n\n",
                    "@dataclass(frozen=True, slots=True, kw_only=True)",
                    f"class {name}:",
                ]
                if doc:
                    lines.append(f'    """{doc}"""\n')
                for f in fields:
                    lines.append(f"    {f.name}: {f.type_annotation} = {f.default_value}")
                lines.append("\n")

                out_path.write_text("\n".join(lines), encoding="utf-8")

        all_types.append("PowerState")
        power_state_path = types_target / "power_state.py"
        power_state_path.write_text(
            '"""Combined PowerState enumeration."""\n\n'
            "from ed_models.core.domain.types.power_state1 import PowerState1\n"
            "from ed_models.core.domain.types.power_state2 import PowerState2\n\n\n"
            "type PowerState = PowerState1 | PowerState2\n",
            encoding="utf-8",
        )

        init_lines = ['"""Domain types and enumerations."""\n']
        for t in sorted(set(all_types)):
            s = to_snake_case(t)
            init_lines.append(f"from ed_models.core.domain.types.{s} import {t}")
        init_lines.append(f"\n__all__ = {sorted(set(all_types))!r}\n")
        (types_target / "__init__.py").write_text("\n".join(init_lines), encoding="utf-8")

    def generate_events(self) -> None:
        """Process and generate all event categories."""
        events_target = self.target_dir / "events"
        events_target.mkdir(parents=True, exist_ok=True)

        categories = [d for d in self.source_dir.iterdir() if d.is_dir() and d.name != "types"]

        master_exports: dict[str, list[str]] = {}

        for category_dir in sorted(categories, key=lambda d: d.name):
            cat_name = category_dir.name
            cat_target = events_target / cat_name
            cat_target.mkdir(parents=True, exist_ok=True)
            cat_events: list[str] = []
            symbol_to_file: dict[str, str] = {}

            for ts_path in sorted(category_dir.glob("*.ts")):
                content = ts_path.read_text(encoding="utf-8")
                enums = extract_enums_from_ts(content)
                ifaces = extract_interfaces(content)

                if not ifaces and not enums:
                    continue

                out_file_name = to_snake_case(ts_path.stem)
                out_path = cat_target / f"{out_file_name}.py"
                current_module = f"ed_models.core.domain.events.{cat_name}.{out_file_name}"

                imports = {
                    "from dataclasses import dataclass",
                    "from ed_models.core.domain.events.base import JournalEvent",
                    "import typing",
                }
                type_imports = set()

                enum_lines = []
                for enum_spec in enums:
                    imports.add("from enum import StrEnum")
                    enum_lines.append(f"\nclass {enum_spec.name}(StrEnum):")
                    if enum_spec.docstring:
                        enum_lines.append(f'    """{enum_spec.docstring}"""\n')
                    for member_name, raw_val in enum_spec.members:
                        enum_lines.append(f'    {member_name} = "{raw_val}"')
                    enum_lines.append("\n")
                    cat_events.append(enum_spec.name)
                    symbol_to_file[enum_spec.name] = out_file_name

                union_alias_lines = []
                for m in re.finditer(r"export\s+type\s+(\w+)\s*=\s*([^;]+);", content):
                    alias_name = m.group(1)
                    raw_val = m.group(2).strip()
                    if "|" in raw_val and not re.search(r'"[^"]+"', raw_val):
                        py_types = [
                            re.sub(r"[^a-zA-Z0-9_]", "", part.strip())
                            for part in raw_val.split("|")
                        ]
                        py_union = " | ".join(t for t in py_types if t)
                        union_alias_lines.append(f"type {alias_name} = {py_union}\n")
                        cat_events.append(alias_name)
                        symbol_to_file[alias_name] = out_file_name

                file_classes: list[DataclassSpec] = []

                for iface_name, extends, doc, body in ifaces:
                    hoisted: list[DataclassSpec] = []
                    fields = self.parse_fields(body, iface_name, hoisted)

                    parent = None
                    if extends and "JournalEvent" in extends:
                        parent = "JournalEvent"
                    elif extends:
                        parent_clean = re.sub(r"[^a-zA-Z0-9_]", "", extends.split("<")[0])
                        parent = parent_clean
                    elif iface_name.endswith("Event") or not hoisted:
                        parent = "JournalEvent"

                    cat_events.append(iface_name)
                    symbol_to_file[iface_name] = out_file_name

                    spec = DataclassSpec(
                        name=iface_name,
                        category=cat_name,
                        parent_class=parent,
                        docstring=doc,
                        fields=fields,
                        nested_classes=hoisted,
                    )
                    file_classes.append(spec)

                all_declared_in_file = {s.name for s in file_classes} | {e.name for e in enums}
                for s in file_classes:
                    all_declared_in_file.update(n.name for n in s.nested_classes)

                for spec in file_classes:
                    all_specs = spec.nested_classes + [spec]
                    for s in all_specs:
                        for f in s.fields:
                            for type_name, mod_path in self.type_to_module.items():
                                if type_name in all_declared_in_file:
                                    continue
                                if re.search(r"\b" + type_name + r"\b", f.type_annotation):
                                    if mod_path != current_module:
                                        type_imports.add(f"from {mod_path} import {type_name}")
                            if "Coordinates3D" in f.type_annotation:
                                imports.add(
                                    "from ed_models.core.domain.spatial.coordinates import Coordinates3D"
                                )

                lines = [
                    '"""Frontier Player Journal event model generated from kayahr/ed-journal."""\n',
                    "\n".join(sorted(imports)),
                ]
                if type_imports:
                    lines.append("\n" + "\n".join(sorted(type_imports)))
                lines.append("\n\n")

                if enum_lines:
                    lines.extend(enum_lines)

                if union_alias_lines:
                    lines.extend(union_alias_lines)
                    lines.append("\n")

                for spec in file_classes:
                    for nested in spec.nested_classes:
                        lines.append("@dataclass(slots=True, kw_only=True)")
                        lines.append(f"class {nested.name}:")
                        if nested.docstring:
                            lines.append(f'    """{nested.docstring}"""\n')
                        if not nested.fields:
                            lines.append("    pass\n")
                        for f in nested.fields:
                            lines.append(f"    {f.name}: {f.type_annotation} = {f.default_value}")
                        lines.append("\n\n")

                    lines.append("@dataclass(slots=True, kw_only=True)")
                    parent_decl = f"({spec.parent_class})" if spec.parent_class else ""
                    lines.append(f"class {spec.name}{parent_decl}:")
                    if spec.docstring:
                        lines.append(f'    """{spec.docstring}"""\n')
                    if not spec.fields:
                        lines.append("    pass\n")
                    for f in spec.fields:
                        lines.append(f"    {f.name}: {f.type_annotation} = {f.default_value}")
                    lines.append("\n")

                out_path.write_text("\n".join(lines), encoding="utf-8")

            cat_init = [f'"""Domain events for {cat_name} category."""\n']
            unique_events = sorted(set(cat_events))
            master_exports[cat_name] = unique_events
            for ev in unique_events:
                mod_file = symbol_to_file.get(ev, to_snake_case(ev))
                cat_init.append(
                    f"from ed_models.core.domain.events.{cat_name}.{mod_file} import {ev}"
                )
            cat_init.append(f"\n__all__ = {unique_events!r}\n")
            (cat_target / "__init__.py").write_text("\n".join(cat_init), encoding="utf-8")

        # Master events/__init__.py with explicit named imports
        master_init = [
            '"""Frontier Player Journal events master registry."""\n',
            "from ed_models.core.domain.events.base import JournalEvent",
        ]
        all_master_symbols = ["JournalEvent"]
        for cat in sorted([d.name for d in categories]):
            symbols = master_exports.get(cat, [])
            all_master_symbols.extend(symbols)
            master_init.append(
                f"from ed_models.core.domain.events.{cat} import ({', '.join(symbols)})"
            )
        master_init.append(f"\n__all__ = {sorted(set(all_master_symbols))!r}\n")
        (events_target / "__init__.py").write_text("\n".join(master_init), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Extract ed-journal TypeScript models into Python dataclasses."
    )
    parser.add_argument(
        "--source",
        type=Path,
        default=Path("/home/michael/src/github.com/kayahr/ed-journal/src/main/events"),
        help="Path to ed-journal src/main/events directory",
    )
    parser.add_argument(
        "--target",
        type=Path,
        default=Path("src/ed_models/core/domain"),
        help="Path to target core/domain directory",
    )
    parser.add_argument("--clean", action="store_true", help="Clean generated directories")
    args = parser.parse_args()

    if not args.source.exists():
        print(f"Error: Source directory {args.source} does not exist.", file=sys.stderr)
        sys.exit(1)

    print(f"[EXTRACT] Reading TypeScript definitions from {args.source}...")
    generator = ModelGenerator(args.source, args.target)

    print("[EXTRACT] Scanning all type definitions across codebase...")
    generator.scan_all_types()

    print("[EXTRACT] Generating domain types and enumerations...")
    generator.generate_types()

    print("[EXTRACT] Generating journal event dataclasses across categories...")
    generator.generate_events()

    print("[EXTRACT] Extraction and domain transformation complete.")


if __name__ == "__main__":
    main()
