#!/bin/bash

docker build -t asteroids:2.0.3 .

bash "$(dirname "$0")/run.sh"
