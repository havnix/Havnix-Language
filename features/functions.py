import re

functions = {}

def define_function(command, lines, current_index):
    match = re.match(r'دالة\s*(\w+)\s*\((.*)\)\s*{', command)
    if match:
        func_name = match.group(1)
        params = match.group(2).split(',')
        params = [param.strip() for param in params]
        functions[func_name] = {
            'params': params,
            'body': []
        }

        current_index += 1
        brace_count = 1  # لتتبع الأقواس المتداخلة
        
        while current_index < len(lines) and brace_count > 0:
            line = lines[current_index].strip()
            if line == '{':
                brace_count += 1
            elif line == '}':
                brace_count -= 1
                if brace_count == 0:  # نهاية الدالة
                    break
            functions[func_name]['body'].append(line)
            current_index += 1
        return current_index
    return None

def execute_function(function_lines, args, variables, lines, execute_line):
    """تنفيذ الدالة مع المتغيرات المحلية"""
    # استخراج اسم الدالة والمعاملات
    func_def = function_lines[0]
    match = re.match(r'دالة\s*(\w+)\s*\((.*)\)', func_def)
    if match:
        params = [p.strip() for p in match.group(2).split(',') if p.strip()]
        
        # إنشاء نسخة من المتغيرات للدالة
        local_vars = variables.copy()
        
        # ربط المعاملات بالقيم
        for param, arg in zip(params, args):
            local_vars[param] = arg
        
        # تنفيذ جسم الدالة
        for line in function_lines[1:]:  # تجاهل سطر التعريف فقط
            if line != '{' and line != '}':  # تجاهل الأقواس
                execute_line(line, local_vars, lines, 0)

def call_function(command, variables, lines, execute_line):
    match = re.match(r'جيب لي\s+(\w+)\((.*)\)\s*;?', command)
    if match:
        function_name = match.group(1)
        args = [arg.strip().strip('"') for arg in match.group(2).split(',') if arg.strip()]
        
        # البحث عن الدالة في المتغيرات أولاً
        if function_name in variables and isinstance(variables[function_name], list):
            function_lines = variables[function_name]
            execute_function(function_lines, args, variables, lines, execute_line)
        # ثم البحث في الدوال المحلية
        elif function_name in functions:
            func = functions[function_name]
            local_vars = variables.copy()
            for i, param in enumerate(func['params']):
                local_vars[param] = args[i]
            for line in func['body']:
                if line != '{' and line != '}':  # تجاهل الأقواس
                    execute_line(line, local_vars, lines, 0)
        else:
            print(f"[Functions] الدالة '{function_name}' غير موجودة.")
