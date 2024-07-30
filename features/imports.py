import re
import os

def execute_import(command, variables, lines):
    import_match = re.match(r'جيب لي\s+"([\w.]+)"\s*;', command)
    if import_match:
        file_to_import = import_match.group(1).strip()
        if not file_to_import.endswith('.havnix'):
            file_to_import += '.havnix'
        
        if os.path.isfile(file_to_import):
            with open(file_to_import, 'r', encoding='utf-8') as file:
                imported_lines = file.readlines()
                imported_lines = [line.strip() for line in imported_lines if line.strip() and not line.strip().startswith('//')]
                
                for line in imported_lines:
                    if line.startswith('$'):
                        var_name, var_value = parse_variable(line)
                        if var_name:
                            variables[var_name] = var_value
                    elif line.startswith('قول ليهو'):
                        lines.append(line)

                print(f"[Import] '{file_to_import}' is imported successfully.")
        else:
            print(f"[Import] failed to import '{file_to_import}'.")

def parse_variable(line):
    match = re.match(r'\$(\w+)\s*=\s*(.*);', line)
    if match:
        var_name = match.group(1).strip()
        var_value = match.group(2).strip().strip("'").strip('"')
        return var_name, var_value
    return None, None
