import re

def create_gui(command, variables):
    # إزالة التعليقات والتأكد من أن التنسيق صحيح
    command = command.strip()
    match = re.match(r'واجهة\(\)\s*=>\s*\{(.*)\}', command, re.DOTALL)
    if match:
        gui_content = match.group(1).strip()
        properties = process_properties(gui_content)
        print(f"خصائص الواجهة: {properties}")
    else:
        print("تنسيق غير صحيح للواجهة:", command)

def process_properties(properties_string):
    properties = {}
    # معالجة خصائص الواجهة العامة
    items = re.split(r',\s*(?=\w)', properties_string.strip())
    for item in items:
        key, value = item.split(':', 1)
        properties[key.strip()] = value.strip()
    return properties