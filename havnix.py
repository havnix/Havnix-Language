import sys
from commands.print import execute_print
from features.if_statement import execute_if_statement
from features.comparison import execute_comparison_operation
from features.variables import execute_variable_assignment
from features.functions import define_function, call_function
from features.comments import process_comments
from features.imports import execute_import

def execute_line(line, variables, lines, current_index):
    if line.startswith('قول ليهو'):
        execute_print(line, variables)
    elif line.startswith('$'):
        execute_variable_assignment(line, variables)
    elif line.startswith('لو'):
        current_index = execute_if_statement(line, variables, lines, current_index, execute_line)
    elif line.startswith('دالة'):
        current_index = define_function(line, lines, current_index)
    elif line.startswith('داير'):
        call_function(line, variables)
    elif line.startswith('جيب لي'):
        execute_import(line, variables, lines)
    else:
        print("أمر غير مفهوم:", line)
    return current_index

def run_program(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            variables = {}
            lines = process_comments(lines)
            current_index = 0
            while current_index < len(lines):
                line = lines[current_index].strip()
                if line:
                    current_index = execute_line(line, variables, lines, current_index)
                current_index += 1
    except FileNotFoundError:
        print(f"الملف {file_name} غير موجود.")
    except Exception as e:
        print(f"حدث خطأ غير متوقع: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("استخدام: python main.py <file.havnix>")
    else:
        run_program(sys.argv[1])
