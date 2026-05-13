#!/bin/bash
echo "=========================================="
echo "   Havnix Installer Builder"
echo "   يبني: setup + havnix + havnix-ide"
echo "=========================================="
echo

# Check for Python
if ! command -v python3 &> /dev/null; then
    echo "[!] Python3 غير مثبت"
    exit 1
fi

# Check for PyInstaller
if ! python3 -m PyInstaller --version &> /dev/null; then
    echo "[*] جاري تثبيت PyInstaller..."
    pip3 install pyinstaller
fi

cd "$(dirname "$0")/.."

echo
echo "[1/3] جاري بناء havnix-setup (Install Wizard)..."
echo
python3 -m PyInstaller --onefile --windowed --name havnix-setup \
    --add-data "core:core" \
    --add-data "packages:packages" \
    --add-data "examples:examples" \
    --add-data "havnix.py:." \
    --add-data "ide.py:." \
    --add-data "requirements.txt:." \
    --add-data "GUIDE.md:." \
    installer/havnix_installer.py

echo
echo "[2/3] جاري بناء havnix (CLI + Package Manager)..."
echo
python3 -m PyInstaller --onefile --console --name havnix \
    --add-data "core:core" \
    --add-data "packages:packages" \
    havnix.py

echo
echo "[3/3] جاري بناء havnix-ide (IDE Launcher)..."
echo
python3 -m PyInstaller --onefile --windowed --name havnix-ide \
    ide.py

echo
echo "=========================================="
[ -f dist/havnix-setup ] && echo "[+] havnix-setup   - Install Wizard"
[ -f dist/havnix ] && echo "[+] havnix          - CLI + Package Manager"
[ -f dist/havnix-ide ] && echo "[+] havnix-ide      - IDE Launcher"
echo
echo "   الملفات في مجلد dist/"
echo "=========================================="
