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

def call_function(command, variables, lines, execute_line):
    match = re.match(r'جيب لي\s*(\w+)\s*\((.*)\)\s*;', command)
    if match:
        func_name = match.group(1)
        args = match.group(2).split(',')
        args = [arg.strip() for arg in args]
        
        if func_name in functions:
            func = functions[func_name]
            local_vars = variables.copy()
            
            for i, param in enumerate(func['params']):
                local_vars[param] = args[i].strip('"')
                
            for line in func['body']:
                execute_line(line, local_vars, lines, 0)
        else:
            print(f"[Functions] '{func_name}' doesn't exists.")
