import pyautogui
import time
import random
import sys

def move_mouse():
    print("Mouse Mover Started (Press Ctrl+C to stop)")
    try:
        while True:
            # Generate random x and y offsets between -5 and 5
            x_offset = random.randint(-5, 5)
            y_offset = random.randint(-5, 5)
            
            # Move the mouse relative to its current position
            pyautogui.moveRel(x_offset, y_offset)
            print(f"Moved mouse by ({x_offset}, {y_offset})")
            
            # Wait for 5 seconds
            time.sleep(5)
    except KeyboardInterrupt:
        print("\nMouse Mover Stopped")
        sys.exit(0)

if __name__ == "__main__":
    # Fail-safe: moving mouse to a corner will throw an exception
    pyautogui.FAILSAFE = True
    move_mouse()
