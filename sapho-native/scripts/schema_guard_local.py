#!/usr/bin/env python3
"""Shared JSON-schema validation helpers for firehose runtime scripts."""

from __future__ import annotations
import json
from pathlib import Path
from jsonschema import validate

ROOT = Path('/home/openclaw/.openclaw/workspace')


def load_schema(schema_path: str | Path) -> dict:
    p = Path(schema_path)
    if not p.is_absolute():
        p = ROOT / p
    return json.loads(p.read_text(encoding='utf-8'))


def validate_payload(payload: dict, schema_path: str | Path) -> None:
    schema = load_schema(schema_path)
    validate(instance=payload, schema=schema)
