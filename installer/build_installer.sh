#!/bin/bash
echo "=============================="
echo "   Havnix Installer Builder"
echo "=============================="
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

echo
echo "[*] جاري بناء havnix-setup..."
echo

cd "$(dirname "$0")/.."

python3 -m PyInstaller --onefile --name havnix-setup --console \
    --add-data "core:core" \
    --add-data "packages:packages" \
    --add-data "examples:examples" \
    --add-data "havnix.py:." \
    --add-data "ide.py:." \
    --add-data "requirements.txt:." \
    --add-data "GUIDE.md:." \
    installer/havnix_installer.py

echo
if [ -f dist/havnix-setup ]; then
    echo "[+] تم بناء الملف بنجاح: dist/havnix-setup"
    chmod +x dist/havnix-setup
else
    echo "[-] فشل بناء الملف"
fi
echo
