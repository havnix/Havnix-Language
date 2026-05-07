"""
Havnix Installer - مثبت هافنيكس
Interactive installer for Windows/Linux/macOS
Sets up environment variables, copies files, creates shortcuts
"""

import os
import sys
import shutil
import platform
import subprocess
import json

HAVNIX_VERSION = "2.0.0"
HAVNIX_NAME = "Havnix"


def get_resource_path(relative_path):
    """Get path to bundled resource (works with PyInstaller)"""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), relative_path)


def print_banner():
    print()
    print("=" * 55)
    print("    _   _                   _      ")
    print("   | | | | __ ___   ___ __ (_)_  __")
    print("   | |_| |/ _` \\ \\ / / '_ \\| \\ \\/ /")
    print("   |  _  | (_| |\\ V /| | | | |>  < ")
    print("   |_| |_|\\__,_| \\_/ |_| |_|_/_/\\_\\")
    print()
    print(f"   Havnix Programming Language v{HAVNIX_VERSION}")
    print("   لغة برمجة عربية باللهجة السودانية")
    print("=" * 55)
    print()


def get_default_install_path():
    """Get default installation path based on OS"""
    system = platform.system()
    if system == 'Windows':
        program_files = os.environ.get('PROGRAMFILES', 'C:\\Program Files')
        return os.path.join(program_files, 'Havnix')
    elif system == 'Darwin':
        return '/usr/local/havnix'
    else:
        return os.path.expanduser('~/.havnix')


def install_files(install_path):
    """Copy Havnix files to installation directory"""
    print(f"[*] جاري نسخ الملفات إلى {install_path}...")

    os.makedirs(install_path, exist_ok=True)

    # Files and directories to copy
    items = [
        ('havnix.py', 'havnix.py'),
        ('ide.py', 'ide.py'),
        ('requirements.txt', 'requirements.txt'),
        ('GUIDE.md', 'GUIDE.md'),
        ('core', 'core'),
        ('packages', 'packages'),
        ('examples', 'examples'),
    ]

    for src_name, dest_name in items:
        src = get_resource_path(src_name)
        dest = os.path.join(install_path, dest_name)
        if os.path.exists(src):
            if os.path.isdir(src):
                if os.path.exists(dest):
                    shutil.rmtree(dest)
                shutil.copytree(src, dest)
            else:
                shutil.copy2(src, dest)
            print(f"  [+] {dest_name}")

    return True


def create_windows_exe(install_path):
    """Create havnix.exe wrapper and uninstall.exe for Windows"""
    # Create havnix.bat (command-line wrapper)
    bat_path = os.path.join(install_path, 'havnix.bat')
    with open(bat_path, 'w', encoding='utf-8') as f:
        f.write('@echo off\n')
        f.write(f'python "{install_path}\\havnix.py" %*\n')
    print(f"  [+] havnix.bat")

    # Create havnix.cmd (alternative wrapper)
    cmd_path = os.path.join(install_path, 'havnix.cmd')
    with open(cmd_path, 'w', encoding='utf-8') as f:
        f.write('@echo off\n')
        f.write(f'python "{install_path}\\havnix.py" %*\n')
    print(f"  [+] havnix.cmd")

    # Create IDE launcher
    ide_bat = os.path.join(install_path, 'havnix-ide.bat')
    with open(ide_bat, 'w', encoding='utf-8') as f:
        f.write('@echo off\n')
        f.write(f'python "{install_path}\\ide.py"\n')
    print(f"  [+] havnix-ide.bat")

    # Create uninstaller script
    uninstall_path = os.path.join(install_path, 'uninstall.bat')
    with open(uninstall_path, 'w', encoding='utf-8') as f:
        f.write('@echo off\n')
        f.write('echo ==============================\n')
        f.write('echo    Havnix Uninstaller\n')
        f.write('echo ==============================\n')
        f.write('echo.\n')
        f.write('echo هل تريد إزالة هافنيكس؟\n')
        f.write('set /p confirm="اكتب Y للتأكيد: "\n')
        f.write('if /i "%confirm%" neq "Y" (\n')
        f.write('    echo تم الإلغاء.\n')
        f.write('    pause\n')
        f.write('    exit /b\n')
        f.write(')\n')
        f.write('echo.\n')
        f.write('echo [*] جاري إزالة هافنيكس...\n')
        f.write(f'echo [*] إزالة من PATH...\n')
        f.write(f'setx PATH "%PATH:{install_path};=%" /M 2>nul\n')
        f.write(f'setx PATH "%PATH:{install_path};=%" 2>nul\n')
        f.write(f'echo [*] حذف ملف Start Menu...\n')
        f.write('del "%APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\Havnix IDE.lnk" 2>nul\n')
        f.write('del "%APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\Havnix.lnk" 2>nul\n')
        f.write('echo [+] تم إزالة هافنيكس بنجاح!\n')
        f.write(f'echo [*] احذف مجلد التثبيت يدوياً: {install_path}\n')
        f.write('pause\n')
    print(f"  [+] uninstall.bat")

    # Create uninstall.py (Python-based uninstaller)
    uninstall_py = os.path.join(install_path, 'uninstall.py')
    with open(uninstall_py, 'w', encoding='utf-8') as f:
        f.write('"""Havnix Uninstaller"""\n')
        f.write('import os, sys, shutil, platform, subprocess\n')
        f.write(f'INSTALL_PATH = r"{install_path}"\n')
        f.write('\n')
        f.write('def uninstall():\n')
        f.write('    print("=" * 40)\n')
        f.write('    print("   Havnix Uninstaller")\n')
        f.write('    print("=" * 40)\n')
        f.write('    confirm = input("هل تريد إزالة هافنيكس؟ (Y/N): ")\n')
        f.write('    if confirm.upper() != "Y":\n')
        f.write('        print("تم الإلغاء.")\n')
        f.write('        return\n')
        f.write('    print("[*] جاري إزالة هافنيكس...")\n')
        f.write('    if platform.system() == "Windows":\n')
        f.write('        try:\n')
        f.write('            import winreg\n')
        f.write('            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Environment", 0, winreg.KEY_ALL_ACCESS)\n')
        f.write('            path_val = winreg.QueryValueEx(key, "Path")[0]\n')
        f.write('            new_path = ";".join([p for p in path_val.split(";") if p.strip() != INSTALL_PATH])\n')
        f.write('            winreg.SetValueEx(key, "Path", 0, winreg.REG_EXPAND_SZ, new_path)\n')
        f.write('            winreg.CloseKey(key)\n')
        f.write('            print("[+] تم إزالة المسار من PATH")\n')
        f.write('        except Exception as e:\n')
        f.write('            print(f"[!] خطأ: {e}")\n')
        f.write('    print("[+] تم إزالة هافنيكس بنجاح!")\n')
        f.write('    print(f"[*] احذف مجلد التثبيت يدوياً: {INSTALL_PATH}")\n')
        f.write('\n')
        f.write('if __name__ == "__main__":\n')
        f.write('    uninstall()\n')
    print(f"  [+] uninstall.py")


def create_linux_scripts(install_path):
    """Create shell scripts for Linux/macOS"""
    # Create havnix wrapper script
    bin_path = os.path.join(install_path, 'bin')
    os.makedirs(bin_path, exist_ok=True)

    havnix_sh = os.path.join(bin_path, 'havnix')
    with open(havnix_sh, 'w') as f:
        f.write('#!/bin/bash\n')
        f.write(f'python3 "{install_path}/havnix.py" "$@"\n')
    os.chmod(havnix_sh, 0o755)
    print(f"  [+] bin/havnix")

    # Create IDE launcher
    ide_sh = os.path.join(bin_path, 'havnix-ide')
    with open(ide_sh, 'w') as f:
        f.write('#!/bin/bash\n')
        f.write(f'python3 "{install_path}/ide.py"\n')
    os.chmod(ide_sh, 0o755)
    print(f"  [+] bin/havnix-ide")

    # Create uninstall script
    uninstall_sh = os.path.join(install_path, 'uninstall.sh')
    with open(uninstall_sh, 'w') as f:
        f.write('#!/bin/bash\n')
        f.write('echo "=============================="\n')
        f.write('echo "   Havnix Uninstaller"\n')
        f.write('echo "=============================="\n')
        f.write('echo ""\n')
        f.write('read -p "هل تريد إزالة هافنيكس؟ (y/n): " confirm\n')
        f.write('if [ "$confirm" != "y" ]; then\n')
        f.write('    echo "تم الإلغاء."\n')
        f.write('    exit 0\n')
        f.write('fi\n')
        f.write('echo "[*] جاري إزالة هافنيكس..."\n')
        f.write(f'sudo rm -f /usr/local/bin/havnix /usr/local/bin/havnix-ide\n')
        f.write(f'rm -rf "{install_path}"\n')
        f.write('echo "[+] تم إزالة هافنيكس بنجاح!"\n')
    os.chmod(uninstall_sh, 0o755)
    print(f"  [+] uninstall.sh")


def add_to_path_windows(install_path):
    """Add Havnix to Windows PATH"""
    try:
        import winreg
        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Environment",
            0,
            winreg.KEY_ALL_ACCESS
        )
        try:
            path_value = winreg.QueryValueEx(key, "Path")[0]
        except FileNotFoundError:
            path_value = ""

        if install_path not in path_value:
            new_path = f"{path_value};{install_path}" if path_value else install_path
            winreg.SetValueEx(key, "Path", 0, winreg.REG_EXPAND_SZ, new_path)
            print(f"[+] تم إضافة المسار إلى PATH: {install_path}")
            # Notify system of environment variable change
            try:
                import ctypes
                HWND_BROADCAST = 0xFFFF
                WM_SETTINGCHANGE = 0x001A
                ctypes.windll.user32.SendMessageW(HWND_BROADCAST, WM_SETTINGCHANGE, 0, "Environment")
            except Exception:
                pass
        else:
            print(f"[*] المسار موجود بالفعل في PATH")
        winreg.CloseKey(key)
        return True
    except ImportError:
        # Not on Windows, use setx as fallback
        try:
            subprocess.run(['setx', 'PATH', f'%PATH%;{install_path}'], capture_output=True)
            print(f"[+] تم إضافة المسار إلى PATH")
            return True
        except Exception:
            pass
    except Exception as e:
        print(f"[!] خطأ في إضافة PATH: {e}")
        print(f"[*] أضف المسار يدوياً: {install_path}")
    return False


def add_to_path_unix(install_path):
    """Add Havnix to Unix PATH"""
    bin_path = os.path.join(install_path, 'bin')

    # Create symlinks in /usr/local/bin
    try:
        for name in ['havnix', 'havnix-ide']:
            link = f'/usr/local/bin/{name}'
            src = os.path.join(bin_path, name)
            if os.path.exists(link):
                os.remove(link)
            os.symlink(src, link)
            print(f"[+] تم إنشاء رابط: {link}")
        return True
    except PermissionError:
        print(f"[!] تحتاج صلاحيات root. جرب:")
        print(f"    sudo ln -sf {bin_path}/havnix /usr/local/bin/havnix")
        print(f"    sudo ln -sf {bin_path}/havnix-ide /usr/local/bin/havnix-ide")
    except Exception as e:
        print(f"[!] خطأ: {e}")

    # Fallback: add to shell profile
    shell_profile = os.path.expanduser('~/.bashrc')
    if os.path.exists(os.path.expanduser('~/.zshrc')):
        shell_profile = os.path.expanduser('~/.zshrc')

    export_line = f'export PATH="{bin_path}:$PATH"'
    try:
        with open(shell_profile, 'r') as f:
            content = f.read()
        if export_line not in content:
            with open(shell_profile, 'a') as f:
                f.write(f'\n# Havnix Programming Language\n{export_line}\n')
            print(f"[+] تم إضافة المسار إلى {shell_profile}")
            print(f"[*] شغل: source {shell_profile}")
    except Exception:
        print(f"[*] أضف هذا السطر إلى {shell_profile}:")
        print(f"    {export_line}")

    return False


def install_python_deps(install_path):
    """Install Python dependencies"""
    req_file = os.path.join(install_path, 'requirements.txt')
    if os.path.exists(req_file):
        print("[*] جاري تثبيت المتطلبات...")
        try:
            subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', req_file],
                          capture_output=True, timeout=120)
            print("[+] تم تثبيت المتطلبات")
        except Exception as e:
            print(f"[!] خطأ في تثبيت المتطلبات: {e}")
            print(f"[*] ثبتها يدوياً: pip install -r {req_file}")


def save_install_info(install_path):
    """Save installation info"""
    info = {
        "version": HAVNIX_VERSION,
        "install_path": install_path,
        "platform": platform.system(),
        "python": sys.version,
    }
    info_path = os.path.join(install_path, 'install_info.json')
    with open(info_path, 'w', encoding='utf-8') as f:
        json.dump(info, f, ensure_ascii=False, indent=4)


def main():
    print_banner()

    system = platform.system()
    default_path = get_default_install_path()

    print(f"نظام التشغيل: {system}")
    print(f"مسار التثبيت الافتراضي: {default_path}")
    print()

    # Ask for install path
    install_path = input(f"مسار التثبيت [{default_path}]: ").strip()
    if not install_path:
        install_path = default_path

    print()
    print(f"سيتم تثبيت هافنيكس في: {install_path}")
    confirm = input("هل تريد المتابعة؟ (Y/n): ").strip()
    if confirm.lower() == 'n':
        print("تم إلغاء التثبيت.")
        sys.exit(0)

    print()
    print("-" * 40)

    # Step 1: Copy files
    print()
    print("[الخطوة 1/5] نسخ الملفات...")
    install_files(install_path)

    # Step 2: Create executables
    print()
    print("[الخطوة 2/5] إنشاء ملفات التشغيل...")
    if system == 'Windows':
        create_windows_exe(install_path)
    else:
        create_linux_scripts(install_path)

    # Step 3: Add to PATH
    print()
    print("[الخطوة 3/5] إضافة إلى PATH...")
    if system == 'Windows':
        add_to_path_windows(install_path)
    else:
        add_to_path_unix(install_path)

    # Step 4: Install Python dependencies
    print()
    print("[الخطوة 4/5] تثبيت المتطلبات...")
    install_python_deps(install_path)

    # Step 5: Save install info
    print()
    print("[الخطوة 5/5] حفظ معلومات التثبيت...")
    save_install_info(install_path)

    # Done!
    print()
    print("=" * 55)
    print("  [+] تم تثبيت هافنيكس بنجاح!")
    print("=" * 55)
    print()
    print("  الأوامر المتاحة:")
    print(f"    havnix --help              عرض المساعدة")
    print(f"    havnix <ملف.havnix>        تشغيل برنامج")
    print(f"    havnix install <مكتبة>     تثبيت مكتبة")
    print(f"    havnix init                إنشاء مشروع")
    if system == 'Windows':
        print(f"    havnix-ide                 فتح بيئة التطوير")
    else:
        print(f"    havnix-ide                 فتح بيئة التطوير")
    print()
    print(f"  مسار التثبيت: {install_path}")
    if system == 'Windows':
        print(f"  إزالة التثبيت: {os.path.join(install_path, 'uninstall.bat')}")
    else:
        print(f"  إزالة التثبيت: {os.path.join(install_path, 'uninstall.sh')}")
    print()

    if system == 'Windows':
        print("  ملاحظة: قد تحتاج إغلاق وفتح Terminal جديد لتفعيل الأوامر")

    print()
    input("اضغط Enter للخروج...")


if __name__ == '__main__':
    main()
