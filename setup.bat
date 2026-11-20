@echo off
title Prajwal Stationery and Xerox Setup

cd /d "%~dp0"

echo ==========================================
echo    PRAJWAL STATIONERY AND XEROX
echo             SETUP
echo ==========================================
echo.

if not exist "venv\Scripts\python.exe" (
    echo ERROR: Virtual environment not found.
    pause
    exit /b 1
)

call venv\Scripts\activate.bat

echo Installing required packages...
python -m pip install -r requirements.txt

echo.
echo Applying database migrations...
python manage.py migrate

echo.
echo ==========================================
echo Setup completed successfully!
echo ==========================================
pause
