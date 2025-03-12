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
def bfsf(graph,start=0):
    bfs = [start]
    visited = [False]*(len(graph))
    visited[start] = True
    for u in bfs:
        for j in graph[u]:
            if visited[j]:
                continue
            visited[j] = True
            bfs.append(j)
    return bfs

def dijkstra(graph, start ,n):
    dist, parents = [float("inf")] * n, [-1] * n
    dist[start] = 0
    queue = [(0, start)]
    while queue:
        path_len, v = heappop(queue)
        if path_len == dist[v]:
            for w, edge_len in graph[v]:
                if edge_len + path_len < dist[w]:
                    dist[w], parents[w] = edge_len + path_len, v
                    heappush(queue, (edge_len + path_len, w))
    return dist, parents

def dfs(graph,start=0):
    # I can also use this to replicate recursion
    # without facing the overhead
    n = len(graph)
    visited = [False] * n
    stack = [start]
    while stack:
        start = stack[-1]
        # stack.pop() # use this if there is nothing after returning
        if not visited[start]:
            visited[start] = True
            for child in graph[start]:
                if not visited[child]:
                    stack.append(child)
        else:
            stack.pop()
            # dp[start] += 1
            # for child in graph[start]:
            #     if finished[child]:
            #         dp[start] += dp[child]
            # finished[start] = True
            # remove else if you are doing nothing here
            # add the stuff that you do post traversel here
            # and add the finished array
    return visited
"""

json_output = code_to_json_class(input(),tobeconverted)
print(json_output) 
