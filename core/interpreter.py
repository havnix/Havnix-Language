import re
import os
import sys
import math
import random
import json

from core.expressions import evaluate_expression, tokenize, ExpressionParser, HavnixExpressionError


class HavnixBreak(Exception):
    pass


class HavnixContinue(Exception):
    pass


class HavnixReturn(Exception):
    def __init__(self, value=None):
        self.value = value


class HavnixError(Exception):
    def __init__(self, message, line_num=None):
        self.message = message
        self.line_num = line_num
        super().__init__(message)


class HavnixInterpreter:
    def __init__(self):
        self.global_vars = {}
        self.functions = {}
        self.db_connections = {}
        self.gui_windows = {}
        self.gui_elements = {}
        self.base_dir = '.'
        self._init_builtin_funcs()

    def _init_builtin_funcs(self):
        self.builtin_funcs = {
            'طول': self._fn_length,
            'قطع': self._fn_substring,
            'بدل': self._fn_replace,
            'قسم': self._fn_split,
            'كبر': self._fn_upper,
            'صغر': self._fn_lower,
            'فيهو': self._fn_contains,
            'ضم': self._fn_join,
            'جذر': self._fn_sqrt,
            'قوة': self._fn_power,
            'مطلق': self._fn_abs,
            'عشوائي': self._fn_random,
            'تقريب': self._fn_round,
            'اكبر': self._fn_max,
            'اصغر': self._fn_min,
            'رقم': self._fn_to_int,
            'عشري': self._fn_to_float,
            'نص': self._fn_to_str,
            'منطقي': self._fn_to_bool,
            'نوع': self._fn_type,
            'مفاتيح': self._fn_keys,
            'قيم': self._fn_values,
            'اضف': self._fn_append,
            'احذف_عنصر': self._fn_remove,
            'ترتيب': self._fn_sort,
            'عكس': self._fn_reverse,
            'نطاق': self._fn_range,
            'json_حلل': self._fn_json_parse,
            'json_نص': self._fn_json_stringify,
        }

    def run(self, filename):
        self.base_dir = os.path.dirname(os.path.abspath(filename))
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                source = f.read()
        except FileNotFoundError:
            print(f"خطأ: الملف '{filename}' غير موجود")
            sys.exit(1)

        lines = self._preprocess(source)
        try:
            self._execute_block(lines, self.global_vars)
        except HavnixError as e:
            if e.line_num:
                print(f"خطأ في السطر {e.line_num}: {e.message}")
            else:
                print(f"خطأ: {e.message}")
        except HavnixReturn as e:
            pass
        except Exception as e:
            print(f"خطأ غير متوقع: {e}")

    def _preprocess(self, source):
        lines = source.split('\n')
        cleaned = []
        in_block_comment = False
        for line in lines:
            stripped = line.strip()
            if stripped.startswith('/*'):
                in_block_comment = True
                if '*/' in stripped[2:]:
                    in_block_comment = False
                continue
            if in_block_comment:
                if '*/' in stripped:
                    in_block_comment = False
                continue
            if stripped.startswith('//'):
                continue
            if '//' in stripped:
                quote_count = 0
                cut_pos = -1
                for idx, ch in enumerate(stripped):
                    if ch in ('"', "'"):
                        quote_count += 1
                    if ch == '/' and idx + 1 < len(stripped) and stripped[idx + 1] == '/' and quote_count % 2 == 0:
                        cut_pos = idx
                        break
                if cut_pos >= 0:
                    stripped = stripped[:cut_pos].rstrip()
            cleaned.append(stripped)

        result = []
        i = 0
        while i < len(cleaned):
            line = cleaned[i]
            is_assignment = bool(re.match(r'^\$\w+\s*=', line) or line.startswith('ثابت '))
            if is_assignment:
                bracket_count = line.count('[') - line.count(']')
                eq_pos = line.index('=')
                rhs = line[eq_pos + 1:]
                paren_count = rhs.count('(') - rhs.count(')')
                brace_count = 0
                for ch in rhs:
                    if ch == '{':
                        brace_count += 1
                    elif ch == '}':
                        brace_count -= 1
                while (bracket_count > 0 or brace_count > 0 or paren_count > 0) and i + 1 < len(cleaned):
                    i += 1
                    next_line = cleaned[i]
                    line = line + ' ' + next_line
                    bracket_count += next_line.count('[') - next_line.count(']')
                    paren_count += next_line.count('(') - next_line.count(')')
                    for ch in next_line:
                        if ch == '{':
                            brace_count += 1
                        elif ch == '}':
                            brace_count -= 1
            result.append(line)
            i += 1
        return result

    def _find_block_end(self, lines, start):
        brace_count = 0
        i = start
        while i < len(lines):
            line = lines[i]
            for ch in line:
                if ch == '{':
                    brace_count += 1
                elif ch == '}':
                    brace_count -= 1
                    if brace_count == 0:
                        return i
            i += 1
        return len(lines) - 1

    def _extract_block_lines(self, lines, start):
        end = self._find_block_end(lines, start)
        block = []
        for i in range(start + 1, end):
            line = lines[i].strip()
            if line and line != '{':
                block.append(line)
        first_line = lines[start]
        brace_pos = first_line.find('{')
        if brace_pos > 0:
            after_brace = first_line[brace_pos + 1:].strip()
            if after_brace and after_brace != '}':
                block.insert(0, after_brace)
        return block, end

    def _execute_block(self, lines, scope):
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if not line or line == '{' or line == '}':
                i += 1
                continue
            i = self._execute_line(line, lines, i, scope)
            i += 1

    def _execute_line(self, line, lines, index, scope):
        line = line.strip()
        if not line or line == '{' or line == '}':
            return index

        if line.startswith('قول ليهو') or line.startswith('اطبع'):
            self._cmd_print(line, scope)
        elif line.startswith('$') and '=' in line:
            if self._is_special_assignment(line):
                self._handle_special_assignment(line, scope)
            else:
                self._cmd_assign(line, scope)
        elif line.startswith('ثابت '):
            self._cmd_const_assign(line, scope)
        elif line.startswith('لو ') or line.startswith('لو('):
            return self._cmd_if(line, lines, index, scope)
        elif line.startswith('طالما'):
            return self._cmd_while(line, lines, index, scope)
        elif line.startswith('لكل'):
            return self._cmd_foreach(line, lines, index, scope)
        elif line.startswith('تكرار'):
            return self._cmd_for(line, lines, index, scope)
        elif line.startswith('دالة '):
            return self._cmd_func_def(line, lines, index, scope)
        elif line.startswith('جيب لي ') or line.startswith('جيب_لي '):
            self._cmd_func_call(line, scope)
        elif line.startswith('رجع'):
            self._cmd_return(line, scope)
        elif line.startswith('اقيف'):
            raise HavnixBreak()
        elif line.startswith('كمل'):
            raise HavnixContinue()
        elif line.startswith('جرب'):
            return self._cmd_try(line, lines, index, scope)
        elif line.startswith('داير '):
            self._cmd_import(line, scope)
        elif line.startswith('اسأل') or line.startswith('اسال'):
            self._cmd_input(line, scope)
        elif line.startswith('اتصل_قاعدة'):
            self._cmd_db_connect(line, scope)
        elif line.startswith('استعلم'):
            self._cmd_db_query(line, scope)
        elif line.startswith('نفذ_استعلام'):
            self._cmd_db_execute(line, scope)
        elif line.startswith('اقفل_قاعدة'):
            self._cmd_db_close(line, scope)
        elif line.startswith('جيب_من') or line.startswith('رسل_لي') or line.startswith('حدث_في') or line.startswith('احذف_من_api'):
            self._cmd_http(line, scope)
        elif line.startswith('نافذة_جديدة'):
            self._cmd_gui_window(line, scope)
        elif line.startswith('زر'):
            self._cmd_gui_button(line, scope)
        elif line.startswith('نص_ثابت'):
            self._cmd_gui_label(line, scope)
        elif line.startswith('مدخل_نص'):
            self._cmd_gui_entry(line, scope)
        elif line.startswith('مساحة_نص'):
            self._cmd_gui_textarea(line, scope)
        elif line.startswith('قائمة_اختيار'):
            self._cmd_gui_dropdown(line, scope)
        elif line.startswith('خانة_اختيار'):
            self._cmd_gui_checkbox(line, scope)
        elif line.startswith('شغل_واجهة'):
            self._cmd_gui_run(line, scope)
        elif line.startswith('اقرأ_ملف') or line.startswith('اقرا_ملف'):
            self._cmd_read_file(line, scope)
        elif line.startswith('اكتب_ملف'):
            self._cmd_write_file(line, scope)
        elif line.startswith('ضيف_ملف'):
            self._cmd_append_file(line, scope)
        elif line.startswith('احذف_ملف'):
            self._cmd_delete_file(line, scope)
        elif line == 'انتهى' or line == 'انتهى;':
            pass
        elif re.match(r'^\w', line) and '(' in line:
            self._cmd_func_call_direct(line, scope)
        else:
            pass

        return index

    _SPECIAL_CMDS = [
        'اتصل_قاعدة', 'استعلم', 'نفذ_استعلام',
        'جيب_من', 'رسل_لي', 'حدث_في', 'احذف_من_api',
        'نافذة_جديدة', 'مدخل_نص', 'مساحة_نص', 'قائمة_اختيار', 'خانة_اختيار',
        'اقرأ_ملف', 'اقرا_ملف',
        'اسأل', 'اسال',
    ]

    def _is_special_assignment(self, line):
        eq_pos = line.index('=')
        rhs = line[eq_pos + 1:].strip()
        for cmd in self._SPECIAL_CMDS:
            if rhs.startswith(cmd):
                return True
        return False

    def _handle_special_assignment(self, line, scope):
        eq_pos = line.index('=')
        rhs = line[eq_pos + 1:].strip()

        if rhs.startswith('اتصل_قاعدة'):
            self._cmd_db_connect(line, scope)
        elif rhs.startswith('استعلم'):
            self._cmd_db_query(line, scope)
        elif rhs.startswith('جيب_من') or rhs.startswith('رسل_لي') or rhs.startswith('حدث_في') or rhs.startswith('احذف_من_api'):
            self._cmd_http(line, scope)
        elif rhs.startswith('نافذة_جديدة'):
            self._cmd_gui_window(line, scope)
        elif rhs.startswith('مدخل_نص'):
            self._cmd_gui_entry(line, scope)
        elif rhs.startswith('مساحة_نص'):
            self._cmd_gui_textarea(line, scope)
        elif rhs.startswith('قائمة_اختيار'):
            self._cmd_gui_dropdown(line, scope)
        elif rhs.startswith('خانة_اختيار'):
            self._cmd_gui_checkbox(line, scope)
        elif rhs.startswith('اقرأ_ملف') or rhs.startswith('اقرا_ملف'):
            self._cmd_read_file(line, scope)
        elif rhs.startswith('اسأل') or rhs.startswith('اسال'):
            self._cmd_input(line, scope)
        else:
            self._cmd_assign(line, scope)

    def _eval(self, expr, scope):
        def user_func_caller(name, args):
            return self._call_function_with_return(name, args, scope)
        return evaluate_expression(expr, scope, self.builtin_funcs, user_func_caller)

    def _interpolate(self, text, scope):
        def replace_indexed(match):
            var_name = match.group(1)
            idx = match.group(2)
            val = scope.get(var_name, f"${var_name}")
            try:
                if isinstance(val, list):
                    val = val[int(idx)]
                elif isinstance(val, dict):
                    key = int(idx) if idx.isdigit() else idx
                    val = val[key]
            except (IndexError, KeyError):
                pass
            return str(val)

        text = re.sub(r'\$(\w+)\[(\w+)\]', replace_indexed, text)
        text = re.sub(r'\$(\w+)', lambda m: str(scope.get(m.group(1), '$' + m.group(1))), text)
        return text

    # ─── Print ───

    def _format_value(self, value):
        if isinstance(value, bool):
            return 'صاح' if value else 'غلط'
        if value is None:
            return 'فاضي'
        if isinstance(value, list):
            return '[' + ', '.join(self._format_value(v) for v in value) + ']'
        if isinstance(value, dict):
            return json.dumps(value, ensure_ascii=False, indent=2)
        return str(value)

    def _cmd_print(self, line, scope):
        match = re.match(r'(?:قول ليهو|اطبع)\s*\(\s*(.+)\s*\)\s*;?\s*$', line)
        if match:
            expr = match.group(1).strip()
            if (expr.startswith('"') and expr.endswith('"')) or (expr.startswith("'") and expr.endswith("'")):
                text = expr[1:-1]
                text = self._interpolate(text, scope)
                print(text)
            else:
                try:
                    value = self._eval(expr, scope)
                    print(self._format_value(value))
                except Exception:
                    text = self._interpolate(expr, scope)
                    print(text)
        else:
            print("خطأ في أمر الطباعة:", line)

    # ─── Variables ───

    def _cmd_assign(self, line, scope):
        match = re.match(r'\$(\w+)\s*\[(.+?)\]\s*=\s*(.+?)\s*;?\s*$', line)
        if match:
            var_name = match.group(1)
            index_expr = match.group(2).strip()
            value_expr = match.group(3).strip()
            index = self._eval(index_expr, scope)
            value = self._eval(value_expr, scope)
            if var_name in scope:
                container = scope[var_name]
                if isinstance(container, list):
                    container[int(index)] = value
                elif isinstance(container, dict):
                    container[index] = value
            return

        match = re.match(r'\$(\w+)\s*=\s*(.+?)\s*;?\s*$', line)
        if match:
            var_name = match.group(1)
            value_expr = match.group(2).strip()
            try:
                value = self._eval(value_expr, scope)
            except Exception:
                value = value_expr.strip('"').strip("'")
            scope[var_name] = value
        else:
            print("خطأ في تعريف المتغير:", line)

    def _cmd_const_assign(self, line, scope):
        match = re.match(r'ثابت\s+\$(\w+)\s*=\s*(.+?)\s*;?\s*$', line)
        if match:
            var_name = match.group(1)
            if var_name in scope:
                print(f"خطأ: الثابت '${var_name}' تم تعريفه مسبقاً ولا يمكن تغييره")
                return
            value_expr = match.group(2).strip()
            scope[var_name] = self._eval(value_expr, scope)

    # ─── If/Elif/Else ───

    def _cmd_if(self, line, lines, index, scope):
        match = re.match(r'لو\s*\((.+?)\)\s*\{', line)
        if not match:
            print("خطأ في جملة لو:", line)
            return index

        condition = match.group(1).strip()
        block_lines, block_end = self._extract_block_lines(lines, index)

        result = bool(self._eval(condition, scope))
        executed = False

        if result:
            self._execute_block(block_lines, scope)
            executed = True

        index = block_end

        while index + 1 < len(lines):
            next_line = lines[index + 1].strip()

            elif_match = re.match(r'(?:غير كدا لو|ولو)\s*\((.+?)\)\s*\{', next_line)
            if elif_match:
                index += 1
                elif_block, elif_end = self._extract_block_lines(lines, index)
                if not executed:
                    elif_cond = elif_match.group(1).strip()
                    if bool(self._eval(elif_cond, scope)):
                        self._execute_block(elif_block, scope)
                        executed = True
                index = elif_end
                continue

            else_match = re.match(r'غير كدا\s*\{', next_line)
            if else_match:
                index += 1
                else_block, else_end = self._extract_block_lines(lines, index)
                if not executed:
                    self._execute_block(else_block, scope)
                index = else_end
                break

            break

        return index

    # ─── While Loop ───

    def _cmd_while(self, line, lines, index, scope):
        match = re.match(r'طالما\s*\((.+?)\)\s*\{', line)
        if not match:
            print("خطأ في حلقة طالما:", line)
            return index

        condition = match.group(1).strip()
        block_lines, block_end = self._extract_block_lines(lines, index)

        max_iter = 100000
        count = 0
        while bool(self._eval(condition, scope)) and count < max_iter:
            try:
                self._execute_block(block_lines, scope)
            except HavnixBreak:
                break
            except HavnixContinue:
                continue
            count += 1

        return block_end

    # ─── For-each Loop ───

    def _cmd_foreach(self, line, lines, index, scope):
        match = re.match(r'لكل\s+\$(\w+)\s+في\s+(.+?)\s*\{', line)
        if not match:
            print("خطأ في حلقة لكل:", line)
            return index

        var_name = match.group(1)
        iterable_expr = match.group(2).strip()
        block_lines, block_end = self._extract_block_lines(lines, index)

        iterable = self._eval(iterable_expr, scope)
        if not hasattr(iterable, '__iter__'):
            print(f"خطأ: القيمة غير قابلة للتكرار")
            return block_end

        items = iterable
        if isinstance(iterable, dict):
            items = list(iterable.keys())

        for item in items:
            scope[var_name] = item
            try:
                self._execute_block(block_lines, scope)
            except HavnixBreak:
                break
            except HavnixContinue:
                continue

        return block_end

    # ─── For Loop ───

    def _cmd_for(self, line, lines, index, scope):
        match = re.match(r'تكرار\s*\((.+?);(.+?);(.+?)\)\s*\{?', line)
        if not match:
            print("خطأ في حلقة تكرار:", line)
            return index

        init_stmt = match.group(1).strip()
        condition = match.group(2).strip()
        increment = match.group(3).strip()

        if '{' in line:
            block_lines, block_end = self._extract_block_lines(lines, index)
        else:
            block_lines = []
            block_end = index + 1
            while block_end < len(lines):
                bl = lines[block_end].strip()
                if bl == 'انتهى' or bl == '}':
                    break
                if bl:
                    block_lines.append(bl)
                block_end += 1

        self._execute_line(init_stmt, lines, index, scope)

        max_iter = 100000
        count = 0
        while bool(self._eval(condition, scope)) and count < max_iter:
            try:
                self._execute_block(block_lines, scope)
            except HavnixBreak:
                break
            except HavnixContinue:
                pass
            self._execute_line(increment, lines, index, scope)
            count += 1

        return block_end

    # ─── Functions ───

    def _cmd_func_def(self, line, lines, index, scope):
        match = re.match(r'دالة\s+(\w+)\s*\((.*?)\)\s*\{', line)
        if not match:
            print("خطأ في تعريف الدالة:", line)
            return index

        func_name = match.group(1)
        params_str = match.group(2).strip()
        params = [p.strip() for p in params_str.split(',') if p.strip()] if params_str else []
        block_lines, block_end = self._extract_block_lines(lines, index)

        self.functions[func_name] = {
            'params': params,
            'body': block_lines
        }

        return block_end

    def _cmd_func_call(self, line, scope):
        match = re.match(r'(?:جيب لي|جيب_لي)\s+(\w+)\s*\((.*?)\)\s*;?\s*$', line)
        if not match:
            print("خطأ في استدعاء الدالة:", line)
            return

        func_name = match.group(1)
        args_str = match.group(2).strip()
        args = self._parse_args(args_str, scope)

        self._call_function(func_name, args, scope)

    def _cmd_func_call_direct(self, line, scope):
        match = re.match(r'(\w+)\s*\((.*?)\)\s*;?\s*$', line)
        if match:
            func_name = match.group(1)
            args_str = match.group(2).strip()
            if func_name in self.functions:
                args = self._parse_args(args_str, scope)
                self._call_function(func_name, args, scope)
            elif func_name in self.builtin_funcs:
                args = self._parse_args(args_str, scope)
                self.builtin_funcs[func_name](*args)

    def _call_function(self, func_name, args, scope):
        if func_name not in self.functions:
            print(f"خطأ: الدالة '{func_name}' غير موجودة")
            return None

        func = self.functions[func_name]
        local_scope = scope.copy()

        for i, param in enumerate(func['params']):
            if i < len(args):
                local_scope[param] = args[i]
            else:
                local_scope[param] = None

        try:
            self._execute_block(func['body'], local_scope)
        except HavnixReturn as ret:
            return ret.value
        return None

    def _call_function_with_return(self, func_name, args, scope):
        if func_name in self.builtin_funcs:
            return self.builtin_funcs[func_name](*args)

        if func_name not in self.functions:
            raise HavnixExpressionError(f"الدالة '{func_name}' غير موجودة")

        func = self.functions[func_name]
        local_scope = scope.copy()

        for i, param in enumerate(func['params']):
            if i < len(args):
                local_scope[param] = args[i]
            else:
                local_scope[param] = None

        try:
            self._execute_block(func['body'], local_scope)
        except HavnixReturn as ret:
            return ret.value
        return None

    def _parse_args(self, args_str, scope):
        if not args_str:
            return []
        args = []
        current = ''
        depth = 0
        in_str = False
        str_char = ''
        for ch in args_str:
            if in_str:
                current += ch
                if ch == str_char:
                    in_str = False
                continue
            if ch in ('"', "'"):
                in_str = True
                str_char = ch
                current += ch
            elif ch in ('(', '[', '{'):
                depth += 1
                current += ch
            elif ch in (')', ']', '}'):
                depth -= 1
                current += ch
            elif ch == ',' and depth == 0:
                args.append(current.strip())
                current = ''
            else:
                current += ch
        if current.strip():
            args.append(current.strip())

        result = []
        for arg in args:
            try:
                result.append(self._eval(arg, scope))
            except Exception:
                result.append(arg.strip('"').strip("'"))
        return result

    def _cmd_return(self, line, scope):
        match = re.match(r'رجع\s*(.*?)\s*;?\s*$', line)
        if match:
            value_expr = match.group(1).strip()
            if value_expr:
                value = self._eval(value_expr, scope)
            else:
                value = None
            raise HavnixReturn(value)

    # ─── Try/Catch ───

    def _cmd_try(self, line, lines, index, scope):
        try_block, try_end = self._extract_block_lines(lines, index)

        catch_block = None
        catch_end = try_end
        catch_var = None
        finally_block = None
        finally_end = try_end

        if try_end + 1 < len(lines):
            next_line = lines[try_end + 1].strip()
            catch_match = re.match(r'(?:امسك|لو_فشل)\s*\(\s*\$?(\w+)\s*\)\s*\{', next_line)
            if catch_match:
                catch_var = catch_match.group(1)
                catch_block, catch_end = self._extract_block_lines(lines, try_end + 1)
            elif re.match(r'(?:امسك|لو_فشل)\s*\{', next_line):
                catch_block, catch_end = self._extract_block_lines(lines, try_end + 1)

        final_end = catch_end if catch_block else try_end
        if final_end + 1 < len(lines):
            next_line = lines[final_end + 1].strip()
            if re.match(r'(?:واخيراً|واخيرا|دايماً|دايما)\s*\{', next_line):
                finally_block, finally_end = self._extract_block_lines(lines, final_end + 1)
                final_end = finally_end

        try:
            self._execute_block(try_block, scope)
        except (HavnixBreak, HavnixContinue, HavnixReturn):
            if finally_block:
                self._execute_block(finally_block, scope)
            raise
        except Exception as e:
            if catch_block:
                if catch_var:
                    scope[catch_var] = str(e)
                self._execute_block(catch_block, scope)
            else:
                if finally_block:
                    self._execute_block(finally_block, scope)
                raise

        if finally_block:
            self._execute_block(finally_block, scope)

        return final_end

    # ─── Import ───

    def _cmd_import(self, line, scope):
        match = re.match(r'داير\s+"(.+?)"\s*;?\s*$', line)
        if not match:
            print("خطأ في أمر الاستيراد:", line)
            return

        file_path = match.group(1)
        if not file_path.endswith('.havnix'):
            file_path += '.havnix'

        search_paths = [
            os.path.join(self.base_dir, file_path),
            file_path,
            os.path.join(self.base_dir, 'include', file_path),
            os.path.join(self.base_dir, 'lib', file_path),
            os.path.join(self.base_dir, 'src', file_path),
        ]

        for path in search_paths:
            if os.path.isfile(path):
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        source = f.read()
                    imported_lines = self._preprocess(source)
                    self._execute_block(imported_lines, scope)
                except Exception as e:
                    print(f"خطأ في استيراد الملف '{file_path}': {e}")
                return

        print(f"خطأ: ما قدرت استعدي الملف '{file_path}' لأني ما لقيتو")

    # ─── Input ───

    def _cmd_input(self, line, scope):
        match = re.match(r'(?:اسأل|اسال)\s*\(\s*\$(\w+)\s*,\s*(.+?)\s*\)\s*;?\s*$', line)
        if match:
            var_name = match.group(1)
            prompt_expr = match.group(2).strip()
            if (prompt_expr.startswith('"') and prompt_expr.endswith('"')) or \
               (prompt_expr.startswith("'") and prompt_expr.endswith("'")):
                prompt = self._interpolate(prompt_expr[1:-1], scope)
            else:
                prompt = str(self._eval(prompt_expr, scope))
            value = input(prompt)
            scope[var_name] = value
            return

        match = re.match(r'\$(\w+)\s*=\s*(?:اسأل|اسال)\s*\(\s*(.+?)\s*\)\s*;?\s*$', line)
        if match:
            var_name = match.group(1)
            prompt_expr = match.group(2).strip()
            if (prompt_expr.startswith('"') and prompt_expr.endswith('"')) or \
               (prompt_expr.startswith("'") and prompt_expr.endswith("'")):
                prompt = self._interpolate(prompt_expr[1:-1], scope)
            else:
                prompt = str(self._eval(prompt_expr, scope))
            value = input(prompt)
            scope[var_name] = value
            return

    # ─── MySQL ───

    def _cmd_db_connect(self, line, scope):
        match = re.match(r'\$(\w+)\s*=\s*اتصل_قاعدة\s*\((.+?)\)\s*;?\s*$', line)
        if not match:
            match = re.match(r'اتصل_قاعدة\s*\((.+?)\)\s*;?\s*$', line)
            if match:
                args = self._parse_args(match.group(1), scope)
                self._do_db_connect('_default', args, scope)
                return
            print("خطأ في أمر اتصال قاعدة البيانات:", line)
            return

        var_name = match.group(1)
        args = self._parse_args(match.group(2), scope)
        self._do_db_connect(var_name, args, scope)

    def _do_db_connect(self, name, args, scope):
        try:
            import mysql.connector
        except ImportError:
            print("خطأ: مكتبة mysql-connector-python غير مثبتة")
            print("قم بتثبيتها: pip install mysql-connector-python")
            return

        if len(args) < 4:
            print("خطأ: اتصل_قاعدة يحتاج 4 معاملات (السيرفر, المستخدم, كلمة_المرور, قاعدة_البيانات)")
            return

        try:
            conn = mysql.connector.connect(
                host=str(args[0]),
                user=str(args[1]),
                password=str(args[2]),
                database=str(args[3]),
                charset='utf8mb4'
            )
            self.db_connections[name] = conn
            scope[name] = name
            print(f"تم الاتصال بقاعدة البيانات '{args[3]}' بنجاح")
        except Exception as e:
            print(f"خطأ في الاتصال بقاعدة البيانات: {e}")

    def _cmd_db_query(self, line, scope):
        match = re.match(r'\$(\w+)\s*=\s*استعلم\s*\(\s*\$?(\w+)\s*,\s*(.+?)\s*\)\s*;?\s*$', line)
        if not match:
            print("خطأ في أمر الاستعلام:", line)
            return

        result_var = match.group(1)
        conn_name = match.group(2)
        query_expr = match.group(3).strip()

        if (query_expr.startswith('"') and query_expr.endswith('"')) or \
           (query_expr.startswith("'") and query_expr.endswith("'")):
            query = self._interpolate(query_expr[1:-1], scope)
        else:
            query = str(self._eval(query_expr, scope))

        conn = self.db_connections.get(conn_name)
        if not conn:
            print(f"خطأ: الاتصال '${conn_name}' غير موجود")
            return

        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(query)
            rows = cursor.fetchall()
            scope[result_var] = rows
            cursor.close()
        except Exception as e:
            print(f"خطأ في الاستعلام: {e}")

    def _cmd_db_execute(self, line, scope):
        match = re.match(r'نفذ_استعلام\s*\(\s*\$?(\w+)\s*,\s*(.+?)\s*\)\s*;?\s*$', line)
        if not match:
            print("خطأ في أمر التنفيذ:", line)
            return

        conn_name = match.group(1)
        query_expr = match.group(2).strip()

        if (query_expr.startswith('"') and query_expr.endswith('"')) or \
           (query_expr.startswith("'") and query_expr.endswith("'")):
            query = self._interpolate(query_expr[1:-1], scope)
        else:
            query = str(self._eval(query_expr, scope))

        conn = self.db_connections.get(conn_name)
        if not conn:
            print(f"خطأ: الاتصال '${conn_name}' غير موجود")
            return

        try:
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            print(f"تم تنفيذ الاستعلام بنجاح (عدد الصفوف المتأثرة: {cursor.rowcount})")
            cursor.close()
        except Exception as e:
            print(f"خطأ في تنفيذ الاستعلام: {e}")

    def _cmd_db_close(self, line, scope):
        match = re.match(r'اقفل_قاعدة\s*\(\s*\$?(\w+)\s*\)\s*;?\s*$', line)
        if not match:
            print("خطأ في أمر إغلاق قاعدة البيانات:", line)
            return

        conn_name = match.group(1)
        conn = self.db_connections.get(conn_name)
        if conn:
            try:
                conn.close()
                del self.db_connections[conn_name]
                print("تم إغلاق الاتصال بقاعدة البيانات بنجاح")
            except Exception as e:
                print(f"خطأ في إغلاق الاتصال: {e}")
        else:
            print(f"خطأ: الاتصال '${conn_name}' غير موجود")

    # ─── HTTP/API ───

    def _cmd_http(self, line, scope):
        get_match = re.match(r'\$(\w+)\s*=\s*جيب_من\s*\((.+?)\)\s*;?\s*$', line)
        if get_match:
            var_name = get_match.group(1)
            args = self._parse_args(get_match.group(2), scope)
            self._do_http_request('GET', var_name, args, scope)
            return

        post_match = re.match(r'\$(\w+)\s*=\s*رسل_لي\s*\((.+?)\)\s*;?\s*$', line)
        if post_match:
            var_name = post_match.group(1)
            args = self._parse_args(post_match.group(2), scope)
            self._do_http_request('POST', var_name, args, scope)
            return

        put_match = re.match(r'\$(\w+)\s*=\s*حدث_في\s*\((.+?)\)\s*;?\s*$', line)
        if put_match:
            var_name = put_match.group(1)
            args = self._parse_args(put_match.group(2), scope)
            self._do_http_request('PUT', var_name, args, scope)
            return

        del_match = re.match(r'\$(\w+)\s*=\s*احذف_من_api\s*\((.+?)\)\s*;?\s*$', line)
        if del_match:
            var_name = del_match.group(1)
            args = self._parse_args(del_match.group(2), scope)
            self._do_http_request('DELETE', var_name, args, scope)
            return

        print("خطأ في أمر HTTP:", line)

    def _do_http_request(self, method, var_name, args, scope):
        try:
            import requests as req_lib
        except ImportError:
            print("خطأ: مكتبة requests غير مثبتة")
            print("قم بتثبيتها: pip install requests")
            return

        if not args:
            print(f"خطأ: {method} يحتاج على الأقل رابط URL")
            return

        url = str(args[0])
        headers = args[2] if len(args) > 2 and isinstance(args[2], dict) else {}

        try:
            if method == 'GET':
                response = req_lib.get(url, headers=headers, timeout=30)
            elif method == 'POST':
                data = args[1] if len(args) > 1 else None
                if isinstance(data, dict):
                    response = req_lib.post(url, json=data, headers=headers, timeout=30)
                else:
                    response = req_lib.post(url, data=str(data) if data else None, headers=headers, timeout=30)
            elif method == 'PUT':
                data = args[1] if len(args) > 1 else None
                if isinstance(data, dict):
                    response = req_lib.put(url, json=data, headers=headers, timeout=30)
                else:
                    response = req_lib.put(url, data=str(data) if data else None, headers=headers, timeout=30)
            elif method == 'DELETE':
                response = req_lib.delete(url, headers=headers, timeout=30)
            else:
                print(f"خطأ: طريقة HTTP غير معروفة: {method}")
                return

            result = {
                'الحالة': response.status_code,
                'النص': response.text,
            }
            try:
                result['البيانات'] = response.json()
            except Exception:
                result['البيانات'] = response.text

            scope[var_name] = result

        except Exception as e:
            print(f"خطأ في طلب HTTP: {e}")
            scope[var_name] = {'الحالة': 0, 'خطأ': str(e)}

    # ─── GUI ───

    def _cmd_gui_window(self, line, scope):
        match = re.match(r'\$(\w+)\s*=\s*نافذة_جديدة\s*\((.+?)\)\s*;?\s*$', line)
        if not match:
            print("خطأ في إنشاء النافذة:", line)
            return

        var_name = match.group(1)
        args = self._parse_args(match.group(2), scope)

        try:
            import tkinter as tk
        except ImportError:
            print("خطأ: مكتبة tkinter غير متوفرة")
            return

        title = str(args[0]) if args else "Havnix App"
        width = int(args[1]) if len(args) > 1 else 400
        height = int(args[2]) if len(args) > 2 else 300

        root = tk.Tk()
        root.title(title)
        root.geometry(f"{width}x{height}")

        self.gui_windows[var_name] = root
        self.gui_elements[var_name] = []
        scope[var_name] = var_name

    def _cmd_gui_button(self, line, scope):
        match = re.match(r'(?:\$(\w+)\s*=\s*)?زر\s*\((.+?)\)\s*;?\s*$', line)
        if not match:
            print("خطأ في إنشاء الزر:", line)
            return

        result_var = match.group(1)
        args = self._parse_args(match.group(2), scope)

        if len(args) < 2:
            print("خطأ: زر يحتاج (النافذة, النص) على الأقل")
            return

        import tkinter as tk

        win_name = str(args[0])
        btn_text = str(args[1])
        callback_name = str(args[2]) if len(args) > 2 else None

        root = self.gui_windows.get(win_name)
        if not root:
            print(f"خطأ: النافذة '${win_name}' غير موجودة")
            return

        def on_click():
            if callback_name and callback_name in self.functions:
                self._call_function(callback_name, [], scope)

        btn = tk.Button(root, text=btn_text, command=on_click, font=('Arial', 12),
                        padx=10, pady=5)
        btn.pack(pady=5)

        if result_var:
            scope[result_var] = btn

    def _cmd_gui_label(self, line, scope):
        match = re.match(r'(?:\$(\w+)\s*=\s*)?نص_ثابت\s*\((.+?)\)\s*;?\s*$', line)
        if not match:
            print("خطأ في إنشاء النص:", line)
            return

        result_var = match.group(1)
        args = self._parse_args(match.group(2), scope)

        if len(args) < 2:
            print("خطأ: نص_ثابت يحتاج (النافذة, النص)")
            return

        import tkinter as tk

        win_name = str(args[0])
        label_text = str(args[1])

        root = self.gui_windows.get(win_name)
        if not root:
            print(f"خطأ: النافذة '${win_name}' غير موجودة")
            return

        label_text = self._interpolate(label_text, scope)
        lbl = tk.Label(root, text=label_text, font=('Arial', 14))
        lbl.pack(pady=5)

        if result_var:
            scope[result_var] = lbl

    def _cmd_gui_entry(self, line, scope):
        match = re.match(r'\$(\w+)\s*=\s*مدخل_نص\s*\((.+?)\)\s*;?\s*$', line)
        if not match:
            print("خطأ في إنشاء مدخل النص:", line)
            return

        var_name = match.group(1)
        args = self._parse_args(match.group(2), scope)

        import tkinter as tk

        win_name = str(args[0])
        placeholder = str(args[1]) if len(args) > 1 else ""

        root = self.gui_windows.get(win_name)
        if not root:
            print(f"خطأ: النافذة '${win_name}' غير موجودة")
            return

        entry = tk.Entry(root, font=('Arial', 12), width=30)
        if placeholder:
            entry.insert(0, placeholder)
        entry.pack(pady=5)

        scope[var_name] = entry

    def _cmd_gui_textarea(self, line, scope):
        match = re.match(r'\$(\w+)\s*=\s*مساحة_نص\s*\((.+?)\)\s*;?\s*$', line)
        if not match:
            print("خطأ في إنشاء مساحة النص:", line)
            return

        var_name = match.group(1)
        args = self._parse_args(match.group(2), scope)

        import tkinter as tk

        win_name = str(args[0])
        rows = int(args[1]) if len(args) > 1 else 10
        cols = int(args[2]) if len(args) > 2 else 40

        root = self.gui_windows.get(win_name)
        if not root:
            return

        text = tk.Text(root, font=('Arial', 12), height=rows, width=cols)
        text.pack(pady=5)

        scope[var_name] = text

    def _cmd_gui_dropdown(self, line, scope):
        match = re.match(r'\$(\w+)\s*=\s*قائمة_اختيار\s*\((.+?)\)\s*;?\s*$', line)
        if not match:
            return

        var_name = match.group(1)
        args = self._parse_args(match.group(2), scope)

        import tkinter as tk
        from tkinter import ttk

        win_name = str(args[0])
        options = args[1] if len(args) > 1 and isinstance(args[1], list) else []

        root = self.gui_windows.get(win_name)
        if not root:
            return

        combo = ttk.Combobox(root, values=[str(o) for o in options], font=('Arial', 12))
        if options:
            combo.current(0)
        combo.pack(pady=5)

        scope[var_name] = combo

    def _cmd_gui_checkbox(self, line, scope):
        match = re.match(r'\$(\w+)\s*=\s*خانة_اختيار\s*\((.+?)\)\s*;?\s*$', line)
        if not match:
            return

        var_name = match.group(1)
        args = self._parse_args(match.group(2), scope)

        import tkinter as tk

        win_name = str(args[0])
        cb_text = str(args[1]) if len(args) > 1 else ""

        root = self.gui_windows.get(win_name)
        if not root:
            return

        var = tk.BooleanVar()
        cb = tk.Checkbutton(root, text=cb_text, variable=var, font=('Arial', 12))
        cb.pack(pady=5)

        scope[var_name] = var

    def _cmd_gui_run(self, line, scope):
        match = re.match(r'شغل_واجهة\s*\(\s*\$?(\w+)\s*\)\s*;?\s*$', line)
        if not match:
            print("خطأ في تشغيل الواجهة:", line)
            return

        win_name = match.group(1)
        root = self.gui_windows.get(win_name)
        if root:
            root.mainloop()
        else:
            print(f"خطأ: النافذة '${win_name}' غير موجودة")

    # ─── File I/O ───

    def _cmd_read_file(self, line, scope):
        match = re.match(r'\$(\w+)\s*=\s*(?:اقرأ_ملف|اقرا_ملف)\s*\((.+?)\)\s*;?\s*$', line)
        if not match:
            print("خطأ في أمر قراءة الملف:", line)
            return

        var_name = match.group(1)
        path = self._eval(match.group(2).strip(), scope)

        try:
            full_path = os.path.join(self.base_dir, str(path))
            with open(full_path, 'r', encoding='utf-8') as f:
                scope[var_name] = f.read()
        except Exception as e:
            print(f"خطأ في قراءة الملف: {e}")

    def _cmd_write_file(self, line, scope):
        match = re.match(r'اكتب_ملف\s*\((.+?)\)\s*;?\s*$', line)
        if not match:
            print("خطأ في أمر كتابة الملف:", line)
            return

        args = self._parse_args(match.group(1), scope)
        if len(args) < 2:
            print("خطأ: اكتب_ملف يحتاج (المسار, المحتوى)")
            return

        try:
            full_path = os.path.join(self.base_dir, str(args[0]))
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(str(args[1]))
            print(f"تم كتابة الملف: {args[0]}")
        except Exception as e:
            print(f"خطأ في كتابة الملف: {e}")

    def _cmd_append_file(self, line, scope):
        match = re.match(r'ضيف_ملف\s*\((.+?)\)\s*;?\s*$', line)
        if not match:
            return

        args = self._parse_args(match.group(1), scope)
        if len(args) < 2:
            return

        try:
            full_path = os.path.join(self.base_dir, str(args[0]))
            with open(full_path, 'a', encoding='utf-8') as f:
                f.write(str(args[1]))
        except Exception as e:
            print(f"خطأ في الإضافة للملف: {e}")

    def _cmd_delete_file(self, line, scope):
        match = re.match(r'احذف_ملف\s*\((.+?)\)\s*;?\s*$', line)
        if not match:
            return

        args = self._parse_args(match.group(1), scope)
        if not args:
            return

        try:
            full_path = os.path.join(self.base_dir, str(args[0]))
            os.remove(full_path)
            print(f"تم حذف الملف: {args[0]}")
        except Exception as e:
            print(f"خطأ في حذف الملف: {e}")

    # ─── Built-in Functions ───

    def _fn_length(self, val):
        if hasattr(val, '__len__'):
            return len(val)
        return 0

    def _fn_substring(self, s, start, end=None):
        s = str(s)
        if end is None:
            return s[int(start):]
        return s[int(start):int(end)]

    def _fn_replace(self, s, old, new):
        return str(s).replace(str(old), str(new))

    def _fn_split(self, s, delimiter=" "):
        return str(s).split(str(delimiter))

    def _fn_upper(self, s):
        return str(s).upper()

    def _fn_lower(self, s):
        return str(s).lower()

    def _fn_contains(self, s, sub):
        return str(sub) in str(s)

    def _fn_join(self, lst, delimiter=""):
        if isinstance(lst, list):
            return str(delimiter).join(str(x) for x in lst)
        return str(lst)

    def _fn_sqrt(self, n):
        return math.sqrt(float(n))

    def _fn_power(self, base, exp):
        return math.pow(float(base), float(exp))

    def _fn_abs(self, n):
        return abs(float(n))

    def _fn_random(self, min_val=0, max_val=100):
        return random.randint(int(min_val), int(max_val))

    def _fn_round(self, n, digits=0):
        return round(float(n), int(digits))

    def _fn_max(self, *args):
        if len(args) == 1 and isinstance(args[0], list):
            return max(args[0])
        return max(args)

    def _fn_min(self, *args):
        if len(args) == 1 and isinstance(args[0], list):
            return min(args[0])
        return min(args)

    def _fn_to_int(self, val):
        try:
            return int(float(val))
        except (ValueError, TypeError):
            return 0

    def _fn_to_float(self, val):
        try:
            return float(val)
        except (ValueError, TypeError):
            return 0.0

    def _fn_to_str(self, val):
        if isinstance(val, bool):
            return 'صاح' if val else 'غلط'
        if val is None:
            return 'فاضي'
        return str(val)

    def _fn_to_bool(self, val):
        if isinstance(val, str):
            return val.lower() not in ('', '0', 'false', 'غلط', 'فاضي')
        return bool(val)

    def _fn_type(self, val):
        if isinstance(val, bool):
            return 'منطقي'
        if isinstance(val, int):
            return 'رقم'
        if isinstance(val, float):
            return 'عشري'
        if isinstance(val, str):
            return 'نص'
        if isinstance(val, list):
            return 'قائمة'
        if isinstance(val, dict):
            return 'قاموس'
        if val is None:
            return 'فاضي'
        return 'مجهول'

    def _fn_keys(self, d):
        if isinstance(d, dict):
            return list(d.keys())
        return []

    def _fn_values(self, d):
        if isinstance(d, dict):
            return list(d.values())
        return []

    def _fn_append(self, lst, val):
        if isinstance(lst, list):
            lst.append(val)
            return lst
        return [lst, val]

    def _fn_remove(self, lst, val):
        if isinstance(lst, list) and val in lst:
            lst.remove(val)
        return lst

    def _fn_sort(self, lst):
        if isinstance(lst, list):
            return sorted(lst)
        return lst

    def _fn_reverse(self, lst):
        if isinstance(lst, list):
            return list(reversed(lst))
        if isinstance(lst, str):
            return lst[::-1]
        return lst

    def _fn_range(self, *args):
        if len(args) == 1:
            return list(range(int(args[0])))
        elif len(args) == 2:
            return list(range(int(args[0]), int(args[1])))
        elif len(args) == 3:
            return list(range(int(args[0]), int(args[1]), int(args[2])))
        return []

    def _fn_json_parse(self, s):
        try:
            return json.loads(str(s))
        except Exception:
            return None

    def _fn_json_stringify(self, val):
        try:
            return json.dumps(val, ensure_ascii=False, indent=2)
        except Exception:
            return str(val)
