#!/bin/bash
# Havnix IDE Launcher
echo ""
echo "  ╔══════════════════════════════════════════╗"
echo "  ║       Havnix IDE v3.0  🇸🇩              ║"
echo "  ║   بيئة تطوير متكاملة للغة هافنيكس      ║"
echo "  ╚══════════════════════════════════════════╝"
echo ""

cd "$(dirname "$0")"

# Check Python
if command -v python3 &>/dev/null; then
    python3 ide.py "$@"
elif command -v python &>/dev/null; then
    python ide.py "$@"
else
    echo "[خطأ] Python غير مثبت!"
    exit 1
fi
