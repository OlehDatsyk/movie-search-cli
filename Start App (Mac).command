#!/bin/bash
# =============================================================
#  Start App (Mac).command
#  Double-click this file in Finder to set up (if needed) and
#  launch the Movie Search CLI application on macOS.
#
#  First-time use: right-click the file, choose "Open," and
#  confirm the security prompt (macOS blocks unsigned scripts by
#  default). After that, double-clicking works normally.
# =============================================================

# Move into the folder this script lives in, no matter where it
# was launched from.
cd "$(cd "$(dirname "$0")" && pwd)" || exit 1

echo "==============================================================="
echo "  Movie Search CLI - macOS Launcher (Was made by Oleh Datsyk)"
echo "==============================================================="
echo

# -------------------------------------------------------------
# 1. Verify Python is installed
# -------------------------------------------------------------
echo "[1/6] Checking for Python..."
PYTHON_CMD=""
if command -v python3 >/dev/null 2>&1; then
    PYTHON_CMD="python3"
elif command -v python >/dev/null 2>&1; then
    PYTHON_CMD="python"
fi

if [ -z "$PYTHON_CMD" ]; then
    echo
    echo "[ERROR] Python was not found on this computer."
    echo "Please install Python from https://www.python.org/downloads/"
    echo
    read -n 1 -s -r -p "Press any key to close this window..."
    exit 1
fi
echo "      Python found ($PYTHON_CMD): OK"
echo

# -------------------------------------------------------------
# 2. Create a virtual environment if it doesn't exist yet
# -------------------------------------------------------------
echo "[2/6] Checking for virtual environment..."
if [ ! -f "venv/bin/activate" ]; then
    echo "      No virtual environment found. Creating one now..."
    "$PYTHON_CMD" -m venv venv
    if [ $? -ne 0 ]; then
        echo
        echo "[ERROR] Failed to create the virtual environment."
        echo
        read -n 1 -s -r -p "Press any key to close this window..."
        exit 1
    fi
    echo "      Virtual environment created."
else
    echo "      Virtual environment already exists."
fi
echo

# -------------------------------------------------------------
# 3. Activate the virtual environment
# -------------------------------------------------------------
echo "[3/6] Activating virtual environment..."
# shellcheck disable=SC1091
source "venv/bin/activate"
if [ $? -ne 0 ]; then
    echo
    echo "[ERROR] Failed to activate the virtual environment."
    echo
    read -n 1 -s -r -p "Press any key to close this window..."
    exit 1
fi
echo "      Activated."
echo

# -------------------------------------------------------------
# 4. Install missing dependencies
# -------------------------------------------------------------
echo "[4/6] Checking / installing dependencies from requirements.txt..."
python -m pip install --disable-pip-version-check -q -r requirements.txt
if [ $? -ne 0 ]; then
    echo
    echo "[ERROR] Failed to install dependencies. Check your internet"
    echo "connection and try again."
    echo
    read -n 1 -s -r -p "Press any key to close this window..."
    exit 1
fi
echo "      Dependencies OK."
echo

# -------------------------------------------------------------
# 5. Verify the .env file exists
# -------------------------------------------------------------
echo "[5/6] Checking for .env file..."
if [ ! -f ".env" ]; then
    echo
    echo "[WARNING] No .env file was found."
    echo "A .env file is required and must contain your OMDb API key."
    echo
    if [ -f ".env.example" ]; then
        echo "      Creating .env from .env.example as a starting point..."
        cp ".env.example" ".env"
        echo
        echo "Please open the new '.env' file in VS Code or TextEdit and"
        echo "replace 'your_api_key_here' with your real OMDb API key,"
        echo "then run this script again."
        echo "Get a free key at: https://www.omdbapi.com/apikey.aspx"
        echo
        read -n 1 -s -r -p "Press any key to close this window..."
        exit 1
    else
        echo "No .env.example file was found either. Please create a"
        echo "'.env' file manually containing:"
        echo "    OMDB_API_KEY=your_actual_api_key_here"
        echo
        read -n 1 -s -r -p "Press any key to close this window..."
        exit 1
    fi
else
    echo "      .env file found."
fi
echo

# -------------------------------------------------------------
# 6. Launch the application
# -------------------------------------------------------------
echo "[6/6] Launching Movie Search CLI..."
echo "============================================================="
echo
python main.py
APP_EXIT_CODE=$?

if [ $APP_EXIT_CODE -ne 0 ]; then
    echo
    echo "============================================================="
    echo "The application exited with an error (code $APP_EXIT_CODE)."
    echo "Review the messages above for details."
    echo "============================================================="
fi

echo
read -n 1 -s -r -p "Press any key to close this window..."
