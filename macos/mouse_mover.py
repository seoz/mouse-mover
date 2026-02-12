import pyautogui
import time
import random
import sys
import threading
import json
import os
import subprocess
from pystray import Icon, MenuItem, Menu
from PIL import Image, ImageDraw

# Event to signal the mouse moving thread to stop
stop_event = threading.Event()

def create_image():
    # Create an image for the menu bar icon
    # A simple black square (which looks better on macOS light/dark mode usually)
    # or sticking to the blue theme. Let's start with blue for consistency.
    width = 64
    height = 64
    image = Image.new('RGB', (width, height), (255, 255, 255))
    dc = ImageDraw.Draw(image)
    dc.rectangle((16, 16, 48, 48), fill=(0, 120, 215)) 
    return image


def get_config_path():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "settings.json")

def load_settings():
    defaults = {"interval": 5, "distance": 10}
    path = get_config_path()
    try:
        if os.path.exists(path):
            with open(path, "r") as f:
                data = json.load(f)
                return {**defaults, **data}
    except Exception as e:
        print(f"Error loading settings: {e}")
    return defaults

def on_settings(icon, item):
    script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "settings_ui.py")
    subprocess.Popen([sys.executable, script_path])

def move_mouse_thread(icon):
    print("Mouse Mover Started")
    try:
        while not stop_event.is_set():
            # Load settings
            settings = load_settings()
            interval = settings.get("interval", 5)
            distance_range = settings.get("distance", 10)

            # Generate random x and y offsets
            x_offset = random.randint(-distance_range, distance_range)
            y_offset = random.randint(-distance_range, distance_range)
            
            # Move the mouse relative to its current position
            pyautogui.moveRel(x_offset, y_offset)
            print(f"Moved mouse by ({x_offset}, {y_offset})")
            
            # Wait for interval seconds, checking stop_event frequently
            steps = int(max(1, interval) / 0.1)
            for _ in range(steps):
                if stop_event.is_set():
                    break
                time.sleep(0.1)
                
    except Exception as e:
        print(f"Error in mouse mover thread: {e}")
    finally:
        print("Mouse Mover Thread Stopped")

def on_exit(icon, item):
    """Callback for the Exit menu item"""
    stop_event.set()
    icon.stop()

def run_app():
    image = create_image()
    menu = Menu(
        MenuItem('Settings', on_settings),
        MenuItem('Exit', on_exit)
    )
    # On macOS, the title might appear next to the icon or in the menu
    icon = Icon("MouseMover", image, "Mouse Mover", menu)
    
    # Start the mouse mover logic in a separate thread
    t = threading.Thread(target=move_mouse_thread, args=(icon,), daemon=True)
    t.start()
    
    # Run the icon (this blocks until icon.stop() is called)
    icon.run()

if __name__ == "__main__":
    # Fail-safe: moving mouse to a corner will throw an exception
    pyautogui.FAILSAFE = True
    run_app()
