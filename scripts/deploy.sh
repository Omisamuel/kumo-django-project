#!/bin/bash
set -e # Exit immediately if a command exits with a non-zero status

# --- CONFIGURATION ---
# REPLACE THIS WITH YOUR ACTUAL GIT URL
REPO_URL="git@github.com:Omisamuel/kumo-django-project.git"

BRANCH="stage"
APP_DIR="/opt/omilabs_kumo_django"

REGISTRY_HOST="${REGISTRY_HOST:-ghcr.io}"
# ---------------------

echo "🚀 Starting deployment logic on $(hostname)..."

# Verify required tools are installed
echo "🔍 Checking prerequisites..."
command -v git >/dev/null 2>&1 || { echo "❌ git not found"; exit 1; }
command -v docker >/dev/null 2>&1 || { echo "❌ docker not found"; exit 1; }
echo "✅ Prerequisites verified"

# 1. Check if the directory exists
if [ ! -d "$APP_DIR/.git" ]; then
    echo "📂 Directory not found (or not a git repo). Cloning..."

    # Ensure parent dir exists
    if [ ! -d "$APP_DIR" ]; then
        # If the user doesn't own /opt, this might fail without sudo
        # But usually, you prep the server once manually: sudo chown $USER /opt
        mkdir -p "$APP_DIR"
    fi

    git clone -b "$BRANCH" "$REPO_URL" "$APP_DIR"
else
    echo "✓ Found existing repository."
fi

# 2. Go to the app directory
cd "$APP_DIR" || { echo "❌ Failed to enter directory $APP_DIR"; exit 1; }

# Registry login (optional, only if creds given)
if [ -n "${REGISTRY_USER:-}" ] && [ -n "${REGISTRY_PASSWORD:-}" ]; then
  echo "🔐 Logging into container registry $REGISTRY_HOST ..."
  echo "$REGISTRY_PASSWORD" | docker login "$REGISTRY_HOST" -u "$REGISTRY_USER" --password-stdin || {
    echo "❌ Docker login failed"; exit 1;
  }
else
  echo "ℹ️ REGISTRY_USER / REGISTRY_PASSWORD not set, skipping registry login."
fi


# 3. Fetch latest code and force reset
echo "🔄 Fetching latest code from git..."
git fetch origin
git reset --hard "origin/$BRANCH"

# 4. Docker Operations
echo "🐳 Pulling latest images..."
docker compose pull

echo "🚀 Restarting containers..."
docker compose up -d --remove-orphans

echo "🏥 Waiting for containers to stabilize..."
sleep 5

echo "📊 Verifying containers are running..."
if docker compose ps | grep -q "Up"; then
    echo "✅ Containers are healthy"
else
    echo "⚠️  Warning: Some containers may not be running"
    docker compose ps
fi

echo "🧹 Cleaning up unused images..."
docker image prune -f

echo "✅ Deployment Finished Successfully!"
echo ""
echo "📋 To monitor the deployment, run:"
echo "   docker compose logs -f"
echo ""
echo "📊 To check container status, run:"
echo "   docker compose ps"