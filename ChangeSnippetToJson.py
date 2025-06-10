import json
import subprocess

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

def z_function(S):
    # return: the Z array, where Z[i] = length of the longest common prefix of S[i:] and S
    n = len(S)
    Z = [0] * n
    l = r = 0
    for i in range(1, n):
        z = Z[i - l]
        if i + z >= r:
            z = max(r - i, 0)
            while i + z < n and S[z] == S[i + z]:
                z += 1
            l, r = i, i + z
        Z[i] = z
    Z[0] = n
    return Z

def manacher(s):
    # returns longest palindrome in s
    t = '#' + '#'.join(s) + '#'
    n = len(t)
    L = [0] * n
    c = r = 0
    ml = 0
    mc = 0
    for i in range(n):
        mirror = 2*c-i
        if i<r:
            L[i] = min(r-i,L[mirror])
        a = i+L[i]+1
        b = i-L[i]-1
        while a<n and b>=0 and t[a]==t[b]:
            L[i] += 1
            a += 1
            b -= 1
        if i+L[i]>r:
            c = i
            r = i+L[i]
        if L[i]>ml:
            ml = L[i]
            mc = i
    start = (mc-ml)//2
    return s[start:start+ml]
"""

s = input("Enter The Name : ")
json_output = code_to_json_class(s,tobeconverted)
print(json_output) 

s = json_output[1:-1]
subprocess.run("clip", text=True, input=s)

print("Copied Succesfully.")