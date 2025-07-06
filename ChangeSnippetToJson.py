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

def transpose(mat):
    return [list(col) for col in zip(*mat)]

def matmul(L,B,MOD=(10**9 + 7)):
    ans = [[0 for i in range(len(B[0]))] for j in range(len(L))]
    for i in range(len(L)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                ans[i][j] = (ans[i][j]+L[i][k]*B[k][j])%MOD
    return ans

def matpow(M,power):
    size = len(M)
    result = [[1 if i == j else 0 for j in range(size)] for i in range(size)]
    while power:
        if power % 2 == 1:
            result = matmul(result, M)
        M = matmul(M, M)
        power //= 2
    return result

def gauss(A,mod=MOD):
    m,n = len(A),len(A[0])-1
    rank = 0
    L = [-1]*n

    for col in range(n):
        for row in range(rank,m):
            if A[row][col]:
                A[rank],A[row] = A[row],A[rank]
                break
        else:
            continue  
        k = pow(A[rank][col],-1,mod)
        for j in range(col,n+1):
            A[rank][j] = A[rank][j]*k%mod

        for row in range(m):
            if row!=rank and A[row][col]:
                factor = A[row][col]
                for j in range(col,n+1):
                    A[row][j] -= factor*A[rank][j]
                    A[row][j] %= mod
        L[col] = rank
        rank += 1
    for row in range(rank, m):
        if A[row][n]:
            return None
    return [A[L[i]][n]  if L[i]!=-1 else 0 for i in range(len(L))]

"""

s = input("Enter The Name : ")
json_output = code_to_json_class(s,tobeconverted)
print(json_output) 

s = json_output[1:-1]
subprocess.run("clip", text=True, input=s)

print("Copied Succesfully.")