# Automatic Mouse Mover

This tool automatically moves your mouse cursor 10 pixels in a random direction every 5 seconds. It is designed to simulate user activity on Windows and macOS.

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
To stop the script:
1.  Look for the **Mouse Mover** icon (blue square) in your system tray (bottom-right corner via the arrow ^).
2.  Right-click the icon and select **Exit**.

Alternatively, you can trigger the fail-safe by moving your mouse to any corner of the screen.

## Building a Standalone Executable

You can package the application into a standalone executable that does not require Python to be installed on the target machine.

### macOS Build
1.  Open your terminal in the project directory.
2.  Run the build script:
    ```bash
    ./build_macos.sh
    ```
3.  The application will be created at `dist/MouseMover.app`.
4.  **Note**: Upon first launch, macOS may ask for accessibility permissions. Grant them to `MouseMover.app` in `System Settings` -> `Privacy & Security` -> `Accessibility`.

### Windows Build
1.  Open Command Prompt or PowerShell in the project directory.
2.  Run the build script:
    ```cmd
    build_windows.bat
    ```
3.  The executable will be created at `dist\MouseMover.exe`.

**Important**: You must run this build script on a Windows machine. Running it on macOS or Linux will not produce a valid Windows executable. If you are developing on macOS/Linux and need a Windows executable, use the provided GitHub Actions workflow (.github/workflows/build.yml) to generate one automatically.

## Troubleshooting

-   **"ModuleNotFoundError: No module named 'pyautogui'"**: Ensure you have activated your virtual environment and installed the requirements.
-   **Permissions (macOS)**: macOS requires you to grant "Accessibility" permissions to the terminal or the application controlling the mouse.
-   **Fail Safe Triggered**: If you move the mouse to any corner of the screen, the script will automatically stop for safety.
