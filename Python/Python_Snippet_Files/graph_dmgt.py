def find_bridges(adj):
	# returns all bridges
	bridges = []
	n = len(adj)
	timer = 0
	visited = [False]*n
	tin = [-1]*n
	low = [-1]*n
	for start in range(n):
		if visited[start]:
			continue
		stack = [(start, -1, 0, False)]
		visited[start] = True
		tin[start] = low[start] = timer
		timer += 1
		while stack:
			v, parent, idx, backtrack = stack.pop()
			if backtrack:
				to = adj[v][idx]
				low[v] = min(low[v], low[to])
				if low[to] > tin[v]:
					bridges.append((v,to))
				continue
			if idx < len(adj[v]):
				to = adj[v][idx]
				stack.append((v, parent, idx + 1, False))
				if to == parent:
					continue
				if visited[to]:
					low[v] = min(low[v], tin[to])
				else:
					visited[to] = True
					tin[to] = low[to] = timer
					timer += 1
					stack.append((v, parent, idx, True))
					stack.append((to, v, 0, False))
	return bridges

def bridges_on_path(adj):
	# returns all bridges on path from 1 to n
	n = len(adj)
	timer = 0
	visited = [False]*n
	tin = [-1]*n
	low = [-1]*n
	bridges = []
	for start in range(n):
		if visited[start]:
			continue
		stack = [(start, -1, 0, False)]
		visited[start] = True
		tin[start] = low[start] = timer
		timer += 1
		while stack:
			v, parent, idx, backtrack = stack.pop()
			if backtrack:
				to = adj[v][idx]
				low[v] = min(low[v], low[to])
				if low[to] > tin[v]:
					bridges.append((v, to))
				continue
			if idx < len(adj[v]):
				to = adj[v][idx]
				stack.append((v, parent, idx+1, False))
				if to == parent:
					continue
				if visited[to]:
					low[v] = min(low[v], tin[to])
				else:
					visited[to] = True
					tin[to] = low[to] = timer
					timer += 1
					stack.append((v, parent, idx, True))
					stack.append((to, v, 0, False))
	comp_id = [-1]*n
	comp = 0
	bridge_set = set(bridges)
	for i in range(n):
		if comp_id[i] != -1:
			continue
		stack = [i]
		comp_id[i] = comp
		while stack:
			v = stack.pop()
			for to in adj[v]:
				if comp_id[to] == -1 and (v, to) not in bridge_set and (to, v) not in bridge_set:
					comp_id[to] = comp
					stack.append(to)
		comp += 1

	tree = [[] for _ in range(comp)]
	for u, v in bridges:
		cu, cv = comp_id[u], comp_id[v]
		tree[cu].append((cv, (u, v)))
		tree[cv].append((cu, (u, v)))

	c1, cN = comp_id[0], comp_id[n-1]
	if c1 == cN:
		return []
	parent = {c1: None}
	edge_used = {c1: None}
	stack = [c1]
	while stack:
		u = stack.pop()
		for v, e in tree[u]:
			if v not in parent:
				parent[v] = u
				edge_used[v] = e
				stack.append(v)
	path_bridges = []
	cur = cN
	while cur != c1:
		path_bridges.append(edge_used[cur])
		cur = parent[cur]
	return [(u,v) for u, v in path_bridges]

def lowlink(edge):
	n = len(edge)
	parent = [-1] * n
	visited = [False] * n
	for s in range(n):
		if not visited[s]:
			que = [s]
			while que:
				now = que.pop()
				if visited[now]: continue
				visited[now] = True
				for nxt in edge[now]:
					if not visited[nxt]:
						parent[nxt] = now
						que.append(nxt)
	order = [-1] * n
	low = [-1] * n
	is_articulation = [False] * n
	articulation = []
	bridge = []
	def dfs(s):
		idx = 0
		cnt = 0
		que = [~s,s]
		while que:
			now = que.pop()
			if now >= 0:
				order[now] = low[now] = idx
				idx += 1
				for nxt in edge[now]:
					if parent[nxt] == now:
						que.append(~nxt)
						que.append(nxt)
					elif parent[now] != nxt and order[nxt] != -1:
						low[now] = min(low[now], order[nxt])
			else:
				now = ~now
				par = parent[now]
				if par == s: cnt += 1
				if now == s:
					is_articulation[now] |= (cnt >= 2)
					if is_articulation[now]:
						articulation.append(now)
					return
				if is_articulation[now]:
					articulation.append(now)
				if now != parent[par]:
					low[par] = min(low[par], low[now])
				is_articulation[par] |= (par != s) and (order[par] <= low[now])
				if order[par] < low[now]:
					bridge.append((par, now))
	for i in range(n):
		if parent[i] == -1:
			dfs(i)
	return articulation, bridge

def find_2ecc(edges,d):
	# returns a new graph, in which two nodes are connected
	# if and only if they are part of same cycle.
	_,bridges = lowlink(d)
	newd = [[] for i in range(len(d))]
	bridges = set((w(i[0]),w(i[1])) for i in bridges)
	for u,v in edges:
		if (w(u),w(v)) not in bridges and (w(v),w(u)) not in bridges:
			newd[u].append(v)
			newd[v].append(u)
	return newd