@echo off
echo ==============================
echo    Havnix Installer Builder
echo ==============================
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

echo.
echo [*] جاري بناء havnix-setup.exe...
echo.

cd /d "%~dp0\.."

python -m PyInstaller --onefile --name havnix-setup --console ^
    --add-data "core;core" ^
    --add-data "packages;packages" ^
    --add-data "examples;examples" ^
    --add-data "havnix.py;." ^
    --add-data "ide.py;." ^
    --add-data "requirements.txt;." ^
    --add-data "GUIDE.md;." ^
    installer\havnix_installer.py

echo.
if exist dist\havnix-setup.exe (
    echo [+] تم بناء الملف بنجاح: dist\havnix-setup.exe
) else (
    echo [-] فشل بناء الملف
)
echo.
pause
