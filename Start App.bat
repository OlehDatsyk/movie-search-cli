@echo off
REM =============================================================
REM  Start App.bat
REM  Double-click this file to set up (if needed) and launch the
REM  Movie Search CLI application on Windows.
REM =============================================================

setlocal enabledelayedexpansion
title Movie Search CLI - Launcher
cd /d "%~dp0"

echo =================================================================
echo   Movie Search CLI - Windows Launcher (Was made by Oleh Datsyk)
echo =================================================================
echo.

REM -------------------------------------------------------------
REM 1. Verify Python is installed
REM -------------------------------------------------------------
echo [1/6] Checking for Python...
where python >nul 2>nul
if %errorlevel% neq 0 (
    where py >nul 2>nul
    if %errorlevel% neq 0 (
        echo.
        echo [ERROR] Python was not found on this computer.
        echo Please install Python from https://www.python.org/downloads/
        echo IMPORTANT: check "Add python.exe to PATH" during installation.
        echo.
        pause
        exit /b 1
    ) else (
        set "PYTHON_CMD=py"
    )
) else (
    set "PYTHON_CMD=python"
)
echo       Python found: OK
echo.

REM -------------------------------------------------------------
REM 2. Create a virtual environment if it doesn't exist yet
REM -------------------------------------------------------------
echo [2/6] Checking for virtual environment...
if not exist "venv\Scripts\activate.bat" (
    echo       No virtual environment found. Creating one now...
    %PYTHON_CMD% -m venv venv
    if %errorlevel% neq 0 (
        echo.
        echo [ERROR] Failed to create the virtual environment.
        echo.
        pause
        exit /b 1
    )
    echo       Virtual environment created.
) else (
    echo       Virtual environment already exists.
)
echo.

REM -------------------------------------------------------------
REM 3. Activate the virtual environment
REM -------------------------------------------------------------
echo [3/6] Activating virtual environment...
call "venv\Scripts\activate.bat"
if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Failed to activate the virtual environment.
    echo.
    pause
    exit /b 1
)
echo       Activated.
echo.

REM -------------------------------------------------------------
REM 4. Install missing dependencies
REM -------------------------------------------------------------
echo [4/6] Checking / installing dependencies from requirements.txt...
python -m pip install --disable-pip-version-check -q -r requirements.txt
if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Failed to install dependencies. Check your internet
    echo connection and try again.
    echo.
    pause
    exit /b 1
)
echo       Dependencies OK.
echo.

REM -------------------------------------------------------------
REM 5. Verify the .env file exists
REM -------------------------------------------------------------
echo [5/6] Checking for .env file...
if not exist ".env" (
    echo.
    echo [WARNING] No .env file was found.
    echo A .env file is required and must contain your OMDb API key.
    echo.
    if exist ".env.example" (
        echo       Creating .env from .env.example as a starting point...
        copy /y ".env.example" ".env" >nul
        echo.
        echo Please open the new ".env" file in VS Code or Notepad and
        echo replace "your_api_key_here" with your real OMDb API key,
        echo then run this script again.
        echo Get a free key at: https://www.omdbapi.com/apikey.aspx
        echo.
        pause
        exit /b 1
    ) else (
        echo No .env.example file was found either. Please create a
        echo ".env" file manually containing:
        echo     OMDB_API_KEY=your_actual_api_key_here
        echo.
        pause
        exit /b 1
    )
) else (
    echo       .env file found.
)
echo.

REM -------------------------------------------------------------
REM 6. Launch the application
REM -------------------------------------------------------------
echo [6/6] Launching Movie Search CLI...
echo =============================================================
echo.
python main.py

REM Keep the window open if the app exited with an error, so the
REM user can read any error messages.
if %errorlevel% neq 0 (
    echo.
    echo =============================================================
    echo The application exited with an error (code %errorlevel%).
    echo Review the messages above for details.
    echo =============================================================
)

echo.
pause
endlocal
