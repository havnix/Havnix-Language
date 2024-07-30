import re

def execute_variable_assignment(command, variables):
    match = re.match(r'\$(\w+)\s*=\s*\[(.*)\]\s*;', command)
    if match:
        var_name = match.group(1)
        var_values = match.group(2).split(',')
        for i, value in enumerate(var_values):
            var_values[i] = value.strip()
            if var_values[i] == "صاح":
                var_values[i] = True
            elif var_values[i] == "غلط":
                var_values[i] = False
            elif '.' in var_values[i]:
                var_values[i] = float(var_values[i])
            else:
                try:
                    var_values[i] = int(var_values[i])
                except ValueError:
                    var_values[i] = var_values[i].strip('"')
        variables[var_name] = var_values
    else:
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
            else:
                try:
                    var_value = int(var_value)
                except ValueError:
                    var_value = var_value.strip('"')
            variables[var_name] = var_value
        else:
            print("أمر غير مفهوم:", command)
