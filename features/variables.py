import re

def execute_variable_assignment(command, variables):
    match = re.match(r'\$(\w+)\s*=\s*(\[.*\]|".*"|\d+|\d+\.\d+|صاح|غلط)\s*;', command)
    if match:
        var_name = match.group(1)
        var_value = match.group(2)
        if var_value == "صاح":
            var_value = True
        elif var_value == "غلط":
            var_value = False
        elif '.' in var_value:
            var_value = float(var_value)
        elif var_value.isdigit():
            var_value = int(var_value)
        elif var_value.startswith('[') and var_value.endswith(']'):
            var_value = var_value[1:-1].split(',')
            var_value = [int(v) if v.isdigit() else v.strip() for v in var_value]
        else:
            var_value = var_value.strip('"')
        variables[var_name] = var_value
    else:
        print("أمر غير مفهوم:", command)