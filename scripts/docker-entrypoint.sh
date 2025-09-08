#!/bin/bash

set -e

setup_display() {
    echo "Setting up display environment..."
    
    if [ -e "/tmp/.X11-unix" ]; then
        xhost +local:docker >/dev/null 2>&1 || true
        echo "✓ X11 configuration applied"
    else
        echo "⚠ X11 environment not detected (headless mode?)"
    fi
}

setup_audio() {
    echo "Setting up audio..."
    
    if [ -e "/dev/snd" ]; then
        if [ ! -d "/tmp/pulse" ]; then
            mkdir -p /tmp/pulse
        fi
        
        if [ -e "/run/user/$(id -u)/pulse/native" ]; then
            ln -sf /run/user/$(id -u)/pulse/native /tmp/pulse/native 2>/dev/null || true
            export PULSE_SERVER=unix:/tmp/pulse/native
            echo "✓ Audio configuration applied"
        else
            echo "⚠ PulseAudio socket not found (audio may not work)"
        fi
    else
        echo "⚠ Audio device not available (silent mode?)"
    fi
}

check_dependencies() {
    echo "Checking dependencies..."
    
    if ! command -v python >/dev/null 2>&1; then
        echo "❌ Python not found!"
        exit 1
    fi
    
    if [ ! -f "run_game.py" ]; then
        echo "❌ File run_game.py not found!"
        exit 1
    fi
    
    echo "✓ All dependencies verified"
}

development_mode() {
    echo "🎮 Mode: Development (local)"
    echo "Starting Asteroids..."
    
    exec python run_game.py
}

production_mode() {
    echo "🚀 Mode: Production (Docker Hub)"
    echo "Starting Asteroids..."
    
    exec python run_game.py
}

main() {
    echo "========================================"
    echo "      Atari Asteroids - Docker Edition   "
    echo "========================================"
    
    setup_display
    setup_audio
    check_dependencies
    
    if [ -f "/.dockerenv" ]; then
        if [ -d "/app" ] && [ -f "/app/run_game.py" ]; then
            production_mode
        else
            echo "❌ Inconsistent production environment"
            exit 1
        fi
    else
        development_mode
    fi
}

main "$@"
