@echo off
chcp 65001 >nul 2>&1
title Havnix IDE
echo.
echo   ╔══════════════════════════════════════════╗
echo   ║       Havnix IDE v3.0                    ║
echo   ║   بيئة تطوير متكاملة للغة هافنيكس       ║
echo   ╚══════════════════════════════════════════╝
echo.

:: Check if Python is installed
where python >nul 2>&1
if %errorlevel% neq 0 (
    echo [خطأ] Python غير مثبت! قم بتثبيت Python 3.8+ من python.org
    pause
    exit /b 1
)

:: Run the IDE
cd /d "%~dp0"
python ide.py
pause
