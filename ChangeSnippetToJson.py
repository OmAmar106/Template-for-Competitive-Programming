import json
import subprocess
import platform

def replace_spaces_with_tabs(code, spaces_per_tab=4):
    lines = code.split('\n')
    converted_lines = []
    for line in lines:
        converted_line = line
        while ' ' * spaces_per_tab in converted_line:
            converted_line = converted_line.replace(' ' * spaces_per_tab, '\t')
        converted_lines.append(converted_line)
    return '\n'.join(converted_lines)

def code_to_json_class(class_name,prefix,code):
    formatted_code = replace_spaces_with_tabs(code)
    lines = [line.rstrip() for line in formatted_code.strip().split('\n')]
    json_structure = {
        class_name: {
            "prefix": prefix.lower(),
            "body": lines,
            "description": f"{class_name} implementation"
        }
    }
    return json.dumps(json_structure, indent=4)

## TODO: Input should be provided via the CLI itself
tobeconverted = """
"""

prefix = input("Enter Prefix : ")
s = input("Enter The Name : ")
json_output = code_to_json_class(s,prefix,tobeconverted)
print(json_output)

s = json_output[1:-1]

os_name = platform.system()

if os_name == "Windows":
    subprocess.run(["clip"], text=True, input=s, check=True)
elif os_name == "Linux":
    subprocess.run(["xclip", "-selection", "clipboard"], text=True, input=s, check=True)
else:
    raise OSError(f"Unsupported operating system: {os_name}")

print("Copied Successfully.")