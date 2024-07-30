import re

def execute_print(command, variables):
    match = re.match(r'قول ليهو\("(.+)"\);', command)
    if match:
        text = match.group(1)
        for var in variables:
            if "$" in text:
                match_var = re.findall(r'\$(\w+)\[(\d+)\]', text)
                for var_name, index in match_var:
                    if var_name in variables:
                        if isinstance(variables[var_name], list):
                            text = text.replace(f"${var_name}[{index}]", str(variables[var_name][int(index)]))
                        else:
                            print(f"تحذير: المتغير {var_name} ليس قائمة.")
                text = text.replace(f"${var}", str(variables[var]))
        
        print(text)
    else:
        print("أمر غير مفهوم:", command)
