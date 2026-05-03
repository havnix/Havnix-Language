#!/usr/bin/env python3
"""
Havnix IDE - بيئة تطوير متكاملة للغة هافنيكس
Arabic RTL IDE with integrated terminal
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import subprocess
import threading
import os
import sys
import re


class HavnixIDE:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Havnix IDE - بيئة تطوير هافنيكس")
        self.root.geometry("1100x750")
        self.root.configure(bg='#1e1e2e')

        self.current_file = None
        self.is_modified = False

        self._setup_styles()
        self._create_menu()
        self._create_toolbar()
        self._create_main_layout()
        self._create_status_bar()
        self._bind_shortcuts()
        self._update_title()

        self.root.protocol("WM_DELETE_WINDOW", self._on_close)

    # ─── Styles ───

    def _setup_styles(self):
        self.colors = {
            'bg': '#1e1e2e',
            'editor_bg': '#1e1e2e',
            'editor_fg': '#cdd6f4',
            'terminal_bg': '#11111b',
            'terminal_fg': '#a6e3a1',
            'line_num_bg': '#181825',
            'line_num_fg': '#6c7086',
            'menu_bg': '#313244',
            'menu_fg': '#cdd6f4',
            'toolbar_bg': '#181825',
            'status_bg': '#313244',
            'status_fg': '#cdd6f4',
            'select_bg': '#45475a',
            'cursor': '#f5e0dc',
            'keyword': '#cba6f7',
            'string': '#a6e3a1',
            'comment': '#6c7086',
            'number': '#fab387',
            'function': '#89b4fa',
            'variable': '#f9e2af',
            'operator': '#f38ba8',
            'builtin': '#94e2d5',
            'button_bg': '#45475a',
            'button_fg': '#cdd6f4',
            'button_active': '#585b70',
            'run_bg': '#a6e3a1',
            'run_fg': '#1e1e2e',
            'stop_bg': '#f38ba8',
            'stop_fg': '#1e1e2e',
        }

        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Toolbar.TFrame', background=self.colors['toolbar_bg'])
        style.configure('Status.TFrame', background=self.colors['status_bg'])
        style.configure('Main.TPanedwindow', background=self.colors['bg'])

    # ─── Menu ───

    def _create_menu(self):
        menubar = tk.Menu(self.root, bg=self.colors['menu_bg'], fg=self.colors['menu_fg'],
                          activebackground=self.colors['select_bg'], activeforeground=self.colors['menu_fg'],
                          borderwidth=0)

        # File menu
        file_menu = tk.Menu(menubar, tearoff=0, bg=self.colors['menu_bg'], fg=self.colors['menu_fg'],
                            activebackground=self.colors['select_bg'])
        file_menu.add_command(label="ملف جديد    Ctrl+N", command=self._new_file)
        file_menu.add_command(label="فتح ملف     Ctrl+O", command=self._open_file)
        file_menu.add_command(label="حفظ         Ctrl+S", command=self._save_file)
        file_menu.add_command(label="حفظ باسم    Ctrl+Shift+S", command=self._save_as)
        file_menu.add_separator()
        file_menu.add_command(label="خروج        Ctrl+Q", command=self._on_close)
        menubar.add_cascade(label="ملف", menu=file_menu)

        # Edit menu
        edit_menu = tk.Menu(menubar, tearoff=0, bg=self.colors['menu_bg'], fg=self.colors['menu_fg'],
                            activebackground=self.colors['select_bg'])
        edit_menu.add_command(label="تراجع       Ctrl+Z", command=lambda: self.editor.edit_undo())
        edit_menu.add_command(label="إعادة       Ctrl+Y", command=lambda: self.editor.edit_redo())
        edit_menu.add_separator()
        edit_menu.add_command(label="قص          Ctrl+X", command=lambda: self.editor.event_generate("<<Cut>>"))
        edit_menu.add_command(label="نسخ         Ctrl+C", command=lambda: self.editor.event_generate("<<Copy>>"))
        edit_menu.add_command(label="لصق         Ctrl+V", command=lambda: self.editor.event_generate("<<Paste>>"))
        edit_menu.add_separator()
        edit_menu.add_command(label="تحديد الكل  Ctrl+A", command=self._select_all)
        menubar.add_cascade(label="تحرير", menu=edit_menu)

        # Run menu
        run_menu = tk.Menu(menubar, tearoff=0, bg=self.colors['menu_bg'], fg=self.colors['menu_fg'],
                           activebackground=self.colors['select_bg'])
        run_menu.add_command(label="تشغيل       F5", command=self._run_code)
        run_menu.add_command(label="مسح الطرفية", command=self._clear_terminal)
        menubar.add_cascade(label="تشغيل", menu=run_menu)

        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0, bg=self.colors['menu_bg'], fg=self.colors['menu_fg'],
                            activebackground=self.colors['select_bg'])
        help_menu.add_command(label="حول هافنيكس", command=self._show_about)
        help_menu.add_command(label="دليل الاستخدام", command=self._show_guide)
        menubar.add_cascade(label="مساعدة", menu=help_menu)

        self.root.config(menu=menubar)

    # ─── Toolbar ───

    def _create_toolbar(self):
        toolbar = ttk.Frame(self.root, style='Toolbar.TFrame')
        toolbar.pack(fill='x', padx=0, pady=0)

        btn_frame = tk.Frame(toolbar, bg=self.colors['toolbar_bg'])
        btn_frame.pack(fill='x', padx=5, pady=3)

        buttons = [
            ("📄 جديد", self._new_file, self.colors['button_bg'], self.colors['button_fg']),
            ("📂 فتح", self._open_file, self.colors['button_bg'], self.colors['button_fg']),
            ("💾 حفظ", self._save_file, self.colors['button_bg'], self.colors['button_fg']),
            ("▶ تشغيل", self._run_code, self.colors['run_bg'], self.colors['run_fg']),
            ("🗑 مسح", self._clear_terminal, self.colors['button_bg'], self.colors['button_fg']),
        ]

        for text, cmd, bg, fg in buttons:
            btn = tk.Button(btn_frame, text=text, command=cmd,
                            bg=bg, fg=fg, activebackground=self.colors['button_active'],
                            activeforeground=fg, relief='flat', padx=12, pady=4,
                            font=('Segoe UI', 10), cursor='hand2', borderwidth=0)
            btn.pack(side='left', padx=2)

    # ─── Main Layout ───

    def _create_main_layout(self):
        main_pane = tk.PanedWindow(self.root, orient='vertical', bg=self.colors['bg'],
                                   sashwidth=4, sashrelief='flat')
        main_pane.pack(fill='both', expand=True, padx=0, pady=0)

        # Editor frame
        editor_frame = tk.Frame(main_pane, bg=self.colors['bg'])
        main_pane.add(editor_frame, stretch='always')

        # Line numbers + Editor
        editor_container = tk.Frame(editor_frame, bg=self.colors['bg'])
        editor_container.pack(fill='both', expand=True)

        # Line numbers
        self.line_numbers = tk.Text(editor_container, width=5, padx=5, pady=8,
                                    bg=self.colors['line_num_bg'], fg=self.colors['line_num_fg'],
                                    font=('Courier New', 13), borderwidth=0, highlightthickness=0,
                                    state='disabled', cursor='arrow', takefocus=False)
        self.line_numbers.pack(side='right', fill='y')

        # Scrollbar
        scrollbar = tk.Scrollbar(editor_container, orient='vertical')
        scrollbar.pack(side='left', fill='y')

        # Editor
        self.editor = tk.Text(editor_container, wrap='none', undo=True,
                              bg=self.colors['editor_bg'], fg=self.colors['editor_fg'],
                              insertbackground=self.colors['cursor'],
                              selectbackground=self.colors['select_bg'],
                              selectforeground=self.colors['editor_fg'],
                              font=('Courier New', 13), padx=10, pady=8,
                              borderwidth=0, highlightthickness=0,
                              spacing1=2, spacing3=2, tabs='40')
        self.editor.pack(side='right', fill='both', expand=True)

        # Configure RTL
        self.editor.tag_configure('rtl', justify='right')

        # Connect scrollbar
        scrollbar.config(command=self._sync_scroll)
        self.editor.config(yscrollcommand=self._on_editor_scroll)

        # Editor bindings
        self.editor.bind('<<Modified>>', self._on_modify)
        self.editor.bind('<KeyRelease>', self._on_key_release)
        self.editor.bind('<ButtonRelease>', self._on_key_release)
        self.editor.bind('<MouseWheel>', self._on_mousewheel)
        self.editor.bind('<Button-4>', self._on_mousewheel)
        self.editor.bind('<Button-5>', self._on_mousewheel)

        # Terminal frame
        terminal_frame = tk.Frame(main_pane, bg=self.colors['terminal_bg'])
        main_pane.add(terminal_frame, stretch='never')
        main_pane.paneconfigure(terminal_frame, minsize=150, height=200)

        # Terminal header
        term_header = tk.Frame(terminal_frame, bg=self.colors['toolbar_bg'])
        term_header.pack(fill='x')
        tk.Label(term_header, text="الطرفية ◀", bg=self.colors['toolbar_bg'],
                 fg=self.colors['terminal_fg'], font=('Segoe UI', 10, 'bold'),
                 padx=10, pady=3).pack(side='right')

        # Terminal text
        self.terminal = scrolledtext.ScrolledText(terminal_frame, wrap='word',
                                                   bg=self.colors['terminal_bg'],
                                                   fg=self.colors['terminal_fg'],
                                                   insertbackground=self.colors['terminal_fg'],
                                                   font=('Courier New', 12), padx=10, pady=5,
                                                   borderwidth=0, highlightthickness=0,
                                                   state='disabled')
        self.terminal.pack(fill='both', expand=True)

        # Configure terminal tags
        self.terminal.tag_configure('error', foreground='#f38ba8')
        self.terminal.tag_configure('success', foreground='#a6e3a1')
        self.terminal.tag_configure('info', foreground='#89b4fa')

        # Set initial content
        self._set_welcome_content()
        self._update_line_numbers()

    def _set_welcome_content(self):
        welcome = '''// مرحبا بك في هافنيكس! 🇸🇩
// اكتب كود هافنيكس هنا واضغط F5 للتشغيل

$الاسم = "عثمان";
$العمر = 18;

قول ليهو("مرحبا يا $الاسم!");
قول ليهو("عمرك $العمر سنة");

لو ($العمر >= 18) {
    قول ليهو("انت كبير 💪");
}

$فواكه = ["تفاح", "موز", "برتقال"];
لكل $فاكهة في $فواكه {
    قول ليهو("فاكهة: $فاكهة");
}

دالة مرحبا(الاسم) {
    قول ليهو("أهلا يا $الاسم!");
}
جيب لي مرحبا("أحمد");
'''
        self.editor.insert('1.0', welcome)
        self.editor.edit_modified(False)
        self.is_modified = False

    # ─── Syntax Highlighting ───

    def _highlight_syntax(self):
        for tag in ['keyword', 'string', 'comment', 'number', 'function',
                     'variable', 'operator', 'builtin']:
            self.editor.tag_remove(tag, '1.0', 'end')

        content = self.editor.get('1.0', 'end')

        # Tag configs
        self.editor.tag_configure('keyword', foreground=self.colors['keyword'], font=('Courier New', 13, 'bold'))
        self.editor.tag_configure('string', foreground=self.colors['string'])
        self.editor.tag_configure('comment', foreground=self.colors['comment'], font=('Courier New', 13, 'italic'))
        self.editor.tag_configure('number', foreground=self.colors['number'])
        self.editor.tag_configure('function', foreground=self.colors['function'])
        self.editor.tag_configure('variable', foreground=self.colors['variable'])
        self.editor.tag_configure('operator', foreground=self.colors['operator'])
        self.editor.tag_configure('builtin', foreground=self.colors['builtin'])

        # Keywords
        keywords = [
            'قول ليهو', 'اطبع', 'لو', 'غير كدا لو', 'غير كدا', 'ولو',
            'طالما', 'لكل', 'في', 'تكرار', 'وقف', 'كمل', 'رجع',
            'دالة', 'جيب لي', 'جرب', 'امسك', 'واخيراً', 'لو_فشل', 'دايماً',
            'داير', 'ثابت', 'صاح', 'غلط', 'فاضي', 'و', 'أو', 'مو',
            'اسأل', 'اسال', 'انتهى',
        ]

        # Database / API / GUI / File keywords
        special_keywords = [
            'اتصل_قاعدة', 'استعلم', 'نفذ_استعلام', 'اقفل_قاعدة',
            'جيب_من', 'ابعت_ل', 'حدث_في', 'احذف_من_api',
            'نافذة_جديدة', 'زر', 'نص_ثابت', 'مدخل_نص', 'مساحة_نص',
            'قائمة_منسدلة', 'خانة_اختيار', 'شغل_واجهة',
            'اقرأ_ملف', 'اكتب_ملف', 'اضف_ملف', 'احذف_ملف',
        ]

        # Builtin functions
        builtins = [
            'طول', 'قطع', 'استبدل', 'قسم', 'كبر', 'صغر', 'يحتوي', 'ضم', 'عكس',
            'جذر', 'قوة', 'مطلق', 'عشوائي', 'تقريب', 'اكبر', 'اصغر',
            'رقم', 'عشري', 'نص', 'منطقي', 'نوع',
            'مفاتيح', 'قيم', 'اضف', 'احذف_عنصر', 'ترتيب', 'نطاق',
            'json_حلل', 'json_نص',
        ]

        lines = content.split('\n')
        for line_num, line in enumerate(lines, 1):
            # Comments
            if '//' in line:
                comment_start = line.index('//')
                start = f"{line_num}.{comment_start}"
                end = f"{line_num}.end"
                self.editor.tag_add('comment', start, end)

            # Strings
            for m in re.finditer(r'"[^"]*"', line):
                start = f"{line_num}.{m.start()}"
                end = f"{line_num}.{m.end()}"
                self.editor.tag_add('string', start, end)

            # Variables ($name)
            for m in re.finditer(r'\$\w+', line):
                start = f"{line_num}.{m.start()}"
                end = f"{line_num}.{m.end()}"
                self.editor.tag_add('variable', start, end)

            # Numbers
            for m in re.finditer(r'\b\d+\.?\d*\b', line):
                start = f"{line_num}.{m.start()}"
                end = f"{line_num}.{m.end()}"
                self.editor.tag_add('number', start, end)

            # Keywords
            for kw in keywords:
                pattern = re.escape(kw)
                for m in re.finditer(pattern, line):
                    start = f"{line_num}.{m.start()}"
                    end = f"{line_num}.{m.end()}"
                    self.editor.tag_add('keyword', start, end)

            # Special keywords (DB, API, GUI, File)
            for kw in special_keywords:
                pattern = re.escape(kw)
                for m in re.finditer(pattern, line):
                    start = f"{line_num}.{m.start()}"
                    end = f"{line_num}.{m.end()}"
                    self.editor.tag_add('function', start, end)

            # Builtin functions
            for fn in builtins:
                pattern = re.escape(fn) + r'\s*\('
                for m in re.finditer(pattern, line):
                    start = f"{line_num}.{m.start()}"
                    end = f"{line_num}.{m.start() + len(fn)}"
                    self.editor.tag_add('builtin', start, end)

            # Operators
            for m in re.finditer(r'[+\-*/%=<>!]+', line):
                start = f"{line_num}.{m.start()}"
                end = f"{line_num}.{m.end()}"
                self.editor.tag_add('operator', start, end)

        # Priority: comment > string > variable > ...
        self.editor.tag_raise('comment')
        self.editor.tag_raise('string')

    # ─── Line Numbers ───

    def _update_line_numbers(self):
        self.line_numbers.config(state='normal')
        self.line_numbers.delete('1.0', 'end')

        line_count = self.editor.index('end-1c').split('.')[0]
        line_numbers_text = '\n'.join(str(i) for i in range(1, int(line_count) + 1))
        self.line_numbers.insert('1.0', line_numbers_text)
        self.line_numbers.config(state='disabled')

    def _sync_scroll(self, *args):
        self.editor.yview(*args)
        self.line_numbers.yview(*args)

    def _on_editor_scroll(self, *args):
        self.line_numbers.yview_moveto(args[0])
        return True

    def _on_mousewheel(self, event):
        if event.num == 4:
            delta = -3
        elif event.num == 5:
            delta = 3
        else:
            delta = -1 * (event.delta // 120)
        self.editor.yview_scroll(delta, 'units')
        self.line_numbers.yview_scroll(delta, 'units')
        return 'break'

    # ─── Status Bar ───

    def _create_status_bar(self):
        status_frame = tk.Frame(self.root, bg=self.colors['status_bg'], height=25)
        status_frame.pack(fill='x', side='bottom')

        self.status_label = tk.Label(status_frame, text="جاهز",
                                      bg=self.colors['status_bg'], fg=self.colors['status_fg'],
                                      font=('Segoe UI', 9), padx=10)
        self.status_label.pack(side='right')

        self.pos_label = tk.Label(status_frame, text="سطر 1, عمود 1",
                                   bg=self.colors['status_bg'], fg=self.colors['status_fg'],
                                   font=('Segoe UI', 9), padx=10)
        self.pos_label.pack(side='left')

        self.file_label = tk.Label(status_frame, text="Havnix IDE v2.0",
                                    bg=self.colors['status_bg'], fg='#89b4fa',
                                    font=('Segoe UI', 9, 'bold'), padx=10)
        self.file_label.pack(side='left')

    def _update_status_pos(self):
        pos = self.editor.index('insert')
        line, col = pos.split('.')
        self.pos_label.config(text=f"سطر {line}, عمود {int(col) + 1}")

    # ─── Keyboard Shortcuts ───

    def _bind_shortcuts(self):
        self.root.bind('<Control-n>', lambda e: self._new_file())
        self.root.bind('<Control-o>', lambda e: self._open_file())
        self.root.bind('<Control-s>', lambda e: self._save_file())
        self.root.bind('<Control-Shift-S>', lambda e: self._save_as())
        self.root.bind('<Control-q>', lambda e: self._on_close())
        self.root.bind('<F5>', lambda e: self._run_code())
        self.root.bind('<Control-a>', lambda e: self._select_all())

    # ─── File Operations ───

    def _new_file(self):
        if self.is_modified:
            result = messagebox.askyesnocancel("حفظ؟", "هل تريد حفظ التغييرات الحالية؟")
            if result is True:
                self._save_file()
            elif result is None:
                return

        self.editor.delete('1.0', 'end')
        self.current_file = None
        self.is_modified = False
        self.editor.edit_modified(False)
        self._update_title()
        self._update_line_numbers()
        self._highlight_syntax()

    def _open_file(self):
        filepath = filedialog.askopenfilename(
            title="فتح ملف هافنيكس",
            filetypes=[("Havnix Files", "*.havnix"), ("All Files", "*.*")],
            defaultextension=".havnix"
        )
        if filepath:
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                self.editor.delete('1.0', 'end')
                self.editor.insert('1.0', content)
                self.current_file = filepath
                self.is_modified = False
                self.editor.edit_modified(False)
                self._update_title()
                self._update_line_numbers()
                self._highlight_syntax()
                self.status_label.config(text=f"تم فتح الملف: {os.path.basename(filepath)}")
            except Exception as e:
                messagebox.showerror("خطأ", f"خطأ في فتح الملف:\n{e}")

    def _save_file(self):
        if self.current_file:
            self._write_file(self.current_file)
        else:
            self._save_as()

    def _save_as(self):
        filepath = filedialog.asksaveasfilename(
            title="حفظ باسم",
            filetypes=[("Havnix Files", "*.havnix"), ("All Files", "*.*")],
            defaultextension=".havnix"
        )
        if filepath:
            self._write_file(filepath)
            self.current_file = filepath
            self._update_title()

    def _write_file(self, filepath):
        try:
            content = self.editor.get('1.0', 'end-1c')
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            self.is_modified = False
            self.editor.edit_modified(False)
            self._update_title()
            self.status_label.config(text=f"تم الحفظ: {os.path.basename(filepath)}")
        except Exception as e:
            messagebox.showerror("خطأ", f"خطأ في حفظ الملف:\n{e}")

    # ─── Run Code ───

    def _run_code(self):
        self._clear_terminal()
        self._terminal_write("▶ تشغيل البرنامج...\n", 'info')

        # Save to temp file if needed
        if self.current_file:
            self._save_file()
            filepath = self.current_file
        else:
            filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), '_temp_run.havnix')
            content = self.editor.get('1.0', 'end-1c')
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

        havnix_py = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'havnix.py')

        def run():
            try:
                result = subprocess.run(
                    [sys.executable, havnix_py, filepath],
                    capture_output=True, text=True, timeout=30,
                    cwd=os.path.dirname(os.path.abspath(filepath))
                )
                self.root.after(0, lambda: self._show_output(result))
            except subprocess.TimeoutExpired:
                self.root.after(0, lambda: self._terminal_write("\n⏱ انتهت المهلة الزمنية (30 ثانية)\n", 'error'))
            except Exception as e:
                self.root.after(0, lambda: self._terminal_write(f"\n❌ خطأ: {e}\n", 'error'))
            finally:
                if not self.current_file and os.path.exists(filepath):
                    try:
                        os.remove(filepath)
                    except OSError:
                        pass

        thread = threading.Thread(target=run, daemon=True)
        thread.start()
        self.status_label.config(text="جاري التشغيل...")

    def _show_output(self, result):
        if result.stdout:
            self._terminal_write(result.stdout)
        if result.stderr:
            self._terminal_write(result.stderr, 'error')

        if result.returncode == 0:
            self._terminal_write("\n✅ انتهى التشغيل بنجاح\n", 'success')
            self.status_label.config(text="تم التشغيل بنجاح")
        else:
            self._terminal_write(f"\n❌ خطأ (كود الخروج: {result.returncode})\n", 'error')
            self.status_label.config(text="خطأ في التشغيل")

    def _terminal_write(self, text, tag=None):
        self.terminal.config(state='normal')
        if tag:
            self.terminal.insert('end', text, tag)
        else:
            self.terminal.insert('end', text)
        self.terminal.see('end')
        self.terminal.config(state='disabled')

    def _clear_terminal(self):
        self.terminal.config(state='normal')
        self.terminal.delete('1.0', 'end')
        self.terminal.config(state='disabled')

    # ─── Event Handlers ───

    def _on_modify(self, event=None):
        if self.editor.edit_modified():
            self.is_modified = True
            self._update_title()

    def _on_key_release(self, event=None):
        self._highlight_syntax()
        self._update_line_numbers()
        self._update_status_pos()

    def _select_all(self):
        self.editor.tag_add('sel', '1.0', 'end')
        return 'break'

    # ─── Window ───

    def _update_title(self):
        title = "Havnix IDE"
        if self.current_file:
            title += f" - {os.path.basename(self.current_file)}"
        else:
            title += " - بدون عنوان"
        if self.is_modified:
            title += " *"
        self.root.title(title)

    def _on_close(self):
        if self.is_modified:
            result = messagebox.askyesnocancel("حفظ؟", "هل تريد حفظ التغييرات قبل الخروج؟")
            if result is True:
                self._save_file()
            elif result is None:
                return
        self.root.destroy()

    def _show_about(self):
        messagebox.showinfo("حول هافنيكس",
                            "Havnix IDE v2.0\n\n"
                            "بيئة تطوير متكاملة للغة هافنيكس\n"
                            "لغة برمجة عربية باللهجة السودانية\n\n"
                            "Developed by Osman Salih\n"
                            "github.com/Snixrs/Havnix-Language")

    def _show_guide(self):
        guide_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'GUIDE.md')
        if os.path.exists(guide_path):
            try:
                with open(guide_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                guide_win = tk.Toplevel(self.root)
                guide_win.title("دليل الاستخدام")
                guide_win.geometry("700x500")
                guide_win.configure(bg=self.colors['bg'])

                text = scrolledtext.ScrolledText(guide_win, wrap='word',
                                                  bg=self.colors['editor_bg'],
                                                  fg=self.colors['editor_fg'],
                                                  font=('Courier New', 11),
                                                  padx=15, pady=10)
                text.pack(fill='both', expand=True)
                text.insert('1.0', content)
                text.config(state='disabled')
            except Exception as e:
                messagebox.showerror("خطأ", f"خطأ في فتح الدليل:\n{e}")
        else:
            messagebox.showinfo("دليل الاستخدام", "ملف الدليل غير موجود.\nراجع GUIDE.md في مجلد المشروع.")

    # ─── Run ───

    def run(self):
        self._highlight_syntax()
        self.root.mainloop()


def main():
    ide = HavnixIDE()
    ide.run()


if __name__ == '__main__':
    main()
