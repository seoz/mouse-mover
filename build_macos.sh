#!/bin/bash

# Ensure virtual environment is active or install dependencies
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

source venv/bin/activate
pip install -r requirements.txt

# Clean previous builds
rm -rf build dist *.spec

# Build the macOS application
echo "Building macOS application..."
pyinstaller --onefile --noconsole --name "MouseMover" --clean macos/mouse_mover.py

echo "Build complete. The application is located in dist/MouseMover.app"
