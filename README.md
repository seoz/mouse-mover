# Automatic Mouse Mover

This tool automatically moves your mouse cursor 5 pixels in a random direction every 5 seconds. It is designed to simulate user activity on Windows and macOS.

## Prerequisites

- [Python 3](https://www.python.org/downloads/) installed on your system.
- `pip` (Python package installer).

## Setup

1.  **Clone or Download** the repository to your local machine.

2.  **Navigate** to the project directory in your terminal:
    ```bash
    cd mouse-mover
    ```

3.  **Set up a Virtual Environment** (Recommended):
    -   **macOS / Linux:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    -   **Windows:**
        ```cmd
        python -m venv venv
        venv\Scripts\activate
        ```

4.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

### macOS
Run the following command in your terminal (with the virtual environment activated):
```bash
python macos/mouse_mover.py
```
To stop the script, press `CTRL+C` in the terminal.

### Windows
Run the following command in Command Prompt or PowerShell (with the virtual environment activated):
```cmd
python windows\mouse_mover.py
```
To stop the script, press `CTRL+C`.

## Building a Standalone Executable (Optional)

If you want to create a standalone executable (e.g., `.exe` or `.app`) that doesn't require Python to be installed, you can use `pyinstaller`.

1.  **Install PyInstaller:**
    ```bash
    pip install pyinstaller
    ```

2.  **Build the Executable:**
    -   **macOS:**
        ```bash
        pyinstaller --onefile --noconsole --name "MouseMover" macos/mouse_mover.py
        ```
        The app will be in the `dist/` folder. Note: You may need to grant accessibility permissions to the app.

    -   **Windows:**
        ```cmd
        pyinstaller --onefile --noconsole --name "MouseMover" windows\mouse_mover.py
        ```
        The `.exe` file will be in the `dist/` folder.

## Troubleshooting

-   **"ModuleNotFoundError: No module named 'pyautogui'"**: Ensure you have activated your virtual environment and installed the requirements.
-   **Permissions (macOS)**: macOS requires you to grant "Accessibility" permissions to the terminal or the application controlling the mouse. Go to `System Settings` -> `Privacy & Security` -> `Accessibility` and enable the terminal (e.g., Terminal, iTerm) or the compiled app.
-   **Fail Safe Triggered**: If you move the mouse to any corner of the screen, the script will automatically stop for safety.
