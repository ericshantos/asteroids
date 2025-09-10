#!/bin/bash

set -e

xhost +local:docker

docker run -it --rm \
    --user $(id -u):$(id -g) \
    --device /dev/snd \
    -e DISPLAY=$DISPLAY \
    -e XDG_RUNTIME_DIR=/tmp \
    -e PULSE_SERVER=unix:/tmp/pulse/native \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    -v /run/user/$(id -u)/pulse/native:/tmp/pulse/native:ro \
    --network host \
    asteroids:latest

xhost -local:docker