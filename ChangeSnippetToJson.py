import json
def replace_spaces_with_tabs(code, spaces_per_tab=4):
    lines = code.split('\n')
    converted_lines = []
    for line in lines:
        converted_line = line
        while ' ' * spaces_per_tab in converted_line:
            converted_line = converted_line.replace(' ' * spaces_per_tab, '\t')
        converted_lines.append(converted_line)
    return '\n'.join(converted_lines)
def code_to_json_class(class_name, code):
    formatted_code = replace_spaces_with_tabs(code)
    lines = [line.rstrip() for line in formatted_code.strip().split('\n')]
    json_structure = {
        class_name: {
            "prefix": class_name.lower(),
            "body": lines,
            "description": f"{class_name} implementation"
        }
    }
    return json.dumps(json_structure, indent=4)

tobeconverted = """
def dfs(graph):
    starttime = [[0,0] for i in range(len(graph))]
    time = 0
    stack = [(0,-1,0)]
    while stack:
        cur, prev, state = stack.pop()
        if state == 0:
            starttime[cur][0] = time
            time += 1
            stack.append((cur, prev, 1))
            for neighbor in graph[w(cur)]:
                if neighbor == prev:
                    continue
                stack.append((neighbor, cur, 0))    
        elif state == 1:
            starttime[cur][1] = time
    return starttime
"""

json_output = code_to_json_class(input(),tobeconverted)
print(json_output) 
