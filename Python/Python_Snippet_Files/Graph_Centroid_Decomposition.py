def shallowest_decomposition_tree(graph, root=0):
	# returns a root and a directed tree, iterate on it and you
	# will find the new centroid
	# quite faster than centroid_decomposition_tree
	ctz = lambda x:(x & -x).bit_length()-1
	n = len(graph)
	forbidden = [0] * n
	decomposition_tree = [[] for _ in range(n)]
	stacks = [[] for _ in range(n.bit_length())]
	def extract_chain(labels, u):
		while labels:
			label = labels.bit_length() - 1
			labels ^= 2**label
			v = stacks[label].pop()
			decomposition_tree[u].append(v)
			u = v
	dfs = [root]
	while dfs:
		u = dfs.pop()
		if u >= 0:
			forbidden[u] = -1
			dfs.append(~u)
			for v in graph[u]:
				if not forbidden[v]:
					dfs.append(v)
		else:
			u = ~u
			forbidden_once = forbidden_twice = 0
			for v in graph[u]:
				forbidden_twice  |= forbidden_once & (forbidden[v] + 1)
				forbidden_once  |= forbidden[v] + 1
			forbidden[u] = forbidden_once | (2**forbidden_twice.bit_length() - 1)
			label_u = ctz(forbidden[u] + 1)
			stacks[label_u].append(u)
			for v in graph[u]:
				extract_chain((forbidden[v] + 1) & (2**label_u - 1), u)
	max_label = (forbidden[root] + 1).bit_length() - 1
	decomposition_root = stacks[max_label].pop()
	extract_chain((forbidden[root] + 1) & (2**max_label - 1), decomposition_root)
	return decomposition_tree, decomposition_root

def centroid_decomposition_tree(graph):
	# returns a root and a directed tree, iterate on it and you
	# will find the new centroid
	n = len(graph)
	graph = [c[:] for c in graph]
	bfs = [0]
	for node in bfs:
		bfs += graph[node]
		for nei in graph[node]:
			graph[nei].remove(node)
	size = [0] * n
	for node in reversed(bfs):
		size[node] = 1 + sum(size[child] for child in graph[node])
	decomposition_tree = [[] for _ in range(n)]
	def centroid_reroot(u):
		N = size[u]
		while True:
			for v in graph[u]:
				if size[v] > N // 2:
					size[u] = N - size[v]
					graph[u].remove(v)
					graph[v].append(u)
					u = v
					break
			else:
				decomposition_tree[u] = [centroid_reroot(v) for v in graph[u]]
				return u
	decomposition_root = centroid_reroot(0)
	return decomposition_tree, decomposition_root
