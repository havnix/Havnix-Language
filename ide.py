#!/usr/bin/env python3
"""
Havnix IDE v3.0 - بيئة تطوير متكاملة للغة هافنيكس
Web-based Arabic RTL IDE with File Explorer, Interactive Terminal, Shell Tabs
Syntax Highlighting, Git support, and more.
No external dependencies - uses Python built-in modules only.

Usage: python3 ide.py [port]
Default port: 249
"""

import http.server
import socketserver
import json
import subprocess
import threading
import os
import sys
import webbrowser
import time
import signal
import select
from urllib.parse import urlparse, parse_qs, unquote

PORT = 249
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ─── Shell Session Manager ───

class ShellManager:
    def __init__(self):
        self.sessions = {}
        self.lock = threading.Lock()

    def create_session(self, session_id, cwd=None, shell_cmd=None):
        if cwd is None:
            cwd = BASE_DIR
        if shell_cmd is None:
            if sys.platform == 'win32':
                shell_cmd = ['/bin/bash']
            else:
                shell_cmd = ['/bin/bash']

        env = os.environ.copy()
        env['PYTHONIOENCODING'] = 'utf-8'
        env['LANG'] = 'en_US.UTF-8'
        env['TERM'] = 'dumb'
        env['PS1'] = '$ '

        try:
            import pty as _pty
            master_fd, slave_fd = _pty.openpty()

            proc = subprocess.Popen(
                shell_cmd,
                stdin=slave_fd,
                stdout=slave_fd,
                stderr=slave_fd,
                cwd=cwd,
                env=env,
                preexec_fn=os.setsid,
            )
            os.close(slave_fd)

            output_buffer = []
            buffer_lock = threading.Lock()

            def reader():
                try:
                    import select as _select
                    while proc.poll() is None:
                        try:
                            r, _, _ = _select.select([master_fd], [], [], 0.5)
                            if r:
                                data = os.read(master_fd, 4096)
                                if data:
                                    text = data.decode('utf-8', errors='replace')
                                    import re as _re
                                    text = _re.sub(r'\x1b\[[0-9;]*[a-zA-Z]', '', text)
                                    text = _re.sub(r'\x1b\]0;[^\x07]*\x07', '', text)
                                    text = text.replace('\r\n', '\n').replace('\r', '\n')
                                    with buffer_lock:
                                        output_buffer.append(text)
                                else:
                                    break
                        except (OSError, ValueError):
                            break
                except Exception:
                    pass
                with buffer_lock:
                    output_buffer.append('\n[انتهت الجلسة]\n')

            t = threading.Thread(target=reader, daemon=True)
            t.start()

            with self.lock:
                self.sessions[session_id] = {
                    'process': proc,
                    'master_fd': master_fd,
                    'output': output_buffer,
                    'buffer_lock': buffer_lock,
                    'read_index': 0,
                }
            return True
        except Exception as e:
            return str(e)

    def send_input(self, session_id, text):
        with self.lock:
            session = self.sessions.get(session_id)
        if not session or session['process'].poll() is not None:
            return False
        try:
            os.write(session['master_fd'], (text + '\n').encode('utf-8'))
            return True
        except Exception:
            return False

    def get_output(self, session_id):
        with self.lock:
            session = self.sessions.get(session_id)
        if not session:
            return ''
        with session['buffer_lock']:
            idx = session['read_index']
            new_output = ''.join(session['output'][idx:])
            session['read_index'] = len(session['output'])
        return new_output

    def kill_session(self, session_id):
        with self.lock:
            session = self.sessions.pop(session_id, None)
        if not session:
            return
        if session['process'].poll() is None:
            try:
                session['process'].kill()
            except Exception:
                pass
        try:
            os.close(session['master_fd'])
        except Exception:
            pass

    def kill_all(self):
        with self.lock:
            ids = list(self.sessions.keys())
        for sid in ids:
            self.kill_session(sid)


shell_manager = ShellManager()

# ─── Running code manager ───

running_outputs = {}
running_lock = threading.Lock()

def run_havnix_code(run_id, filepath, cwd):
    havnix_py = os.path.join(BASE_DIR, 'havnix.py')
    env = os.environ.copy()
    env['PYTHONIOENCODING'] = 'utf-8'
    env['LANG'] = 'en_US.UTF-8'

    try:
        proc = subprocess.Popen(
            [sys.executable, havnix_py, filepath],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdin=subprocess.PIPE,
            cwd=cwd,
            env=env,
        )

        with running_lock:
            running_outputs[run_id] = {'status': 'running', 'stdout': '', 'stderr': '', 'code': None, 'process': proc}

        stdout_data, stderr_data = proc.communicate(timeout=30)

        with running_lock:
            running_outputs[run_id] = {
                'status': 'done',
                'stdout': stdout_data.decode('utf-8', errors='replace') if stdout_data else '',
                'stderr': stderr_data.decode('utf-8', errors='replace') if stderr_data else '',
                'code': proc.returncode,
                'process': None,
            }
    except subprocess.TimeoutExpired:
        proc.kill()
        with running_lock:
            running_outputs[run_id] = {'status': 'timeout', 'stdout': '', 'stderr': 'انتهت المهلة (30 ثانية)', 'code': -1, 'process': None}
    except Exception as e:
        with running_lock:
            running_outputs[run_id] = {'status': 'error', 'stdout': '', 'stderr': str(e), 'code': -1, 'process': None}

# ─── HTTP Handler ───

class IDEHandler(http.server.BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

    def _send_json(self, data, status=200):
        body = json.dumps(data, ensure_ascii=False).encode('utf-8')
        self.send_response(status)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', len(body))
        self.end_headers()
        self.wfile.write(body)

    def _read_body(self):
        length = int(self.headers.get('Content-Length', 0))
        if length:
            return json.loads(self.rfile.read(length).decode('utf-8'))
        return {}

    def do_GET(self):
        path = urlparse(self.path).path

        if path == '/' or path == '/index.html':
            self._serve_html()
        elif path == '/api/files':
            self._handle_list_files()
        elif path.startswith('/api/read'):
            qs = parse_qs(urlparse(self.path).query)
            filepath = qs.get('path', [''])[0]
            self._handle_read_file(filepath)
        elif path.startswith('/api/run_output'):
            qs = parse_qs(urlparse(self.path).query)
            run_id = qs.get('id', [''])[0]
            self._handle_run_output(run_id)
        elif path.startswith('/api/shell_output'):
            qs = parse_qs(urlparse(self.path).query)
            sid = qs.get('id', [''])[0]
            output = shell_manager.get_output(sid)
            self._send_json({'output': output})
        else:
            self.send_error(404)

    def do_POST(self):
        path = urlparse(self.path).path
        data = self._read_body()

        if path == '/api/save':
            self._handle_save(data)
        elif path == '/api/run':
            self._handle_run(data)
        elif path == '/api/shell_create':
            self._handle_shell_create(data)
        elif path == '/api/shell_input':
            self._handle_shell_input(data)
        elif path == '/api/shell_kill':
            self._handle_shell_kill(data)
        elif path == '/api/send_input':
            self._handle_send_input(data)
        else:
            self.send_error(404)

    def _handle_list_files(self):
        qs = parse_qs(urlparse(self.path).query)
        root = qs.get('root', [BASE_DIR])[0]
        tree = self._build_tree(root)
        self._send_json({'tree': tree, 'root': root})

    def _build_tree(self, path, depth=0):
        if depth > 5:
            return []
        items = []
        try:
            entries = sorted(os.listdir(path))
        except (PermissionError, OSError):
            return []

        dirs = []
        files = []
        for e in entries:
            if e.startswith('.') or e.startswith('__'):
                continue
            full = os.path.join(path, e)
            if os.path.isdir(full):
                dirs.append(e)
            elif os.path.isfile(full):
                files.append(e)

        for d in dirs:
            full = os.path.join(path, d)
            children = self._build_tree(full, depth + 1)
            items.append({'name': d, 'path': full, 'type': 'dir', 'children': children})

        for f in files:
            full = os.path.join(path, f)
            items.append({'name': f, 'path': full, 'type': 'file'})

        return items

    def _handle_read_file(self, filepath):
        try:
            filepath = unquote(filepath)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            self._send_json({'content': content, 'path': filepath})
        except Exception as e:
            self._send_json({'error': str(e)}, 400)

    def _handle_save(self, data):
        try:
            filepath = data.get('path')
            content = data.get('content', '')
            if not filepath:
                filepath = os.path.join(BASE_DIR, 'untitled.havnix')
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            self._send_json({'success': True, 'path': filepath})
        except Exception as e:
            self._send_json({'error': str(e)}, 400)

    def _handle_run(self, data):
        content = data.get('content', '')
        filepath = data.get('filepath')

        if filepath:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            run_path = filepath
        else:
            run_path = os.path.join(BASE_DIR, '_temp_run.havnix')
            with open(run_path, 'w', encoding='utf-8') as f:
                f.write(content)

        run_id = f"run_{int(time.time() * 1000)}"
        cwd = os.path.dirname(os.path.abspath(run_path))
        t = threading.Thread(target=run_havnix_code, args=(run_id, run_path, cwd), daemon=True)
        t.start()
        self._send_json({'run_id': run_id})

    def _handle_run_output(self, run_id):
        with running_lock:
            result = running_outputs.get(run_id)
        if result:
            safe_result = {k: v for k, v in result.items() if k != 'process'}
            self._send_json(safe_result)
        else:
            self._send_json({'status': 'not_found'})

    def _handle_shell_create(self, data):
        sid = data.get('id', f"shell_{int(time.time() * 1000)}")
        shell_type = data.get('type', 'bash')
        cwd = data.get('cwd', BASE_DIR)

        if shell_type == 'bash':
            cmd = ['/bin/bash', '--norc', '-i']
        elif shell_type == 'git':
            cmd = ['/bin/bash', '--norc', '-i']
        elif shell_type == 'powershell':
            if os.path.exists('/usr/bin/pwsh'):
                cmd = ['/usr/bin/pwsh']
            elif os.path.exists('C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe'):
                cmd = ['powershell.exe']
            else:
                cmd = ['/bin/bash', '--norc', '-i']
        elif shell_type == 'cmd':
            if sys.platform == 'win32':
                cmd = ['cmd.exe']
            else:
                cmd = ['/bin/bash', '--norc', '-i']
        else:
            cmd = ['/bin/bash', '--norc', '-i']

        result = shell_manager.create_session(sid, cwd, cmd)
        if result is True:
            self._send_json({'id': sid, 'success': True})
        else:
            self._send_json({'error': result}, 400)

    def _handle_shell_input(self, data):
        sid = data.get('id')
        text = data.get('text', '')
        if shell_manager.send_input(sid, text):
            self._send_json({'success': True})
        else:
            self._send_json({'error': 'Session not found or ended'}, 400)

    def _handle_shell_kill(self, data):
        sid = data.get('id')
        shell_manager.kill_session(sid)
        self._send_json({'success': True})

    def _handle_send_input(self, data):
        run_id = data.get('run_id')
        text = data.get('text', '')
        with running_lock:
            result = running_outputs.get(run_id)
        if result and result.get('process') and result['process'].poll() is None:
            try:
                result['process'].stdin.write((text + '\n').encode('utf-8'))
                result['process'].stdin.flush()
                self._send_json({'success': True})
            except Exception as e:
                self._send_json({'error': str(e)}, 400)
        else:
            self._send_json({'error': 'Process not running'}, 400)

    def _serve_html(self):
        html = get_ide_html()
        body = html.encode('utf-8')
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.send_header('Content-Length', len(body))
        self.end_headers()
        self.wfile.write(body)


def get_ide_html():
    return r'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Havnix IDE - بيئة تطوير هافنيكس</title>
<style>
:root {
    --bg: #1e1e2e;
    --surface: #181825;
    --overlay: #313244;
    --text: #cdd6f4;
    --subtext: #a6adc8;
    --muted: #6c7086;
    --red: #f38ba8;
    --green: #a6e3a1;
    --yellow: #f9e2af;
    --blue: #89b4fa;
    --purple: #cba6f7;
    --teal: #94e2d5;
    --peach: #fab387;
    --select: #45475a;
    --border: #313244;
    --pink: #f5c2e7;
}

* { margin: 0; padding: 0; box-sizing: border-box; }

body {
    background: var(--bg);
    color: var(--text);
    font-family: 'Segoe UI', 'Noto Sans Arabic', 'Arial', sans-serif;
    height: 100vh;
    overflow: hidden;
    direction: rtl;
}

#app {
    display: flex;
    flex-direction: column;
    height: 100vh;
}

#toolbar {
    display: flex;
    align-items: center;
    background: var(--surface);
    padding: 4px 8px;
    gap: 4px;
    border-bottom: 1px solid var(--border);
    direction: rtl;
}

#toolbar button {
    background: var(--overlay);
    color: var(--text);
    border: none;
    padding: 6px 14px;
    border-radius: 4px;
    cursor: pointer;
    font-family: inherit;
    font-size: 13px;
    transition: background 0.15s;
}
#toolbar button:hover { background: var(--select); }
#toolbar .run-btn { background: var(--green); color: var(--bg); font-weight: bold; }
#toolbar .run-btn:hover { opacity: 0.9; }

#main-area {
    display: flex;
    flex: 1;
    overflow: hidden;
    direction: ltr;
}

/* ─── File Explorer ─── */
#explorer {
    width: 220px;
    min-width: 150px;
    background: var(--surface);
    border-left: 1px solid var(--border);
    display: flex;
    flex-direction: column;
    overflow: hidden;
}

#explorer-header {
    padding: 8px 12px;
    font-weight: bold;
    font-size: 13px;
    background: var(--overlay);
    display: flex;
    justify-content: space-between;
    align-items: center;
    direction: rtl;
}
#explorer-header button {
    background: none;
    border: none;
    color: var(--subtext);
    cursor: pointer;
    font-size: 12px;
    padding: 2px 6px;
    border-radius: 3px;
}
#explorer-header button:hover { background: var(--select); }

#file-tree {
    flex: 1;
    overflow-y: auto;
    padding: 4px 0;
    direction: rtl;
}

.tree-item {
    padding: 3px 8px;
    cursor: pointer;
    font-size: 13px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    display: flex;
    align-items: center;
    gap: 4px;
    direction: rtl;
}
.tree-item:hover { background: var(--select); }
.tree-item.active { background: var(--select); color: var(--blue); }
.tree-item .icon { font-size: 14px; flex-shrink: 0; }
.tree-dir > .tree-children { display: none; }
.tree-dir.open > .tree-children { display: block; }
.tree-dir > .tree-item .arrow { transition: transform 0.15s; font-size: 10px; }
.tree-dir.open > .tree-item .arrow { transform: rotate(90deg); }

/* ─── Editor Area ─── */
#editor-area {
    flex: 1;
    display: flex;
    flex-direction: column;
    overflow: hidden;
}

#editor-tabs {
    display: flex;
    background: var(--surface);
    border-bottom: 1px solid var(--border);
    overflow-x: auto;
    direction: rtl;
}

#editor-container {
    flex: 1;
    display: flex;
    overflow: hidden;
    position: relative;
}

#line-numbers {
    width: 50px;
    background: var(--surface);
    color: var(--muted);
    font-family: 'Courier New', 'DejaVu Sans Mono', monospace;
    font-size: 14px;
    line-height: 1.6;
    padding: 8px 4px;
    text-align: center;
    overflow: hidden;
    user-select: none;
    border-left: 1px solid var(--border);
    white-space: pre;
    direction: ltr;
}

/* Editor wrapper for syntax highlighting overlay */
#editor-wrapper {
    flex: 1;
    position: relative;
    overflow: hidden;
}

#highlight-layer {
    position: absolute;
    top: 0; right: 0; bottom: 0; left: 0;
    font-family: 'Courier New', 'DejaVu Sans Mono', monospace;
    font-size: 14px;
    line-height: 1.6;
    padding: 8px 12px;
    direction: rtl;
    text-align: right;
    white-space: pre;
    overflow: hidden;
    pointer-events: none;
    color: var(--text);
    z-index: 1;
    background: var(--bg);
}

#editor {
    position: absolute;
    top: 0; right: 0; bottom: 0; left: 0;
    width: 100%;
    height: 100%;
    background: transparent;
    color: transparent;
    caret-color: var(--yellow);
    font-family: 'Courier New', 'DejaVu Sans Mono', monospace;
    font-size: 14px;
    line-height: 1.6;
    padding: 8px 12px;
    border: none;
    outline: none;
    resize: none;
    tab-size: 4;
    direction: rtl;
    text-align: right;
    overflow: auto;
    white-space: pre;
    z-index: 2;
}

/* Syntax highlighting colors */
.hl-keyword { color: var(--purple); font-weight: bold; }
.hl-builtin { color: var(--blue); }
.hl-string { color: var(--green); }
.hl-comment { color: var(--muted); font-style: italic; }
.hl-number { color: var(--peach); }
.hl-variable { color: var(--red); }
.hl-operator { color: var(--teal); }
.hl-bracket { color: var(--yellow); }
.hl-bool { color: var(--peach); font-weight: bold; }
.hl-func { color: var(--blue); font-weight: bold; }
.hl-plain { color: var(--text); }

/* ─── Bottom Panel ─── */
#bottom-panel {
    height: 250px;
    min-height: 100px;
    background: var(--surface);
    border-top: 1px solid var(--border);
    display: flex;
    flex-direction: column;
}

#terminal-tabs {
    display: flex;
    background: var(--overlay);
    gap: 1px;
    align-items: center;
    direction: rtl;
    padding-right: 4px;
}

.term-tab {
    padding: 5px 12px;
    font-size: 12px;
    cursor: pointer;
    color: var(--subtext);
    border-bottom: 2px solid transparent;
    display: flex;
    align-items: center;
    gap: 6px;
}
.term-tab:hover { background: var(--select); }
.term-tab.active { color: var(--green); border-bottom-color: var(--green); }
.term-tab .close-tab { font-size: 13px; opacity: 0.5; }
.term-tab .close-tab:hover { opacity: 1; color: var(--red); }

#terminal-tabs .add-tab {
    background: none;
    border: none;
    color: var(--subtext);
    cursor: pointer;
    font-size: 16px;
    padding: 2px 8px;
    margin-right: auto;
    margin-left: 4px;
}
#terminal-tabs .add-tab:hover { color: var(--text); }

#terminal-container {
    flex: 1;
    position: relative;
    overflow: hidden;
}

.terminal-panel {
    position: absolute;
    inset: 0;
    display: none;
    flex-direction: column;
    background: #11111b;
}
.terminal-panel.active { display: flex; }

.terminal-output {
    flex: 1;
    overflow-y: auto;
    padding: 8px 12px;
    font-family: 'Courier New', 'DejaVu Sans Mono', monospace;
    font-size: 13px;
    line-height: 1.5;
    color: var(--green);
    direction: rtl;
    text-align: right;
    white-space: pre-wrap;
    word-break: break-all;
}

.terminal-output .error { color: var(--red); }
.terminal-output .info { color: var(--blue); }
.terminal-output .success { color: var(--green); }

.terminal-input-row {
    display: flex;
    align-items: center;
    padding: 4px 8px;
    background: var(--overlay);
    gap: 6px;
    direction: rtl;
}

.terminal-input-row .prompt-sign {
    color: var(--green);
    font-family: monospace;
    font-size: 14px;
}

.terminal-input-row input {
    flex: 1;
    background: #11111b;
    color: var(--text);
    border: none;
    outline: none;
    font-family: 'Courier New', monospace;
    font-size: 13px;
    padding: 4px 8px;
    direction: rtl;
}

#resize-handle {
    height: 4px;
    background: var(--border);
    cursor: ns-resize;
}
#resize-handle:hover { background: var(--blue); }

#status-bar {
    display: flex;
    justify-content: space-between;
    padding: 3px 12px;
    background: var(--overlay);
    font-size: 11px;
    color: var(--subtext);
    direction: rtl;
}

::-webkit-scrollbar { width: 8px; height: 8px; }
::-webkit-scrollbar-track { background: var(--surface); }
::-webkit-scrollbar-thumb { background: var(--muted); border-radius: 4px; }
::-webkit-scrollbar-thumb:hover { background: var(--subtext); }

#explorer-resize {
    width: 4px;
    background: var(--border);
    cursor: ew-resize;
    flex-shrink: 0;
}
#explorer-resize:hover { background: var(--blue); }

.dropdown-menu {
    position: absolute;
    background: var(--overlay);
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 4px;
    min-width: 160px;
    z-index: 1000;
    box-shadow: 0 4px 12px rgba(0,0,0,0.3);
    direction: rtl;
    display: none;
}
.dropdown-menu.show { display: block; }
.dropdown-menu button {
    display: block;
    width: 100%;
    text-align: right;
    padding: 6px 12px;
    background: none;
    border: none;
    color: var(--text);
    cursor: pointer;
    font-size: 13px;
    border-radius: 4px;
    font-family: inherit;
}
.dropdown-menu button:hover { background: var(--select); }
</style>
</head>
<body>
<div id="app">
    <div id="toolbar">
        <button onclick="newFile()">جديد</button>
        <button onclick="openFile()">فتح</button>
        <button onclick="saveFile()">حفظ</button>
        <button onclick="saveAsFile()">حفظ بإسم</button>
        <button class="run-btn" onclick="runCode()">&#9654; تشغيل F5</button>
        <button onclick="clearTerminal()">مسح</button>
        <span style="margin-right:auto; margin-left:8px; color:var(--blue); font-weight:bold; font-size:12px;">Havnix IDE v1.0</span>
    </div>

    <div id="main-area">
        <div id="explorer">
            <div id="explorer-header">
                <span>الملفات</span>
                <button onclick="refreshExplorer()">تحديث</button>
            </div>
            <div id="file-tree"></div>
        </div>
        <div id="explorer-resize"></div>

        <div id="editor-area">
            <div id="editor-tabs"></div>
            <div id="editor-container">
                <div id="editor-wrapper">
                    <div id="highlight-layer"></div>
                    <textarea id="editor" spellcheck="false" dir="rtl"></textarea>
                </div>
                <div id="line-numbers">1</div>
            </div>
        </div>
    </div>

    <div id="resize-handle"></div>

    <div id="bottom-panel">
        <div id="terminal-tabs">
            <div class="term-tab active" data-tab="output" onclick="switchTermTab('output')">المخرجات</div>
            <button class="add-tab" onclick="showNewTabMenu(event)" title="Terminal جديد">+</button>
        </div>
        <div id="terminal-container">
            <div class="terminal-panel active" id="term-output">
                <div class="terminal-output" id="output-text"></div>
            </div>
        </div>
    </div>

    <div id="status-bar">
        <span id="status-text">جاهز</span>
        <span id="cursor-pos">سطر 1, عمود 1</span>
    </div>
</div>

<div class="dropdown-menu" id="new-tab-menu">
    <button onclick="createShellTab('bash')">Bash</button>
    <button onclick="createShellTab('git')">Git Bash</button>
</div>

<script>
// ─── State ───
let currentFile = null;
let isModified = false;
let termTabs = {output: {type: 'output', el: document.getElementById('term-output')}};
let activeTermTab = 'output';
let currentRunId = null;
let shellPollers = {};
let tabCounter = 0;

const editor = document.getElementById('editor');
const highlightLayer = document.getElementById('highlight-layer');
const lineNumbers = document.getElementById('line-numbers');
const outputText = document.getElementById('output-text');

// ─── Syntax Highlighting ───
const HAVNIX_KEYWORDS = [
    'لو', 'غير كدا لو', 'غير كدا', 'طالما', 'لكل', 'في',
    'تكرار', 'كسر', 'تخطى', 'ارجع', 'دالة', 'ثابت',
    'جرب', 'امسك', 'واخيراً', 'استورد', 'صدر'
];
const HAVNIX_BUILTINS = [
    'قول ليهو', 'اطبع', 'جيب لي', 'طول', 'نوع', 'نص', 'رقم', 'عشري',
    'قائمة', 'تقسيم', 'دمج', 'بدل', 'فيهو', 'يبدأ_ب', 'ينتهي_ب',
    'حروف_كبيرة', 'حروف_صغيرة', 'قص_فراغات', 'عكس', 'ترتيب',
    'اضف', 'احذف', 'ادرج', 'مفاتيح', 'قيم', 'عناصر',
    'جذر', 'قوة', 'مطلق', 'تقريب', 'اقصى', 'ادنى', 'مجموع',
    'عشوائي', 'عشوائي_نطاق', 'اختيار_عشوائي',
    'اقرأ_ملف', 'اكتب_ملف', 'اضف_لملف', 'ملف_موجود', 'احذف_ملف',
    'من_json', 'الى_json',
    'اتصل_قاعدة', 'استعلم', 'نفذ_استعلام', 'اقفل_قاعدة',
    'جيب_من', 'رسل_لي', 'حدث_في', 'احذف_من_api',
    'نافذة_جديدة', 'زر', 'نص_ثابت', 'مدخل_نص', 'مساحة_نص',
    'قائمة_اختيار', 'خانة_اختيار', 'شغل_واجهة',
    'الوقت_الحالي', 'انتظر'
];
const HAVNIX_BOOLS = ['صاح', 'غلط', 'فاضي'];

function escapeHtml(text) {
    return text.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

function highlightCode(code) {
    let result = '';
    let i = 0;
    const len = code.length;

    while (i < len) {
        // Comments: //
        if (code[i] === '/' && code[i+1] === '/') {
            let end = code.indexOf('\n', i);
            if (end === -1) end = len;
            result += '<span class="hl-comment">' + escapeHtml(code.substring(i, end)) + '</span>';
            i = end;
            continue;
        }

        // Strings: "..." or '...'
        if (code[i] === '"' || code[i] === "'") {
            const quote = code[i];
            let j = i + 1;
            while (j < len && code[j] !== quote) {
                if (code[j] === '\\') j++;
                j++;
            }
            if (j < len) j++;
            result += '<span class="hl-string">' + escapeHtml(code.substring(i, j)) + '</span>';
            i = j;
            continue;
        }

        // Variables: $...
        if (code[i] === '$') {
            let j = i + 1;
            while (j < len && /[\u0600-\u06FF\u0750-\u077Fa-zA-Z0-9_]/.test(code[j])) j++;
            result += '<span class="hl-variable">' + escapeHtml(code.substring(i, j)) + '</span>';
            i = j;
            continue;
        }

        // Numbers
        if (/[0-9]/.test(code[i])) {
            let j = i;
            while (j < len && /[0-9.]/.test(code[j])) j++;
            result += '<span class="hl-number">' + escapeHtml(code.substring(i, j)) + '</span>';
            i = j;
            continue;
        }

        // Brackets
        if ('(){}[]'.includes(code[i])) {
            result += '<span class="hl-bracket">' + escapeHtml(code[i]) + '</span>';
            i++;
            continue;
        }

        // Operators
        if ('=+-*/<>!&|;,.%:'.includes(code[i])) {
            result += '<span class="hl-operator">' + escapeHtml(code[i]) + '</span>';
            i++;
            continue;
        }

        // Arabic words: check keywords/builtins
        if (/[\u0600-\u06FF\u0750-\u077F]/.test(code[i])) {
            let j = i;
            while (j < len && /[\u0600-\u06FF\u0750-\u077F\s_]/.test(code[j])) j++;
            let word = code.substring(i, j).trimEnd();
            let trailing = code.substring(i + word.length, j);

            let matched = false;
            // Check multi-word builtins first (longest match)
            for (const b of HAVNIX_BUILTINS) {
                if (word === b || word.startsWith(b + ' ') || word.startsWith(b)) {
                    if (code.substring(i, i + b.length) === b) {
                        result += '<span class="hl-builtin">' + escapeHtml(b) + '</span>';
                        i += b.length;
                        matched = true;
                        break;
                    }
                }
            }
            if (matched) continue;

            // Check multi-word keywords
            for (const kw of HAVNIX_KEYWORDS) {
                if (code.substring(i, i + kw.length) === kw) {
                    let afterKw = code[i + kw.length];
                    if (!afterKw || !/[\u0600-\u06FF\u0750-\u077F]/.test(afterKw)) {
                        result += '<span class="hl-keyword">' + escapeHtml(kw) + '</span>';
                        i += kw.length;
                        matched = true;
                        break;
                    }
                }
            }
            if (matched) continue;

            // Check single words
            let wordEnd = i;
            while (wordEnd < len && /[\u0600-\u06FF\u0750-\u077F_0-9]/.test(code[wordEnd])) wordEnd++;
            let singleWord = code.substring(i, wordEnd);

            if (HAVNIX_BOOLS.includes(singleWord)) {
                result += '<span class="hl-bool">' + escapeHtml(singleWord) + '</span>';
            } else if (HAVNIX_KEYWORDS.includes(singleWord)) {
                result += '<span class="hl-keyword">' + escapeHtml(singleWord) + '</span>';
            } else if (HAVNIX_BUILTINS.includes(singleWord)) {
                result += '<span class="hl-builtin">' + escapeHtml(singleWord) + '</span>';
            } else {
                result += '<span class="hl-plain">' + escapeHtml(singleWord) + '</span>';
            }
            i = wordEnd;
            continue;
        }

        // Default
        result += '<span class="hl-plain">' + escapeHtml(code[i]) + '</span>';
        i++;
    }

    return result;
}

function updateHighlight() {
    highlightLayer.innerHTML = highlightCode(editor.value) + '\n';
}

// ─── Editor Events ───
editor.addEventListener('input', () => {
    updateLineNumbers();
    updateHighlight();
    isModified = true;
    updateTitle();
});

editor.addEventListener('keydown', (e) => {
    if (e.key === 'Tab') {
        e.preventDefault();
        const start = editor.selectionStart;
        const end = editor.selectionEnd;
        editor.value = editor.value.substring(0, start) + '    ' + editor.value.substring(end);
        editor.selectionStart = editor.selectionEnd = start + 4;
        editor.dispatchEvent(new Event('input'));
    }
    if (e.key === 'F5') {
        e.preventDefault();
        runCode();
    }
    if (e.ctrlKey && e.key === 's') {
        e.preventDefault();
        saveFile();
    }
    if (e.ctrlKey && e.key === 'o') {
        e.preventDefault();
        openFile();
    }
    if (e.ctrlKey && e.key === 'n') {
        e.preventDefault();
        newFile();
    }
});

editor.addEventListener('scroll', () => {
    lineNumbers.scrollTop = editor.scrollTop;
    highlightLayer.scrollTop = editor.scrollTop;
    highlightLayer.scrollLeft = editor.scrollLeft;
});

editor.addEventListener('click', updateCursorPos);
editor.addEventListener('keyup', updateCursorPos);

function updateLineNumbers() {
    const lines = editor.value.split('\n').length;
    let nums = '';
    for (let i = 1; i <= lines; i++) nums += i + '\n';
    lineNumbers.textContent = nums;
}

function updateCursorPos() {
    const val = editor.value;
    const pos = editor.selectionStart;
    const before = val.substring(0, pos);
    const line = before.split('\n').length;
    const col = pos - before.lastIndexOf('\n');
    document.getElementById('cursor-pos').textContent = '\u0633\u0637\u0631 ' + line + ', \u0639\u0645\u0648\u062f ' + col;
}

function updateTitle() {
    let title = 'Havnix IDE';
    if (currentFile) title += ' - ' + currentFile.split('/').pop().split('\\').pop();
    else title += ' - \u0628\u062f\u0648\u0646 \u0639\u0646\u0648\u0627\u0646';
    if (isModified) title += ' *';
    document.title = title;
}

// ─── File Operations ───
function newFile() {
    if (isModified && !confirm('\u0627\u0644\u062a\u063a\u064a\u064a\u0631\u0627\u062a \u063a\u064a\u0631 \u0645\u062d\u0641\u0648\u0638\u0629. \u0647\u0644 \u062a\u0631\u064a\u062f \u0627\u0644\u0645\u062a\u0627\u0628\u0639\u0629\u061f')) return;
    editor.value = '';
    currentFile = null;
    isModified = false;
    updateTitle();
    updateLineNumbers();
    updateHighlight();
}

async function openFile() {
    const input = document.createElement('input');
    input.type = 'file';
    input.accept = '.havnix,.hx,.txt';
    input.onchange = async (e) => {
        const file = e.target.files[0];
        if (!file) return;
        const text = await file.text();
        editor.value = text;
        currentFile = null;
        isModified = false;
        updateTitle();
        updateLineNumbers();
        updateHighlight();
        setStatus('\u062a\u0645 \u0641\u062a\u062d \u0627\u0644\u0645\u0644\u0641');
    };
    input.click();
}

function openFileFromExplorer(filepath) {
    fetch('/api/read?path=' + encodeURIComponent(filepath))
        .then(r => r.json())
        .then(data => {
            if (data.error) { alert(data.error); return; }
            editor.value = data.content;
            currentFile = data.path;
            isModified = false;
            updateTitle();
            updateLineNumbers();
            updateHighlight();
            setStatus('\u062a\u0645 \u0641\u062a\u062d: ' + filepath.split('/').pop());
        });
}

async function saveFile() {
    if (!currentFile) { saveAsFile(); return; }
    const resp = await fetch('/api/save', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({path: currentFile, content: editor.value})
    });
    const data = await resp.json();
    if (data.success) {
        isModified = false;
        updateTitle();
        setStatus('\u062a\u0645 \u0627\u0644\u062d\u0641\u0638: ' + currentFile.split('/').pop());
    } else {
        alert('\u062e\u0637\u0623: ' + data.error);
    }
}

async function saveAsFile() {
    const name = prompt('\u0627\u0633\u0645 \u0627\u0644\u0645\u0644\u0641:', currentFile ? currentFile.split('/').pop() : 'untitled.havnix');
    if (!name) return;
    let path = name;
    const resp = await fetch('/api/save', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({path: path, content: editor.value})
    });
    const data = await resp.json();
    if (data.success) {
        currentFile = data.path;
        isModified = false;
        updateTitle();
        setStatus('\u062a\u0645 \u0627\u0644\u062d\u0641\u0638: ' + currentFile.split('/').pop());
        refreshExplorer();
    } else {
        alert('\u062e\u0637\u0623: ' + data.error);
    }
}

// ─── Run Code ───
async function runCode() {
    switchTermTab('output');
    clearTerminal();
    appendOutput('\u25b6 \u062a\u0634\u063a\u064a\u0644 \u0627\u0644\u0628\u0631\u0646\u0627\u0645\u062c...\n', 'info');
    setStatus('\u062c\u0627\u0631\u064a \u0627\u0644\u062a\u0634\u063a\u064a\u0644...');

    if (currentFile) {
        await fetch('/api/save', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({path: currentFile, content: editor.value})
        });
    }

    const resp = await fetch('/api/run', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({content: editor.value, filepath: currentFile})
    });
    const data = await resp.json();
    currentRunId = data.run_id;
    pollRunOutput(data.run_id);
}

function pollRunOutput(runId) {
    fetch('/api/run_output?id=' + runId)
        .then(r => r.json())
        .then(data => {
            if (data.status === 'running') {
                setTimeout(() => pollRunOutput(runId), 200);
            } else if (data.status === 'done') {
                if (data.stdout) appendOutput(data.stdout);
                if (data.stderr) appendOutput(data.stderr, 'error');
                if (data.code === 0) {
                    appendOutput('\n--- \u0627\u0646\u062a\u0647\u0649 \u0627\u0644\u062a\u0634\u063a\u064a\u0644 \u0628\u0646\u062c\u0627\u062d ---\n', 'success');
                    setStatus('\u062a\u0645 \u0627\u0644\u062a\u0634\u063a\u064a\u0644 \u0628\u0646\u062c\u0627\u062d');
                } else {
                    appendOutput('\n--- \u062e\u0637\u0623 (\u0643\u0648\u062f: ' + data.code + ') ---\n', 'error');
                    setStatus('\u062e\u0637\u0623 \u0641\u064a \u0627\u0644\u062a\u0634\u063a\u064a\u0644');
                }
                currentRunId = null;
            } else if (data.status === 'timeout') {
                appendOutput('\n--- \u0627\u0646\u062a\u0647\u062a \u0627\u0644\u0645\u0647\u0644\u0629 (30 \u062b\u0627\u0646\u064a\u0629) ---\n', 'error');
                setStatus('\u0627\u0646\u062a\u0647\u062a \u0627\u0644\u0645\u0647\u0644\u0629');
                currentRunId = null;
            } else if (data.status === 'error') {
                appendOutput('\n\u062e\u0637\u0623: ' + data.stderr + '\n', 'error');
                setStatus('\u062e\u0637\u0623');
                currentRunId = null;
            } else {
                setTimeout(() => pollRunOutput(runId), 500);
            }
        })
        .catch(() => setTimeout(() => pollRunOutput(runId), 1000));
}

// ─── Terminal ───
function appendOutput(text, cls) {
    const span = document.createElement('span');
    if (cls) span.className = cls;
    span.textContent = text;
    outputText.appendChild(span);
    outputText.scrollTop = outputText.scrollHeight;
}

function clearTerminal() {
    outputText.innerHTML = '';
}

function setStatus(text) {
    document.getElementById('status-text').textContent = text;
}

// ─── Terminal Tabs ───
function switchTermTab(id) {
    document.querySelectorAll('.term-tab').forEach(t => t.classList.remove('active'));
    document.querySelectorAll('.terminal-panel').forEach(p => p.classList.remove('active'));

    const tab = document.querySelector('.term-tab[data-tab="' + id + '"]');
    if (tab) tab.classList.add('active');

    const panel = document.getElementById('term-' + id);
    if (panel) panel.classList.add('active');

    activeTermTab = id;
}

function showNewTabMenu(e) {
    e.stopPropagation();
    e.preventDefault();
    const menu = document.getElementById('new-tab-menu');
    const rect = e.target.getBoundingClientRect();
    menu.style.top = (rect.bottom + 2) + 'px';
    menu.style.left = rect.left + 'px';
    menu.style.right = 'auto';
    menu.classList.toggle('show');
}

document.addEventListener('click', (e) => {
    const menu = document.getElementById('new-tab-menu');
    if (!menu.contains(e.target) && !e.target.classList.contains('add-tab')) {
        menu.classList.remove('show');
    }
});

async function createShellTab(type) {
    document.getElementById('new-tab-menu').classList.remove('show');
    tabCounter++;
    const id = type + '_' + tabCounter;
    const label = type === 'bash' ? 'Bash' : type === 'git' ? 'Git' : type;

    const tabBar = document.getElementById('terminal-tabs');
    const addBtn = tabBar.querySelector('.add-tab');
    const tab = document.createElement('div');
    tab.className = 'term-tab';
    tab.dataset.tab = id;
    const tabLabel = document.createElement('span');
    tabLabel.textContent = label;
    tabLabel.onclick = function() { switchTermTab(id); };
    const closeBtn = document.createElement('span');
    closeBtn.className = 'close-tab';
    closeBtn.innerHTML = '&times;';
    closeBtn.onclick = function(ev) { closeShellTab(id, ev); };
    tab.appendChild(tabLabel);
    tab.appendChild(closeBtn);
    tab.onclick = function() { switchTermTab(id); };
    tabBar.insertBefore(tab, addBtn);

    const container = document.getElementById('terminal-container');
    const panel = document.createElement('div');
    panel.className = 'terminal-panel';
    panel.id = 'term-' + id;

    const outDiv = document.createElement('div');
    outDiv.className = 'terminal-output';
    outDiv.id = 'shell-output-' + id;
    panel.appendChild(outDiv);

    const inputRow = document.createElement('div');
    inputRow.className = 'terminal-input-row';
    const promptSign = document.createElement('span');
    promptSign.className = 'prompt-sign';
    promptSign.textContent = '$';
    inputRow.appendChild(promptSign);
    const inputEl = document.createElement('input');
    inputEl.type = 'text';
    inputEl.id = 'shell-input-' + id;
    inputEl.placeholder = '\u0627\u0643\u062a\u0628 \u0623\u0645\u0631...';
    inputEl.onkeydown = function(ev) { if (ev.key === 'Enter') sendShellInput(id); };
    inputRow.appendChild(inputEl);
    panel.appendChild(inputRow);

    container.appendChild(panel);

    termTabs[id] = {type: 'shell', el: panel};
    switchTermTab(id);

    const resp = await fetch('/api/shell_create', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({id: id, type: type})
    });
    const data = await resp.json();
    if (data.success) {
        pollShellOutput(id);
        document.getElementById('shell-input-' + id).focus();
    }
}

function pollShellOutput(id) {
    if (!termTabs[id]) return;
    fetch('/api/shell_output?id=' + id)
        .then(r => r.json())
        .then(data => {
            if (data.output) {
                const el = document.getElementById('shell-output-' + id);
                if (el) {
                    const span = document.createElement('span');
                    span.textContent = data.output;
                    el.appendChild(span);
                    el.scrollTop = el.scrollHeight;
                }
            }
            shellPollers[id] = setTimeout(() => pollShellOutput(id), 300);
        })
        .catch(() => {
            shellPollers[id] = setTimeout(() => pollShellOutput(id), 1000);
        });
}

async function sendShellInput(id) {
    const input = document.getElementById('shell-input-' + id);
    const text = input.value;
    input.value = '';

    await fetch('/api/shell_input', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({id: id, text: text})
    });
}

async function closeShellTab(id, e) {
    if (e) e.stopPropagation();

    await fetch('/api/shell_kill', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({id: id})
    });

    if (shellPollers[id]) clearTimeout(shellPollers[id]);
    delete shellPollers[id];
    delete termTabs[id];

    const tab = document.querySelector('.term-tab[data-tab="' + id + '"]');
    if (tab) tab.remove();
    const panel = document.getElementById('term-' + id);
    if (panel) panel.remove();

    switchTermTab('output');
}

// ─── File Explorer ───
function refreshExplorer() {
    fetch('/api/files')
        .then(r => r.json())
        .then(data => {
            const tree = document.getElementById('file-tree');
            tree.innerHTML = '';
            renderTree(data.tree, tree, 0);
        });
}

function renderTree(items, parent, depth) {
    for (const item of items) {
        if (item.type === 'dir') {
            const div = document.createElement('div');
            div.className = 'tree-dir';

            const label = document.createElement('div');
            label.className = 'tree-item';
            label.style.paddingRight = (8 + depth * 16) + 'px';
            label.innerHTML = '<span class="arrow">&#9654;</span><span class="icon">\ud83d\udcc1</span><span>' + item.name + '</span>';
            label.onclick = () => div.classList.toggle('open');
            div.appendChild(label);

            const children = document.createElement('div');
            children.className = 'tree-children';
            renderTree(item.children || [], children, depth + 1);
            div.appendChild(children);

            parent.appendChild(div);
        } else {
            const div = document.createElement('div');
            div.className = 'tree-item';
            div.style.paddingRight = (8 + depth * 16) + 'px';

            let icon = '\ud83d\udcc4';
            if (item.name.endsWith('.havnix')) icon = '\ud83d\udcdc';
            else if (item.name.endsWith('.py')) icon = '\ud83d\udc0d';
            else if (item.name.endsWith('.md')) icon = '\ud83d\udcdd';

            div.innerHTML = '<span class="icon">' + icon + '</span><span>' + item.name + '</span>';
            div.onclick = () => {
                document.querySelectorAll('.tree-item').forEach(t => t.classList.remove('active'));
                div.classList.add('active');
                openFileFromExplorer(item.path);
            };
            parent.appendChild(div);
        }
    }
}

// ─── Resize Handles ───
(function setupResize() {
    const handle = document.getElementById('resize-handle');
    const bottomPanel = document.getElementById('bottom-panel');
    let startY, startH;

    handle.addEventListener('mousedown', (e) => {
        startY = e.clientY;
        startH = bottomPanel.offsetHeight;
        document.addEventListener('mousemove', onResizeV);
        document.addEventListener('mouseup', () => document.removeEventListener('mousemove', onResizeV));
    });

    function onResizeV(e) {
        const diff = startY - e.clientY;
        bottomPanel.style.height = Math.max(100, startH + diff) + 'px';
    }

    const expResize = document.getElementById('explorer-resize');
    const explorer = document.getElementById('explorer');
    let startX, startW;

    expResize.addEventListener('mousedown', (e) => {
        startX = e.clientX;
        startW = explorer.offsetWidth;
        document.addEventListener('mousemove', onResizeH);
        document.addEventListener('mouseup', () => document.removeEventListener('mousemove', onResizeH));
    });

    function onResizeH(e) {
        const diff = e.clientX - startX;
        explorer.style.width = Math.max(120, startW + diff) + 'px';
    }
})();

// ─── Init ───
function init() {
    editor.value = '// \u0645\u0631\u062d\u0628\u0627 \u0628\u0643 \u0641\u064a \u0647\u0627\u0641\u0646\u064a\u0643\u0633! \ud83c\uddf8\ud83c\udde9\n// \u0627\u0643\u062a\u0628 \u0643\u0648\u062f \u0647\u0627\u0641\u0646\u064a\u0643\u0633 \u0647\u0646\u0627 \u0648\u0627\u0636\u063a\u0637 F5 \u0644\u0644\u062a\u0634\u063a\u064a\u0644\n\n$\u0627\u0644\u0627\u0633\u0645 = "\u0639\u062b\u0645\u0627\u0646";\n$\u0627\u0644\u0639\u0645\u0631 = 18;\n\n\u0642\u0648\u0644 \u0644\u064a\u0647\u0648("\u0645\u0631\u062d\u0628\u0627 \u064a\u0627 $\u0627\u0644\u0627\u0633\u0645!");\n\u0642\u0648\u0644 \u0644\u064a\u0647\u0648("\u0639\u0645\u0631\u0643 $\u0627\u0644\u0639\u0645\u0631 \u0633\u0646\u0629");\n\n\u0644\u0648 ($\u0627\u0644\u0639\u0645\u0631 >= 18) {\n    \u0642\u0648\u0644 \u0644\u064a\u0647\u0648("\u0627\u0646\u062a \u0643\u0628\u064a\u0631 \ud83d\udcaa");\n}\n\n$\u0641\u0648\u0627\u0643\u0647 = ["\u062a\u0641\u0627\u062d", "\u0645\u0648\u0632", "\u0628\u0631\u062a\u0642\u0627\u0644"];\n\u0644\u0643\u0644 $\u0641\u0627\u0643\u0647\u0629 \u0641\u064a $\u0641\u0648\u0627\u0643\u0647 {\n    \u0642\u0648\u0644 \u0644\u064a\u0647\u0648("\u0641\u0627\u0643\u0647\u0629: $\u0641\u0627\u0643\u0647\u0629");\n}\n\n\u062f\u0627\u0644\u0629 \u0645\u0631\u062d\u0628\u0627(\u0627\u0644\u0627\u0633\u0645) {\n    \u0642\u0648\u0644 \u0644\u064a\u0647\u0648("\u0627\u0647\u0644\u0627 \u064a\u0627 $\u0627\u0644\u0627\u0633\u0645!");\n}\n\u062c\u064a\u0628 \u0644\u064a \u0645\u0631\u062d\u0628\u0627("\u0627\u062d\u0645\u062f");\n';
    updateLineNumbers();
    updateHighlight();
    refreshExplorer();
    updateTitle();
}

init();
</script>
</body>
</html>'''


class ThreadedHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    allow_reuse_address = True
    daemon_threads = True


def main():
    port = PORT
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            pass

    server = ThreadedHTTPServer(('0.0.0.0', port), IDEHandler)
    url = f'http://localhost:{port}'

    print(f"""
╔══════════════════════════════════════════╗
║       Havnix IDE v3.0                    ║
║   بيئة تطوير متكاملة للغة هافنيكس            ║
╠══════════════════════════════════════════╣
║   {url:<37s}                             ║
║   اضغط Ctrl+C للإيقاف                     ║
╚══════════════════════════════════════════╝
""")

    threading.Timer(0.5, lambda: webbrowser.open(url)).start()

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nجاري الإيقاف...")
        shell_manager.kill_all()
        server.shutdown()


if __name__ == '__main__':
    main()
