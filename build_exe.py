#!/usr/bin/env python3
"""
Build Havnix IDE as standalone EXE.
Requires: pip install pyinstaller

Usage: python build_exe.py
Output: dist/HavnixIDE.exe
"""

import subprocess
import sys
import os

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(base_dir)

    # Check PyInstaller
    try:
        import PyInstaller
    except ImportError:
        print("جاري تثبيت PyInstaller...")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyinstaller'])

    # Build
    cmd = [
        sys.executable, '-m', 'PyInstaller',
        '--onefile',
        '--name', 'HavnixIDE',
        '--add-data', f'havnix.py{os.pathsep}.',
        '--add-data', f'core{os.pathsep}core',
        '--add-data', f'commands{os.pathsep}commands',
        '--add-data', f'features{os.pathsep}features',
        '--add-data', f'include{os.pathsep}include',
        '--add-data', f'examples{os.pathsep}examples',
        '--add-data', f'GUIDE.md{os.pathsep}.',
        '--hidden-import', 'http.server',
        '--hidden-import', 'socketserver',
        '--hidden-import', 'webbrowser',
        '--console',
        'ide.py'
    ]

    print("جاري بناء الملف التنفيذي...")
    print(' '.join(cmd))
    subprocess.check_call(cmd)

    print("\n" + "=" * 50)
    print("تم البناء بنجاح!")
    print(f"الملف: {os.path.join(base_dir, 'dist', 'HavnixIDE.exe')}")
    print("=" * 50)


if __name__ == '__main__':
    main()
