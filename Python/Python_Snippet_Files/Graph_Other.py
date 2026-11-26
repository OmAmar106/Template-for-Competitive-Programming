def euler_path(d):
	start = [1]
	ans = []
	while start:
		cur = start[-1]
		if len(d[cur])==0:
			ans.append(start.pop())
			continue
		k1 = d[cur].pop()
		d[k1].remove(cur) # if undirected
		start.append(k1)
	return ans

def floyd_warshall(n, edges):
	dist = [[0 if i == j else float("inf") for i in range(n)] for j in range(n)]
	pred = [[None] * n for _ in range(n)]

	for u, v, d in edges:
		dist[u][v] = d
		pred[u][v] = u

	for k in range(n):
		for i in range(n):
			for j in range(n):
				if dist[i][k] + dist[k][j] < dist[i][j]:
					dist[i][j] = dist[i][k] + dist[k][j]
					pred[i][j] = pred[k][j]
	# Sanity Check
	# for u, v, d in edges:
	#	 if dist[u] + d < dist[v]:
	#		 return None
	return dist, pred

def bellman_ford(n, edges, start=0):
	dist = [float("inf")] * n
	pred = [None] * n
	dist[start] = 0
	for _ in range(n):
		for u, v, d in edges:
			if dist[u] + d < dist[v]:
				dist[v] = dist[u] + d
				pred[v] = u
	# for u, v, d in edges:
	#	 if dist[u] + d < dist[v]:
	#		 return -1
	# This returns -1 , if there is a negative cycle
	return dist

def toposort(graph):
	res, found = [], [0] * len(graph)
	stack = list(range(len(graph)))
	while stack:
		node = stack.pop()
		if node < 0:
			res.append(~node)
		elif not found[node]:
			found[node] = 1
			stack.append(~node)
			stack += graph[node]
	for node in res:
		if any(found[nei] for nei in graph[node]):
			return None
		found[node] = 0
	return res[::-1]

def euler_path_faster(d):
	# expects a adjacency list having u -> (v,edge index)
	# v -> (u,~edge index) (for reverse edges)
	n = len(d)
	visited = defaultdict(lambda :False)
	visited2 = [False]*n
	ans = []
	for cur in range(n):
		if not visited2[cur] and d[cur]:
			start = [cur]
			while start:
				cur = start[-1]
				visited2[cur] = True
				while d[cur] and visited[max(d[cur][-1][1],~d[cur][-1][1])]:
					d[cur].pop()
				if len(d[cur])==0:
					start.pop()
					continue
				k1,k2 = d[cur].pop()
				ans.append(k2)
				visited[max(k2,~k2)] = True
				start.append(k1)
	return ans
