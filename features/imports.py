import re
import os

def execute_import(command, variables, lines):
    import_match = re.match(r'داير\s+"([\w./]+)"\s*;', command)
    if import_match:
        file_to_import = import_match.group(1).strip()
        if not file_to_import.endswith('.havnix'):
            file_to_import += '.havnix'
        
        search_paths = [
            file_to_import,
            os.path.join('src', file_to_import),
            os.path.join('include', file_to_import),
            os.path.join('lib', file_to_import),
        ]

        for path in search_paths:
            if os.path.isfile(path):
                with open(path, 'r', encoding='utf-8') as file:
                    imported_lines = file.readlines()
                    imported_lines = [line.strip() for line in imported_lines if line.strip() and not line.strip().startswith('//')]
                    
                    for line in imported_lines:
                        if line.startswith('$'):
                            var_name, var_value = parse_variable(line)
                            if var_name:
                                variables[var_name] = var_value
                        elif line.startswith('قول ليهو'):
                            lines.append(line)
                return
        
        print(f"[Import] ما قدرت استعدي الملف دا '{file_to_import}' لأني ما لقيتو")

def parse_variable(line):
    match = re.match(r'\$(\w+)\s*=\s*[\'"]?(.*?)[\'"]?\s*;', line)
    if match:
        var_name = match.group(1).strip()
        var_value = match.group(2).strip()
        return var_name, var_value
    return None, None
