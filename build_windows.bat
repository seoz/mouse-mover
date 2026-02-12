@echo off
echo Building Windows application...

:: Ensure virtual environment exists
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

:: Activate virtual environment
call venv\Scripts\activate

:: Install dependencies
pip install -r requirements.txt

:: Clean previous builds
if exist "build" rmdir /s /q "build"
if exist "dist" rmdir /s /q "dist"
del *.spec

:: Build the Windows executable
echo Running PyInstaller...
pyinstaller --onefile --noconsole --name "MouseMover" --clean windows\mouse_mover.py

echo Build complete. The executable is located in dist\MouseMover.exe
pause
