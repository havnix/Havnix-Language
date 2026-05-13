"""
Havnix Setup Wizard - مثبت هافنيكس
Professional GUI installer for Windows/Linux/macOS
"""

import os
import sys
import shutil
import platform
import subprocess
import json
import threading
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

HAVNIX_VERSION = "2.0.0"
HAVNIX_NAME = "Havnix"

# Colors
BG_DARK = "#0a0a0f"
BG_PANEL = "#12121a"
BG_SURFACE = "#1a1a2e"
ACCENT = "#60a5fa"
ACCENT_HOVER = "#3b82f6"
TEXT_WHITE = "#ffffff"
TEXT_LIGHT = "#c0c0c0"
TEXT_MUTED = "#666680"
BORDER = "#2a2a3e"
BLUE_DARK = "#1B569A"
GREEN = "#22c55e"
RED = "#ef4444"


def get_resource_path(relative_path):
    """Get path to bundled resource (works with PyInstaller)"""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), relative_path)


def get_default_install_path():
    system = platform.system()
    if system == 'Windows':
        return os.path.join(os.environ.get('PROGRAMFILES', 'C:\\Program Files'), 'Havnix')
    elif system == 'Darwin':
        return '/usr/local/havnix'
    else:
        return os.path.expanduser('~/.havnix')


class HavnixInstaller(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Havnix Setup Wizard")
        self.geometry("700x520")
        self.resizable(False, False)
        self.configure(bg=BG_DARK)

        # Center window
        self.update_idletasks()
        x = (self.winfo_screenwidth() - 700) // 2
        y = (self.winfo_screenheight() - 520) // 2
        self.geometry(f"700x520+{x}+{y}")

        # Variables
        self.install_path = tk.StringVar(value=get_default_install_path())
        self.desktop_shortcut = tk.BooleanVar(value=True)
        self.ide_shortcut = tk.BooleanVar(value=True)
        self.add_to_path = tk.BooleanVar(value=True)
        self.associate_files = tk.BooleanVar(value=True)
        self.current_page = 0

        # Pages
        self.pages = []
        self._create_pages()
        self._show_page(0)

    def _create_logo_frame(self, parent):
        """Create the logo section at the top"""
        logo_frame = tk.Frame(parent, bg=BG_DARK, height=100)
        logo_frame.pack(fill='x', padx=0, pady=0)
        logo_frame.pack_propagate(False)

        # Gradient-like top bar
        top_bar = tk.Frame(logo_frame, bg=BG_DARK, height=100)
        top_bar.pack(fill='both', expand=True)

        # Logo canvas
        canvas = tk.Canvas(top_bar, width=80, height=80, bg=BG_DARK, highlightthickness=0)
        canvas.pack(side='left', padx=(30, 15), pady=10)

        # Draw logo (gradient square with H)
        canvas.create_rectangle(5, 5, 75, 75, fill=BLUE_DARK, outline='')
        canvas.create_rectangle(5, 5, 75, 40, fill='#000000', outline='')
        canvas.create_text(40, 40, text="H", fill="white", font=("Arial", 36, "bold"))

        # Title and version
        title_frame = tk.Frame(top_bar, bg=BG_DARK)
        title_frame.pack(side='left', pady=10)

        tk.Label(title_frame, text="Havnix", font=("Arial", 24, "bold"),
                fg=TEXT_WHITE, bg=BG_DARK).pack(anchor='w')
        tk.Label(title_frame, text=f"لغة برمجة عربية باللهجة السودانية  •  v{HAVNIX_VERSION}",
                font=("Arial", 11), fg=TEXT_MUTED, bg=BG_DARK).pack(anchor='w')

        # Separator
        sep = tk.Frame(parent, bg=BORDER, height=1)
        sep.pack(fill='x')

        return logo_frame

    def _create_nav_buttons(self, parent, back=True, next_text="التالي", next_cmd=None, back_cmd=None):
        """Create bottom navigation buttons"""
        sep = tk.Frame(parent, bg=BORDER, height=1)
        sep.pack(fill='x', side='bottom')

        nav = tk.Frame(parent, bg=BG_PANEL, height=60)
        nav.pack(fill='x', side='bottom')
        nav.pack_propagate(False)

        # Cancel button
        cancel_btn = tk.Button(nav, text="إلغاء", font=("Arial", 11),
                              bg=BG_SURFACE, fg=TEXT_LIGHT, bd=0,
                              activebackground=BORDER, activeforeground=TEXT_WHITE,
                              padx=20, pady=8, cursor="hand2",
                              command=self._cancel)
        cancel_btn.pack(side='left', padx=15, pady=12)

        # Next button
        next_btn = tk.Button(nav, text=next_text, font=("Arial", 11, "bold"),
                            bg=ACCENT, fg=TEXT_WHITE, bd=0,
                            activebackground=ACCENT_HOVER, activeforeground=TEXT_WHITE,
                            padx=25, pady=8, cursor="hand2",
                            command=next_cmd or (lambda: self._next_page()))
        next_btn.pack(side='right', padx=15, pady=12)

        # Back button
        if back:
            back_btn = tk.Button(nav, text="السابق", font=("Arial", 11),
                                bg=BG_SURFACE, fg=TEXT_LIGHT, bd=0,
                                activebackground=BORDER, activeforeground=TEXT_WHITE,
                                padx=20, pady=8, cursor="hand2",
                                command=back_cmd or (lambda: self._prev_page()))
            back_btn.pack(side='right', pady=12)

        return nav

    def _create_pages(self):
        # Page 0: Welcome
        page0 = tk.Frame(self, bg=BG_DARK)
        self._create_logo_frame(page0)
        content0 = tk.Frame(page0, bg=BG_DARK)
        content0.pack(fill='both', expand=True, padx=40, pady=20)

        tk.Label(content0, text="مرحباً بك في مثبّت هافنيكس",
                font=("Arial", 18, "bold"), fg=TEXT_WHITE, bg=BG_DARK).pack(pady=(10, 8))
        tk.Label(content0, text="هذا المثبت سيجهز لك كل شي تحتاجه عشان تبدأ تبرمج باللهجة السودانية",
                font=("Arial", 11), fg=TEXT_LIGHT, bg=BG_DARK, wraplength=500).pack(pady=(0, 20))

        # Features list
        features_frame = tk.Frame(content0, bg=BG_SURFACE, padx=20, pady=15)
        features_frame.pack(fill='x', pady=5)

        features = [
            ("مفسّر هافنيكس", "havnix.exe — شغل ملفات .havnix من أي مكان"),
            ("بيئة التطوير", "ide.exe — IDE عربي متكامل مع طرفية"),
            ("مدير المكتبات", "havnix install/uninstall — نظام حزم كامل"),
            ("6 مكتبات رسمية", "رياضيات، تقويم هجري، ألوان، نصوص، تحقق، ملفات"),
            ("أمثلة جاهزة", "15+ مثال .havnix للتعلم"),
        ]
        for title, desc in features:
            row = tk.Frame(features_frame, bg=BG_SURFACE)
            row.pack(fill='x', pady=3)
            tk.Label(row, text="●", fg=ACCENT, bg=BG_SURFACE, font=("Arial", 8)).pack(side='right', padx=(8, 0))
            tk.Label(row, text=title, fg=TEXT_WHITE, bg=BG_SURFACE, font=("Arial", 11, "bold"),
                    anchor='e').pack(side='right')
            tk.Label(row, text=f" — {desc}", fg=TEXT_MUTED, bg=BG_SURFACE, font=("Arial", 10),
                    anchor='e').pack(side='right')

        self._create_nav_buttons(page0, back=False)
        self.pages.append(page0)

        # Page 1: Install Location
        page1 = tk.Frame(self, bg=BG_DARK)
        self._create_logo_frame(page1)
        content1 = tk.Frame(page1, bg=BG_DARK)
        content1.pack(fill='both', expand=True, padx=40, pady=20)

        tk.Label(content1, text="اختر مكان التثبيت",
                font=("Arial", 16, "bold"), fg=TEXT_WHITE, bg=BG_DARK).pack(anchor='e', pady=(10, 15))

        tk.Label(content1, text="سيتم تثبيت هافنيكس في المجلد التالي:",
                font=("Arial", 11), fg=TEXT_LIGHT, bg=BG_DARK).pack(anchor='e', pady=(0, 8))

        path_frame = tk.Frame(content1, bg=BG_DARK)
        path_frame.pack(fill='x', pady=5)

        browse_btn = tk.Button(path_frame, text="استعراض...", font=("Arial", 10),
                              bg=BG_SURFACE, fg=TEXT_LIGHT, bd=0,
                              activebackground=BORDER, padx=12, pady=6, cursor="hand2",
                              command=self._browse_path)
        browse_btn.pack(side='left')

        path_entry = tk.Entry(path_frame, textvariable=self.install_path, font=("Arial", 11),
                             bg=BG_SURFACE, fg=TEXT_WHITE, insertbackground=TEXT_WHITE,
                             bd=0, relief='flat')
        path_entry.pack(side='left', fill='x', expand=True, padx=(8, 0), ipady=6)

        # Space info
        tk.Label(content1, text="المساحة المطلوبة: ~25 MB",
                font=("Arial", 10), fg=TEXT_MUTED, bg=BG_DARK).pack(anchor='e', pady=(15, 0))

        self._create_nav_buttons(page1)
        self.pages.append(page1)

        # Page 2: Options
        page2 = tk.Frame(self, bg=BG_DARK)
        self._create_logo_frame(page2)
        content2 = tk.Frame(page2, bg=BG_DARK)
        content2.pack(fill='both', expand=True, padx=40, pady=20)

        tk.Label(content2, text="خيارات التثبيت",
                font=("Arial", 16, "bold"), fg=TEXT_WHITE, bg=BG_DARK).pack(anchor='e', pady=(10, 15))

        options_frame = tk.Frame(content2, bg=BG_SURFACE, padx=20, pady=15)
        options_frame.pack(fill='x')

        options = [
            (self.add_to_path, "إضافة هافنيكس إلى PATH", "يخليك تكتب havnix من أي مكان في الطرفية"),
            (self.desktop_shortcut, "إنشاء اختصار Havnix على سطح المكتب", "اختصار لتشغيل ملفات .havnix"),
            (self.ide_shortcut, "إنشاء اختصار Havnix IDE على سطح المكتب", "يفتح بيئة التطوير مباشرة"),
            (self.associate_files, "ربط ملفات .havnix بهافنيكس", "دبل كليك على .havnix يشغله تلقائياً"),
        ]

        for var, title, desc in options:
            opt_frame = tk.Frame(options_frame, bg=BG_SURFACE)
            opt_frame.pack(fill='x', pady=6)
            cb = tk.Checkbutton(opt_frame, variable=var, bg=BG_SURFACE, fg=TEXT_WHITE,
                               selectcolor=BG_DARK, activebackground=BG_SURFACE,
                               activeforeground=TEXT_WHITE, font=("Arial", 11),
                               text=title, anchor='e', cursor="hand2")
            cb.pack(anchor='e')
            tk.Label(opt_frame, text=desc, font=("Arial", 9), fg=TEXT_MUTED,
                    bg=BG_SURFACE, anchor='e').pack(anchor='e', padx=(0, 24))

        self._create_nav_buttons(page2, next_text="تثبيت", next_cmd=self._start_install)
        self.pages.append(page2)

        # Page 3: Installing (progress)
        page3 = tk.Frame(self, bg=BG_DARK)
        self._create_logo_frame(page3)
        content3 = tk.Frame(page3, bg=BG_DARK)
        content3.pack(fill='both', expand=True, padx=40, pady=20)

        tk.Label(content3, text="جاري التثبيت...",
                font=("Arial", 16, "bold"), fg=TEXT_WHITE, bg=BG_DARK).pack(pady=(10, 15))

        self.progress_var = tk.DoubleVar(value=0)
        self.progress_bar = ttk.Progressbar(content3, variable=self.progress_var,
                                           maximum=100, length=500, mode='determinate')
        self.progress_bar.pack(pady=10)

        self.status_label = tk.Label(content3, text="", font=("Arial", 11),
                                    fg=TEXT_LIGHT, bg=BG_DARK, wraplength=500)
        self.status_label.pack(pady=5)

        self.log_text = tk.Text(content3, height=8, font=("Consolas", 9),
                               bg=BG_SURFACE, fg=TEXT_LIGHT, bd=0, relief='flat',
                               insertbackground=TEXT_WHITE, wrap='word')
        self.log_text.pack(fill='both', expand=True, pady=10)

        self.pages.append(page3)

        # Page 4: Complete
        page4 = tk.Frame(self, bg=BG_DARK)
        self._create_logo_frame(page4)
        content4 = tk.Frame(page4, bg=BG_DARK)
        content4.pack(fill='both', expand=True, padx=40, pady=20)

        tk.Label(content4, text="تم التثبيت بنجاح!",
                font=("Arial", 20, "bold"), fg=GREEN, bg=BG_DARK).pack(pady=(10, 8))
        tk.Label(content4, text="هافنيكس جاهز للاستخدام",
                font=("Arial", 12), fg=TEXT_LIGHT, bg=BG_DARK).pack(pady=(0, 20))

        done_frame = tk.Frame(content4, bg=BG_SURFACE, padx=20, pady=15)
        done_frame.pack(fill='x')

        cmds = [
            ("havnix --help", "عرض المساعدة"),
            ("havnix main.havnix", "تشغيل برنامج"),
            ("havnix install <مكتبة>", "تثبيت مكتبة"),
            ("havnix init", "إنشاء مشروع جديد"),
        ]
        for cmd, desc in cmds:
            row = tk.Frame(done_frame, bg=BG_SURFACE)
            row.pack(fill='x', pady=2)
            tk.Label(row, text=cmd, fg=ACCENT, bg=BG_SURFACE,
                    font=("Consolas", 11)).pack(side='left')
            tk.Label(row, text=f"  ←  {desc}", fg=TEXT_MUTED, bg=BG_SURFACE,
                    font=("Arial", 10)).pack(side='left')

        self.open_ide_var = tk.BooleanVar(value=True)
        tk.Checkbutton(content4, variable=self.open_ide_var, text="فتح Havnix IDE بعد الإغلاق",
                      bg=BG_DARK, fg=TEXT_WHITE, selectcolor=BG_DARK, activebackground=BG_DARK,
                      activeforeground=TEXT_WHITE, font=("Arial", 11), cursor="hand2"
                      ).pack(pady=(15, 0))

        self._create_nav_buttons(page4, back=False, next_text="إنهاء", next_cmd=self._finish)
        self.pages.append(page4)

    def _show_page(self, idx):
        for p in self.pages:
            p.pack_forget()
        self.pages[idx].pack(fill='both', expand=True)
        self.current_page = idx

    def _next_page(self):
        if self.current_page < len(self.pages) - 1:
            self._show_page(self.current_page + 1)

    def _prev_page(self):
        if self.current_page > 0:
            self._show_page(self.current_page - 1)

    def _browse_path(self):
        path = filedialog.askdirectory(title="اختر مجلد التثبيت")
        if path:
            self.install_path.set(os.path.join(path, 'Havnix'))

    def _cancel(self):
        if messagebox.askyesno("إلغاء", "هل تريد إلغاء التثبيت؟"):
            self.destroy()

    def _log(self, msg):
        self.log_text.insert('end', msg + '\n')
        self.log_text.see('end')
        self.update_idletasks()

    def _set_status(self, msg, progress=None):
        self.status_label.config(text=msg)
        if progress is not None:
            self.progress_var.set(progress)
        self.update_idletasks()

    def _start_install(self):
        self._show_page(3)
        # Run install in thread to keep GUI responsive
        threading.Thread(target=self._do_install, daemon=True).start()

    def _do_install(self):
        install_path = self.install_path.get()

        try:
            # Step 1: Create directory
            self._set_status("إنشاء مجلد التثبيت...", 5)
            os.makedirs(install_path, exist_ok=True)
            self._log(f"[+] تم إنشاء: {install_path}")

            # Step 2: Copy files
            self._set_status("نسخ الملفات...", 10)
            items = [
                ('havnix.py', 'havnix.py'),
                ('ide.py', 'ide.py'),
                ('requirements.txt', 'requirements.txt'),
                ('GUIDE.md', 'GUIDE.md'),
                ('core', 'core'),
                ('packages', 'packages'),
                ('examples', 'examples'),
            ]
            for i, (src_name, dest_name) in enumerate(items):
                src = get_resource_path(src_name)
                dest = os.path.join(install_path, dest_name)
                if os.path.exists(src):
                    if os.path.isdir(src):
                        if os.path.exists(dest):
                            shutil.rmtree(dest)
                        shutil.copytree(src, dest)
                    else:
                        shutil.copy2(src, dest)
                    self._log(f"  [+] {dest_name}")
                progress = 10 + (i + 1) * 5
                self._set_status(f"نسخ {dest_name}...", progress)

            # Step 3: Create executables
            self._set_status("إنشاء ملفات التشغيل...", 50)
            system = platform.system()
            if system == 'Windows':
                self._create_windows_files(install_path)
            else:
                self._create_unix_files(install_path)

            # Step 4: Add to PATH
            if self.add_to_path.get():
                self._set_status("إضافة إلى PATH...", 60)
                if system == 'Windows':
                    self._add_to_path_windows(install_path)
                else:
                    self._add_to_path_unix(install_path)

            # Step 5: Desktop shortcuts
            if system == 'Windows':
                if self.desktop_shortcut.get():
                    self._set_status("إنشاء اختصار Havnix...", 70)
                    self._create_windows_shortcut(install_path, "Havnix", "havnix.bat", "Havnix Programming Language")
                    self._log("[+] اختصار Havnix على سطح المكتب")

                if self.ide_shortcut.get():
                    self._set_status("إنشاء اختصار IDE...", 75)
                    self._create_windows_shortcut(install_path, "Havnix IDE", "havnix-ide.bat", "Havnix IDE")
                    self._log("[+] اختصار Havnix IDE على سطح المكتب")

            # Step 6: File association
            if self.associate_files.get() and system == 'Windows':
                self._set_status("ربط ملفات .havnix...", 80)
                self._associate_havnix_files(install_path)

            # Step 7: Install requirements
            self._set_status("تثبيت المتطلبات...", 85)
            self._install_requirements(install_path)

            # Step 8: Save info
            self._set_status("حفظ معلومات التثبيت...", 95)
            info = {
                "version": HAVNIX_VERSION,
                "install_path": install_path,
                "platform": system,
                "python": sys.version,
            }
            with open(os.path.join(install_path, 'install_info.json'), 'w', encoding='utf-8') as f:
                json.dump(info, f, ensure_ascii=False, indent=4)
            self._log("[+] تم حفظ معلومات التثبيت")

            # Done!
            self._set_status("تم التثبيت بنجاح!", 100)
            self._log("")
            self._log("=" * 40)
            self._log("  تم تثبيت هافنيكس بنجاح!")
            self._log(f"  المسار: {install_path}")
            self._log("=" * 40)

            self.after(1500, lambda: self._show_page(4))

        except PermissionError:
            self._set_status("خطأ: تحتاج صلاحيات مدير", None)
            self._log("[!] خطأ: تحتاج تشغيل المثبت كمسؤول (Run as Administrator)")
            messagebox.showerror("خطأ", "تحتاج صلاحيات مدير.\nشغل المثبت بالنقر اليمين → Run as Administrator")
        except Exception as e:
            self._set_status(f"خطأ: {e}", None)
            self._log(f"[!] خطأ: {e}")
            messagebox.showerror("خطأ", f"حصل خطأ أثناء التثبيت:\n{e}")

    def _create_windows_files(self, install_path):
        """Create batch files and uninstaller for Windows"""
        # havnix.bat
        bat = os.path.join(install_path, 'havnix.bat')
        with open(bat, 'w', encoding='utf-8') as f:
            f.write('@echo off\n')
            f.write(f'python "{install_path}\\havnix.py" %*\n')
        self._log("  [+] havnix.bat")

        # havnix.cmd
        cmd = os.path.join(install_path, 'havnix.cmd')
        with open(cmd, 'w', encoding='utf-8') as f:
            f.write('@echo off\n')
            f.write(f'python "{install_path}\\havnix.py" %*\n')
        self._log("  [+] havnix.cmd")

        # havnix-ide.bat
        ide = os.path.join(install_path, 'havnix-ide.bat')
        with open(ide, 'w', encoding='utf-8') as f:
            f.write('@echo off\n')
            f.write(f'python "{install_path}\\ide.py"\n')
        self._log("  [+] havnix-ide.bat")

        # uninstall.bat
        uninst = os.path.join(install_path, 'uninstall.bat')
        with open(uninst, 'w', encoding='utf-8') as f:
            f.write('@echo off\n')
            f.write('echo ==============================\n')
            f.write('echo    Havnix Uninstaller\n')
            f.write('echo ==============================\n')
            f.write('echo.\n')
            f.write('set /p confirm="هل تريد إزالة هافنيكس؟ (Y/N): "\n')
            f.write('if /i "%confirm%" neq "Y" (echo تم الإلغاء. & pause & exit /b)\n')
            f.write('echo [*] جاري إزالة هافنيكس...\n')
            f.write(f'setx PATH "%PATH:{install_path};=%" 2>nul\n')
            f.write('del "%USERPROFILE%\\Desktop\\Havnix.lnk" 2>nul\n')
            f.write('del "%USERPROFILE%\\Desktop\\Havnix IDE.lnk" 2>nul\n')
            f.write('del "%APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\Havnix IDE.lnk" 2>nul\n')
            f.write('del "%APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\Havnix.lnk" 2>nul\n')
            f.write('echo [+] تم إزالة الاختصارات والمسارات\n')
            f.write(f'echo [*] احذف مجلد التثبيت يدوياً: {install_path}\n')
            f.write('pause\n')
        self._log("  [+] uninstall.bat")

    def _create_unix_files(self, install_path):
        """Create shell scripts for Linux/macOS"""
        bin_path = os.path.join(install_path, 'bin')
        os.makedirs(bin_path, exist_ok=True)

        for name, target in [('havnix', 'havnix.py'), ('havnix-ide', 'ide.py')]:
            script = os.path.join(bin_path, name)
            with open(script, 'w') as f:
                f.write('#!/bin/bash\n')
                f.write(f'python3 "{install_path}/{target}" "$@"\n')
            os.chmod(script, 0o755)
            self._log(f"  [+] bin/{name}")

        # uninstall.sh
        uninst = os.path.join(install_path, 'uninstall.sh')
        with open(uninst, 'w') as f:
            f.write('#!/bin/bash\n')
            f.write('read -p "هل تريد إزالة هافنيكس؟ (y/n): " c\n')
            f.write('[ "$c" != "y" ] && echo "تم الإلغاء." && exit 0\n')
            f.write(f'sudo rm -f /usr/local/bin/havnix /usr/local/bin/havnix-ide\n')
            f.write(f'rm -rf "{install_path}"\n')
            f.write('echo "[+] تم إزالة هافنيكس"\n')
        os.chmod(uninst, 0o755)
        self._log("  [+] uninstall.sh")

    def _add_to_path_windows(self, install_path):
        try:
            import winreg
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Environment", 0, winreg.KEY_ALL_ACCESS)
            try:
                path_value = winreg.QueryValueEx(key, "Path")[0]
            except FileNotFoundError:
                path_value = ""
            if install_path not in path_value:
                new_path = f"{path_value};{install_path}" if path_value else install_path
                winreg.SetValueEx(key, "Path", 0, winreg.REG_EXPAND_SZ, new_path)
                self._log(f"[+] تم إضافة المسار إلى PATH")
                try:
                    import ctypes
                    ctypes.windll.user32.SendMessageW(0xFFFF, 0x001A, 0, "Environment")
                except Exception:
                    pass
            else:
                self._log("[*] المسار موجود بالفعل في PATH")
            winreg.CloseKey(key)
        except ImportError:
            try:
                subprocess.run(['setx', 'PATH', f'%PATH%;{install_path}'],
                              capture_output=True, timeout=30)
                self._log(f"[+] تم إضافة المسار إلى PATH")
            except Exception as e:
                self._log(f"[!] أضف المسار يدوياً: {install_path}")
        except Exception as e:
            self._log(f"[!] خطأ في PATH: {e}")

    def _add_to_path_unix(self, install_path):
        bin_path = os.path.join(install_path, 'bin')
        try:
            for name in ['havnix', 'havnix-ide']:
                link = f'/usr/local/bin/{name}'
                src = os.path.join(bin_path, name)
                if os.path.exists(link):
                    os.remove(link)
                os.symlink(src, link)
            self._log("[+] تم إنشاء روابط في /usr/local/bin/")
        except PermissionError:
            shell_profile = os.path.expanduser('~/.bashrc')
            if os.path.exists(os.path.expanduser('~/.zshrc')):
                shell_profile = os.path.expanduser('~/.zshrc')
            export_line = f'export PATH="{bin_path}:$PATH"'
            try:
                with open(shell_profile, 'r') as f:
                    content = f.read()
                if export_line not in content:
                    with open(shell_profile, 'a') as f:
                        f.write(f'\n# Havnix\n{export_line}\n')
                    self._log(f"[+] تم إضافة المسار إلى {shell_profile}")
            except Exception:
                self._log(f"[*] أضف يدوياً: {export_line}")

    def _create_windows_shortcut(self, install_path, name, target, description):
        """Create a Windows desktop shortcut using PowerShell"""
        desktop = os.path.join(os.path.expanduser('~'), 'Desktop')
        lnk_path = os.path.join(desktop, f"{name}.lnk")
        target_path = os.path.join(install_path, target)

        ps_script = f'''
$WshShell = New-Object -ComObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut("{lnk_path}")
$Shortcut.TargetPath = "{target_path}"
$Shortcut.WorkingDirectory = "{install_path}"
$Shortcut.Description = "{description}"
$Shortcut.Save()
'''
        try:
            subprocess.run(['powershell', '-Command', ps_script],
                          capture_output=True, timeout=15)
        except Exception as e:
            self._log(f"[!] ما قدرت أسوي اختصار: {e}")

    def _associate_havnix_files(self, install_path):
        """Associate .havnix files with havnix.exe on Windows"""
        try:
            import winreg
            # Create .havnix extension
            key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, r"Software\Classes\.havnix")
            winreg.SetValue(key, "", winreg.REG_SZ, "HavnixFile")
            winreg.CloseKey(key)

            # Create HavnixFile type
            key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, r"Software\Classes\HavnixFile")
            winreg.SetValue(key, "", winreg.REG_SZ, "Havnix Source File")
            winreg.CloseKey(key)

            # Set open command
            cmd = f'python "{install_path}\\havnix.py" "%1"'
            key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, r"Software\Classes\HavnixFile\shell\open\command")
            winreg.SetValue(key, "", winreg.REG_SZ, cmd)
            winreg.CloseKey(key)

            self._log("[+] تم ربط ملفات .havnix")
        except Exception as e:
            self._log(f"[!] ما قدرت أربط الملفات: {e}")

    def _install_requirements(self, install_path):
        req_file = os.path.join(install_path, 'requirements.txt')
        if os.path.exists(req_file):
            self._log("[*] جاري تثبيت المتطلبات...")
            try:
                result = subprocess.run(
                    [sys.executable, '-m', 'pip', 'install', '-r', req_file, '--quiet'],
                    capture_output=True, text=True, timeout=300
                )
                if result.returncode == 0:
                    self._log("[+] تم تثبيت المتطلبات")
                else:
                    self._log(f"[!] خطأ: {result.stderr[:200] if result.stderr else 'unknown'}")
                    self._log(f"[*] ثبتها يدوياً: pip install -r \"{req_file}\"")
            except subprocess.TimeoutExpired:
                self._log("[!] انتهت المهلة. ثبتها يدوياً:")
                self._log(f"    pip install -r \"{req_file}\"")
            except Exception as e:
                self._log(f"[!] خطأ: {e}")

    def _finish(self):
        install_path = self.install_path.get()
        if self.open_ide_var.get():
            ide_path = os.path.join(install_path, 'ide.py')
            if os.path.exists(ide_path):
                try:
                    subprocess.Popen([sys.executable, ide_path], cwd=install_path)
                except Exception:
                    pass
        self.destroy()


def main():
    app = HavnixInstaller()
    app.mainloop()


if __name__ == '__main__':
    main()
