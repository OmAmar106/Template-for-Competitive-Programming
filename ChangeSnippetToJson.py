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

def sieve_unique(N):
    mini = [i for i in range(N)]
    for i in range(2,N):
        if mini[i]==i:
            for j in range(2*i,N,i):
                mini[j] = i
    return mini

def unique_prime_factors(k):
    \"\"\"
        When the numbers are large this is the best method to get 
        unique prime factors, precompute n log n log n , then each query is log n
    \"\"\"
    Lmini = [] #precalculate this upto the number required
    # this should not be here , it should be global and contain the mini made in sieve_unique
    # dont forget
    
    ans = []
    while k!=1:
        ans.append(Lmini[k])
        k //= Lmini[k]
    return ans

"""

json_output = code_to_json_class(input(),tobeconverted)
print(json_output) 


"""  DSU , trie , treap,2SAT , graphs , neo game brute force , interactive problems """

