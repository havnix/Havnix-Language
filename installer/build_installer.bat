@echo off
echo ==========================================
echo    Havnix Installer Builder
echo    يبني: setup.exe + havnix.exe + ide.exe
echo ==========================================
echo.

REM Check for Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [!] Python غير مثبت. حمل Python من https://python.org
    pause
    exit /b 1
)

REM Check for PyInstaller
python -m PyInstaller --version >nul 2>&1
if errorlevel 1 (
    echo [*] جاري تثبيت PyInstaller...
    pip install pyinstaller
)

cd /d "%~dp0\.."

echo.
echo [1/3] جاري بناء havnix-setup.exe (Install Wizard)...
echo.
python -m PyInstaller --onefile --windowed --name havnix-setup ^
    --add-data "core;core" ^
    --add-data "packages;packages" ^
    --add-data "examples;examples" ^
    --add-data "havnix.py;." ^
    --add-data "ide.py;." ^
    --add-data "requirements.txt;." ^
    --add-data "GUIDE.md;." ^
    installer\havnix_installer.py

echo.
echo [2/3] جاري بناء havnix.exe (CLI + Package Manager)...
echo.
python -m PyInstaller --onefile --console --name havnix ^
    --add-data "core;core" ^
    --add-data "packages;packages" ^
    havnix.py

echo.
echo [3/3] جاري بناء havnix-ide.exe (IDE Launcher)...
echo.
python -m PyInstaller --onefile --windowed --name havnix-ide ^
    ide.py

echo.
echo ==========================================
if exist dist\havnix-setup.exe (
    echo [+] havnix-setup.exe  - Install Wizard
)
if exist dist\havnix.exe (
    echo [+] havnix.exe        - CLI + Package Manager
)
if exist dist\havnix-ide.exe (
    echo [+] havnix-ide.exe    - IDE Launcher
)
echo.
echo    الملفات في مجلد dist\
echo ==========================================
pause
