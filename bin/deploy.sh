#!/usr/bin/env bash
# bin/deploy.sh — Deploy the test project to test.sagecoders.com
# Usage: ./bin/deploy.sh [--no-rebuild] [--no-caddy]
set -euo pipefail

cd "$(dirname "$0")/.."
ROOT="$(pwd)"

REBUILD=1
CADDY=1
for arg in "$@"; do
  case "$arg" in
    --no-rebuild) REBUILD=0 ;;
    --no-caddy)   CADDY=0 ;;
    *) echo "Unknown arg: $arg" >&2; exit 1 ;;
  esac
done

PORT=3002
SUBDOMAIN=test
DOMAIN="${SUBDOMAIN}.sagecoders.com"

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  Deploying ${DOMAIN} → host:${PORT}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# 1. Build image
if [ "$REBUILD" -eq 1 ]; then
  echo "🔨 Building image..."
  sudo docker compose build
fi

# 2. Start containers
echo "🚀 Starting containers..."
sudo docker compose up -d

# 3. Wait for app to be ready
echo "⏳ Waiting for app on localhost:${PORT}..."
for i in {1..30}; do
  if curl -fsI -o /dev/null "http://localhost:${PORT}/up" 2>/dev/null; then
    echo "✅ App is up"
    break
  fi
  sleep 1
  if [ "$i" -eq 30 ]; then
    echo "❌ App didn't start in 30s. Check logs:"
    echo "   sudo docker compose logs app"
    exit 1
  fi
done

# 4. Caddy
if [ "$CADDY" -eq 1 ]; then
  echo "🌐 Configuring Caddy for ${DOMAIN}..."
  ~/.hermes/scripts/caddy-add.sh "$SUBDOMAIN" "$PORT"
fi

echo ""
echo "🎉 ${DOMAIN} deployed!"
echo "   App:   https://${DOMAIN}"
echo "   Admin: https://${DOMAIN}/admin"
echo "   Logs:  sudo docker compose logs -f app"
