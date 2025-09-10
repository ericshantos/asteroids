#!/bin/bash
set -e

setup_display() {
    echo "🔎 Checking display..."
    
    if [ -e "/tmp/.X11-unix" ]; then
        xhost +local:docker >/dev/null 2>&1 || true
        echo "✅ Display available and X11 configured"
    else
        echo "❌ Error: X11 environment not detected. Make sure the display is exported."
        exit 1
    fi
}

setup_audio() {
    echo "🔎 Checking audio..."
    
    if [ -e "/dev/snd" ]; then
        mkdir -p /tmp/pulse
        
        if [ -S "/run/user/$(id -u)/pulse/native" ]; then
            ln -sf /run/user/$(id -u)/pulse/native /tmp/pulse/native 2>/dev/null || true
            export PULSE_SERVER=unix:/tmp/pulse/native
            echo "✅ Audio configured with PulseAudio"
        else
            echo "❌ Error: PulseAudio socket not found."
            exit 1
        fi
    else
        echo "❌ Error: Audio device (/dev/snd) not available."
        exit 1
    fi
}

check_dependencies() {
    echo "🔎 Checking dependencies..."
    
    if ! command -v python >/dev/null 2>&1; then
        echo "❌ Python not found in the container!"
        exit 1
    fi
    
    if [ ! -f "/app/run_game.py" ]; then
        echo "❌ File run_game.py not found in /app!"
        exit 1
    fi
    
    echo "✅ Dependencies successfully verified"
}

main() {
    setup_display
    setup_audio
    check_dependencies
    
    echo "🎮 Starting game..."
    exec python /app/run_game.py
}

main "$@"