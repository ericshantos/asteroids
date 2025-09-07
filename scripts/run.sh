#!/bin/bash

xhost +local:docker

docker run -it --rm \
    --device /dev/snd \
    -e DISPLAY=$DISPLAY \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    -v /run/user/$(id -u)/pulse/native:/tmp/pulse/native \
    -e PULSE_SERVER=unix:/tmp/pulse/native \
    asteroids:2.0.3

xhost -local:docker