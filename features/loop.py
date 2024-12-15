import re

def evaluate_condition(condition, variables):
    try:
        condition = condition.replace("صاح", "True").replace("غلط", "False")
        for var in variables:
            condition = condition.replace(f"${var}", str(variables[var]))
        return eval(condition)
    except Exception as e:
        print(f"خطأ في تقييم الشرط: {e}")
        return False

def execute_loop(line, variables, lines, current_index, execute_line):
    try:
        parts = re.match(r'تكرار\s*\((.*);(.*);(.*)\)', line)
        if parts:
            start_command = parts.group(1).strip()
            condition_command = parts.group(2).strip()
            increment_command = parts.group(3).strip()

            execute_line(start_command, variables, lines, current_index)

            loop_start_index = current_index

            while evaluate_condition(condition_command, variables):
                current_index = loop_start_index + 1
                while not lines[current_index].strip() == 'انتهى':
                    line = lines[current_index].strip()
                    if line:
                        current_index = execute_line(line, variables, lines, current_index)
                    current_index += 1

                execute_line(increment_command, variables, lines, current_index)
        
            while not lines[current_index].strip() == 'انتهى':
                current_index += 1
            return current_index
        else:
            print("تنسيق غير صحيح للحلقة التكرارية:", line)
            return current_index
    except Exception as e:
        print(f"حدث خطأ غير متوقع في تنفيذ الحلقة التكرارية: {e}")
        return current_index