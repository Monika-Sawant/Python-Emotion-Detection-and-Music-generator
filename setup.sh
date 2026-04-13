#!/bin/bash

# ============================================
# Emotion Music Generator - Setup Script
# ============================================

echo ""
echo "============================================================"
echo "         EMOTION-BASED MUSIC GENERATOR - SETUP"
echo "============================================================"
echo ""

# Check Python installation
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.8+ first"
    echo ""
    echo "Ubuntu/Debian: sudo apt-get install python3 python3-pip python3-venv"
    echo "macOS: brew install python3"
    echo ""
    exit 1
fi

echo "✓ Python found"
python3 --version

# Create virtual environment
echo ""
echo "Creating virtual environment..."
python3 -m venv venv

if [ $? -ne 0 ]; then
    echo "ERROR: Failed to create virtual environment"
    exit 1
fi

echo "✓ Virtual environment created"

# Activate virtual environment
echo ""
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo ""
echo "Upgrading pip..."
python -m pip install --upgrade pip -q

# Install requirements
echo ""
echo "Installing dependencies (this may take a few minutes)..."
echo ""
pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo ""
    echo "WARNING: Some packages failed to install"
    echo "Try manually: pip install pygame"
    echo ""
fi

# Check for audio tools
echo ""
echo "============================================================"
echo "AUDIO TOOLS SETUP"
echo "============================================================"
echo ""

if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    echo "macOS detected"
    echo ""
    
    if ! command -v fluidsynth &> /dev/null; then
        echo "FluidSynth not found. Installing..."
        brew install fluidsynth 2>/dev/null
    fi
    
    if ! command -v timidity &> /dev/null; then
        echo "Timidity not found. Installing..."
        brew install timidity 2>/dev/null
    fi
    
else
    # Linux
    echo "Linux detected"
    echo ""
    
    if ! command -v fluidsynth &> /dev/null; then
        echo "FluidSynth not found."
        echo "To install: sudo apt-get install fluidsynth"
    else
        echo "✓ FluidSynth found"
    fi
    
    if ! command -v timidity &> /dev/null; then
        echo "Timidity not found."
        echo "To install: sudo apt-get install timidity"
    else
        echo "✓ Timidity found"
    fi
fi

# Installation complete
echo ""
echo "============================================================"
echo "SETUP COMPLETE!"
echo "============================================================"
echo ""
echo "To run the application:"
echo "  source venv/bin/activate  # (if not already activated)"
echo "  python app.py"
echo ""
echo "Happy music generating! 🎵"
echo ""
