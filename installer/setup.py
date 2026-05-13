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

    installer_script = os.path.join(root_dir, 'installer', 'havnix_installer.py')
    sep = os.pathsep

    # 1. Build havnix-setup.exe (GUI Install Wizard)
    print("[1/3] جاري بناء havnix-setup.exe (Install Wizard)...")
    cmd_setup = [
        sys.executable, '-m', 'PyInstaller',
        '--onefile', '--windowed',
        '--name', 'havnix-setup',
        '--add-data', f'{root_dir}/core{sep}core',
        '--add-data', f'{root_dir}/packages{sep}packages',
        '--add-data', f'{root_dir}/examples{sep}examples',
        '--add-data', f'{root_dir}/havnix.py{sep}.',
        '--add-data', f'{root_dir}/ide.py{sep}.',
        '--add-data', f'{root_dir}/requirements.txt{sep}.',
        '--add-data', f'{root_dir}/GUIDE.md{sep}.',
        installer_script
    ]
    subprocess.run(cmd_setup, cwd=root_dir)

    # 2. Build havnix.exe (CLI + Package Manager)
    print()
    print("[2/3] جاري بناء havnix.exe (CLI)...")
    cmd_cli = [
        sys.executable, '-m', 'PyInstaller',
        '--onefile', '--console',
        '--name', 'havnix',
        '--add-data', f'{root_dir}/core{sep}core',
        '--add-data', f'{root_dir}/packages{sep}packages',
        os.path.join(root_dir, 'havnix.py')
    ]
    subprocess.run(cmd_cli, cwd=root_dir)

    # 3. Build havnix-ide.exe (IDE Launcher)
    print()
    print("[3/3] جاري بناء havnix-ide.exe (IDE)...")
    cmd_ide = [
        sys.executable, '-m', 'PyInstaller',
        '--onefile', '--windowed',
        '--name', 'havnix-ide',
        os.path.join(root_dir, 'ide.py')
    ]
    subprocess.run(cmd_ide, cwd=root_dir)

    print()
    print("=" * 40)
    dist = os.path.join(root_dir, 'dist')
    for f in ['havnix-setup', 'havnix', 'havnix-ide']:
        exe = f + ('.exe' if sys.platform == 'win32' else '')
        if os.path.exists(os.path.join(dist, exe)):
            print(f"[+] {exe}")
    print(f"\nالملفات في: {dist}")


if __name__ == '__main__':
    build_setup()
