#!/bin/bash
# Run with 'chmod +x start.sh' (On first run)
# Then `./start.sh` every time afterwards

# ── 1. Check if Docker is installed ──────────────────────────────────────────
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker and try again."
    echo "   Download it here: https://www.docker.com/products/docker-desktop"
    exit 1
fi

# ── 2. Check if Docker daemon is running ─────────────────────────────────────
if ! docker info &> /dev/null; then
    echo "❌ Docker is installed but not running. Please start Docker Desktop and try again."
    exit 1
fi

# ── 3. Check if .env file exists ─────────────────────────────────────────────
if [ ! -f .env ]; then
    echo "❌ No .env file found."
    echo "   Copy .env.example to .env and fill in your API keys:"
    echo ""
    echo "   cp .env.example .env"
    echo ""
    echo "   Required keys:"
    echo "   - NASA_API_KEY"
    echo "   - RAWG_API_KEY"
    echo "   - SPOTIFY_CLIENT_ID"
    echo "   - SPOTIFY_CLIENT_SECRET"
    exit 1
fi

# ── 4. Tear down any existing containers ─────────────────────────────────────
echo "🛑 Stopping any running containers..."
docker compose down

# ── 5. Build a fresh image and start the app ─────────────────────────────────
echo "🔨 Building image and starting the app..."
docker compose up --build