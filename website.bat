@echo off
title Prajwal Stationery and Xerox

cd /d "%~dp0"

echo ==========================================
echo    PRAJWAL STATIONERY AND XEROX
echo ==========================================
echo.
echo Starting website...

start "" "http://127.0.0.1:8000/store/product/"

call venv\Scripts\activate.bat

python manage.py runserver 127.0.0.1:8000

pause
