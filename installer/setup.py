"""
Havnix Setup Builder - بناء ملف التثبيت
يبني ملف setup.exe لتثبيت هافنيكس على Windows
يستخدم PyInstaller لإنشاء الملف التنفيذي
"""

import os
import sys
import json
import shutil
import subprocess

HAVNIX_VERSION = "2.0.0"


def build_setup():
    """Build the Havnix setup installer"""
    print(f"=== بناء مثبت هافنيكس {HAVNIX_VERSION} ===")
    print()

    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Check for PyInstaller
    try:
        import PyInstaller
        print("[+] PyInstaller موجود")
    except ImportError:
        print("[!] PyInstaller غير مثبت. جاري التثبيت...")
        subprocess.run([sys.executable, '-m', 'pip', 'install', 'pyinstaller'], check=True)

    # Build the installer exe
    installer_script = os.path.join(root_dir, 'installer', 'havnix_installer.py')

    print("[*] جاري بناء setup.exe...")
    cmd = [
        sys.executable, '-m', 'PyInstaller',
        '--onefile',
        '--name', 'havnix-setup',
        '--icon', 'NONE',
        '--add-data', f'{root_dir}/core{os.pathsep}core',
        '--add-data', f'{root_dir}/packages{os.pathsep}packages',
        '--add-data', f'{root_dir}/havnix.py{os.pathsep}.',
        '--add-data', f'{root_dir}/ide.py{os.pathsep}.',
        '--add-data', f'{root_dir}/requirements.txt{os.pathsep}.',
        '--add-data', f'{root_dir}/GUIDE.md{os.pathsep}.',
        '--add-data', f'{root_dir}/examples{os.pathsep}examples',
        installer_script
    ]

    subprocess.run(cmd, cwd=root_dir)
    print()
    print(f"[+] تم بناء الملف: dist/havnix-setup.exe")
    print(f"[+] شغل الملف لتثبيت هافنيكس")


if __name__ == '__main__':
    build_setup()
