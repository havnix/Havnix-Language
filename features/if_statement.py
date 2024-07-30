import re
from features.comparison import execute_comparison_operation

def execute_if_statement(command, variables, lines, current_index, execute_line):
    match = re.match(r'لو\s*\(\s*(\$\w+|\d+|"[^"]*"|صاح|غلط)\s*([!=><]+)\s*(\$\w+|\d+|"[^"]*"|صاح|غلط)\s*\)\s*{', command)
    if match:
        left_operand = match.group(1)
        operator = match.group(2)
        right_operand = match.group(3)

        if left_operand.isdigit():
            left_value = int(left_operand)
        elif left_operand == "صاح":
            left_value = True
        elif left_operand == "غلط":
            left_value = False
        else:
            left_value = variables.get(left_operand.strip('$'), left_operand.strip('"'))

        if right_operand.isdigit():
            right_value = int(right_operand)
        elif right_operand == "صاح":
            right_value = True
        elif right_operand == "غلط":
            right_value = False
        else:
            right_value = variables.get(right_operand.strip('$'), right_operand.strip('"'))

        if execute_comparison_operation(left_value, operator, right_value):
            current_index += 1
            while current_index < len(lines) and not lines[current_index].strip().startswith('}'):
                current_index = execute_line(lines[current_index].strip(), variables, lines, current_index)
                current_index += 1
            current_index += 1

            if current_index < len(lines):
                next_line = lines[current_index].strip()
                if next_line.startswith('غير كدا'):
                    while current_index < len(lines) and not lines[current_index].strip().startswith('}'):
                        current_index += 1
                    current_index += 1 
        else:
            while current_index < len(lines) and not lines[current_index].strip().startswith('}'):
                current_index += 1
            current_index += 1

            if current_index < len(lines):
                next_line = lines[current_index].strip()
                if next_line.startswith('غير كدا'):
                    current_index += 1  
                    while current_index < len(lines) and not lines[current_index].strip().startswith('}'):
                        current_index = execute_line(lines[current_index].strip(), variables, lines, current_index)
                        current_index += 1
                    current_index += 1
    else:
        print("أمر غير مفهوم:", command)

    return current_index
