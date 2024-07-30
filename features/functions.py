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
        while current_index < len(lines):
            line = lines[current_index].strip()
            if line == '}':
                break
            functions[func_name]['body'].append(line)
            current_index += 1
        return current_index
    return None

def call_function(command, variables):

    match = re.match(r'داير\s*(\w+)\s*\((.*)\)\s*;', command)
    if match:
        func_name = match.group(1)
        args = match.group(2).split(',')
        args = [arg.strip() for arg in args]
        
        if func_name in functions:
            func = functions[func_name]
            body = func['body']

            for line in body:
                for i, param in enumerate(func['params']):


                    arg_value = args[i].strip('"')
                    line = re.sub(r'\b' + re.escape(param) + r'\b', arg_value, line)
                print(line)
        else:
            print(f"الدالة {func_name} غير موجودة.")
