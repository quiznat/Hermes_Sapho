#!/usr/bin/env bash
set -euo pipefail

STAMP="$(date -u +%Y%m%dT%H%M%SZ)"
OUT_DIR="${1:-/home/hermes/backups}"
OUT_FILE="$OUT_DIR/hermes-state-$STAMP.tar.gz"

mkdir -p "$OUT_DIR"

cd /home/hermes

tar -czf "$OUT_FILE" \
  .hermes/auth.json \
  .hermes/memories \
  .hermes/sessions \
  .hermes/state.db* \
  sapho-native/state \
  sapho-native/public \
  sapho-native/articles \
  sapho-native/daily \
  sapho-native/discovery \
  sapho-native/queue \
  sapho-native/runtime

echo "$OUT_FILE"
