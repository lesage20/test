#!/usr/bin/env bash
# bin/logs.sh — Tail logs from the test stack
# Usage: ./bin/logs.sh [service]
set -euo pipefail
cd "$(dirname "$0")/.."

SERVICE="${1:-}"
if [ -n "$SERVICE" ]; then
  exec sudo docker compose logs -f "$SERVICE"
else
  exec sudo docker compose logs -f
fi
