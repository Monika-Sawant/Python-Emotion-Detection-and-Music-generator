@echo off
REM ============================================
REM Emotion Music Generator - Windows Setup
REM ============================================

echo.
echo ============================================================
echo         EMOTION-BASED MUSIC GENERATOR - SETUP
echo ============================================================
echo.

REM Check Python installation
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

echo ✓ Python found
python --version

REM Create virtual environment
echo.
echo Creating virtual environment...
python -m venv venv
if errorlevel 1 (
    echo ERROR: Failed to create virtual environment
    pause
    exit /b 1
)

echo ✓ Virtual environment created

REM Activate virtual environment
echo.
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Upgrade pip
echo.
echo Upgrading pip...
python -m pip install --upgrade pip >nul 2>&1

REM Install requirements
echo.
echo Installing dependencies (this may take a few minutes)...
echo.
pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo WARNING: Some packages failed to install
    echo You may need to manually install pygame:
    echo   pip install pygame
    echo.
)

REM Check for audio tools
echo.
echo ============================================================
echo AUDIO TOOLS SETUP
echo ============================================================
echo.
echo For best audio quality, consider installing:
echo   1. FluidSynth: http://www.fluidsynth.org/download/
echo   2. Timidity: http://timidity.sourceforge.net/
echo.
echo (Optional - the app works without them but uses fallback synthesizer)
echo.

REM Installation complete
echo ============================================================
echo SETUP COMPLETE!
echo ============================================================
echo.
echo To run the application:
echo   python app.py
echo.
echo Happy music generating! 🎵
echo.
pause
