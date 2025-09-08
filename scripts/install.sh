#!/bin/bash

set -e

echo "🔨 Building development image..."
docker build -t asteroids:dev .

echo "🎮 Starting the game..."
exec ./scripts/run.sh