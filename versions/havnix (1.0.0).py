import re
import sys

# قول ليهو | print
def execute_print_command(command, variables):
    match = re.match(r'قول ليهو\("(.+)"\);', command)
    if match:
        text = match.group(1)
        for var in variables:
            # التعرف على مصفوفات المتغيرات واستبدالها بقيمها المطلقة
            if "$" in text:
                match_var = re.findall(r'\$(\w+)\[(\d+)\]', text)
                for var_name, index in match_var:
                    if var_name in variables:
                        text = text.replace(f"${var_name}[{index}]", str(variables[var_name][int(index)]))
            text = text.replace(f"${var}", str(variables[var]))
        print(text)
    else:
        print("أمر غير مفهوم:", command)


# متغيرات
def execute_variable_assignment(command, variables):
    match = re.match(r'\$(\w+)\s*=\s*\[(.*)\]\s*;', command)  # دي للمصفوفات
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
        match = re.match(r'\$(\w+)\s*=\s*(\[.*\]|".*"|\d+|\d+\.\d+|صاح|غلط)\s*;', command)  # دي للمتتغيرات البوليان
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

# مقارنة
def execute_comparison_operation(left_operand, operator, right_operand):
    if operator == "==":
        return left_operand == right_operand
    elif operator == "!=":
        return left_operand != right_operand
    elif operator == ">":
        return left_operand > right_operand
    elif operator == ">=":
        return left_operand >= right_operand
    elif operator == "<":
        return left_operand < right_operand
    elif operator == "<=":
        return left_operand <= right_operand
    else:
        print("عملية مقارنة غير صحيحة")
        return False

# جمل شرطية
def execute_if_statement(command, variables, lines, current_index):
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

            # غير كدا (else)
            if current_index < len(lines):
                next_line = lines[current_index].strip()
                if next_line.startswith('غير كدا'):
                    while current_index < len(lines) and not lines[current_index].strip().startswith('}'):
                        current_index += 1
                    current_index += 1  # تجاوز '}'
        else:
            while current_index < len(lines) and not lines[current_index].strip().startswith('}'):
                current_index += 1
            current_index += 1  # تجاوز '}'

            # تنفيذ الكود جوا غير كدا (else)
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

# معالجة لي كل الاوامر
def execute_line(line, variables, lines, current_index):
    if line.startswith('قول ليهو'):
        execute_print_command(line, variables)
    elif line.startswith('$'):
        execute_variable_assignment(line, variables)
    elif line.startswith('لو'):
        current_index = execute_if_statement(line, variables, lines, current_index)
    else:
        print("أمر غير مفهوم:", line)

    return current_index

# معالجة الاوامر من ملف تاني
def run_program(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            variables = {}  # قائمة بالمتغيرات وقيمها
            current_index = 0
            while current_index < len(lines):
                line = lines[current_index].strip()
                
                # التعليقات
                if '//' in line:
                    line = line.split('//')[0].strip()
                
                # المحتوى بين تعليقات /* */
                if '/*' in line:
                    while '*/' not in line:
                        current_index += 1
                        line = lines[current_index].strip()
                    line = line.split('*/')[1].strip()
                
                if line:  # تجاهل الأسطر المافيها كلام
                    current_index = execute_line(line, variables, lines, current_index)
                current_index += 1
    except FileNotFoundError:
        print(f"الملف {file_name} غير موجود.")
    except Exception as e:
        print(f"حدث خطأ غير متوقع: {e}")

# تشغيل البرنامج
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("استخدام: python havnix.py <file.havnix>")
    else:
        run_program(sys.argv[1])
