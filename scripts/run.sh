#!/bin/bash


set -e

echo "🚀 Building development image..."

xhost +local:docker

docker run -it --rm \
    --name asteroids-dev \
    --device /dev/snd \
    -e DISPLAY=$DISPLAY \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    -v /run/user/$(id -u)/pulse/native:/tmp/pulse/native \
    -e PULSE_SERVER=unix:/tmp/pulse/native \
    -v $(pwd):/app \
    -w /app \
    asteroids:dev

xhost -local:docker