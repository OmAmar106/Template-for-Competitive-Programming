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
class PersistentSegmentTree:

    class Node:
        def __init__(self, value=0, left=None, right=None):
            self.value = value
            self.left = left
            self.right = right
            
    @staticmethod
    def func(a, b):
        return a+b
    def __init__(self, data):
        self.n = len(data)
        self.versions = []
        self.versions.append(self._build(data))
    def _build(self, data):
        stack = [(0, self.n - 1, False)]
        nodes = {}
        while stack:
            left, right, visited = stack.pop()
            if left == right:
                nodes[(left, right)] = self.Node(data[left])
            else:
                if visited:
                    mid = (left + right) // 2
                    left_child = nodes[(left, mid)]
                    right_child = nodes[(mid + 1, right)]
                    nodes[(left, right)] = self.Node(self.func(left_child.value,right_child.value),left_child, right_child)
                else:
                    stack.append((left, right, True))
                    mid = (left + right) // 2
                    stack.append((mid + 1, right, False))
                    stack.append((left, mid, False))
        return nodes[(0, self.n - 1)]
    
    def update(self, version, pos, value):
        old_root = self.versions[version]
        stack, path = [(old_root, 0, self.n - 1)], []
        while stack:
            node, left, right = stack.pop()
            path.append((node, left, right))
            if left == right:
                break
            mid = (left + right) // 2
            if pos <= mid:
                stack.append((node.left, left, mid))
            else:
                stack.append((node.right, mid + 1, right))
        
        new_nodes = {}
        for node, left, right in reversed(path):
            if left == right:
                k = value
                # k = self.func(node.value,value) # if i want to update
                new_nodes[(left, right)] = self.Node(k)
            else:
                mid = (left + right) // 2
                left_child = new_nodes.get((left, mid), node.left)
                right_child = new_nodes.get((mid + 1, right), node.right)
                new_nodes[(left, right)] = self.Node(self.func(left_child.value,right_child.value),left_child, right_child)
        return new_nodes[(0, self.n - 1)]

    def create_version(self, version, pos, value):
        new_root = self.update(version, pos, value)
        self.versions.append(new_root)
        return len(self.versions) - 1

    def query(self, version, ql, qr):
        node, left, right = self.versions[version], 0, self.n - 1
        stack = [(node, left, right)]
        result = 0 # change this depending on the problem
        while stack:
            node, left, right = stack.pop()
            if ql > right or qr < left:
                continue
            if ql <= left and right <= qr:
                result = self.func(result,node.value)
            else:
                mid = (left + right) // 2
                stack.append((node.left, left, mid))
                stack.append((node.right, mid + 1, right))
        return result
"""

json_output = code_to_json_class(input(),tobeconverted)
print(json_output) 
