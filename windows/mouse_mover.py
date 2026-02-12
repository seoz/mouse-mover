import pyautogui
import time
import random
import sys
import threading
from pystray import Icon, MenuItem, Menu
from PIL import Image, ImageDraw

# Event to signal the mouse moving thread to stop
stop_event = threading.Event()

def create_image():
    # Create an image for the system tray icon
    # A simple white background with a blue square in the center
    width = 64
    height = 64
    image = Image.new('RGB', (width, height), (255, 255, 255))
    dc = ImageDraw.Draw(image)
    dc.rectangle((16, 16, 48, 48), fill=(0, 120, 215)) 
    return image

def move_mouse_thread(icon):
    print("Mouse Mover Started")
    try:
        while not stop_event.is_set():
            # Generate random x and y offsets between -10 and 10
            x_offset = random.randint(-10, 10)
            y_offset = random.randint(-10, 10)
            
            # Move the mouse relative to its current position
            pyautogui.moveRel(x_offset, y_offset)
            print(f"Moved mouse by ({x_offset}, {y_offset})")
            
            # Wait for 5 seconds, checking stop_event frequently
            for _ in range(50):  # Check every 0.1s for 5 seconds
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
    menu = Menu(MenuItem('Exit', on_exit))
    icon = Icon("MouseMover", image, "Mouse Mover", menu)
    
    # Start the mouse mover logic in a separate threaddaemon thread
    # Daemon thread ensures it dies if the main program exits unexpectedly
    t = threading.Thread(target=move_mouse_thread, args=(icon,), daemon=True)
    t.start()
    
    # Run the icon (this blocks until icon.stop() is called)
    icon.run()

if __name__ == "__main__":
    # Fail-safe: moving mouse to a corner will throw an exception
    pyautogui.FAILSAFE = True
    run_app()
