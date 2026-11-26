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

def dominator_tree(adj,root=0):
	n = len(adj)
	arr = [-1]*n
	rev = []
	par = [-1]*n

	arr[root] = 0
	rev.append(root)
	st=[(root,0)]
	while st:
		v,i = st[-1]
		if i==len(adj[v]):
			st.pop()
			continue
		u = adj[v][i]
		st[-1] = (v,i+1)
		if arr[u]==-1:
			arr[u] = len(rev)
			rev.append(u)
			par[u] = v
			st.append((u,0))

	pred = [[] for _ in range(n)]

	for v in rev:
		for u in adj[v]:
			if arr[u]!=-1:
				pred[u].append(v)

	ancestor = [-1]*n
	label = list(range(n))
	semi = list(range(n))
	idom = [-1]*n
	bucket = [[] for _ in range(n)]

	def eval(v):
		if ancestor[v]==-1:
			return label[v]
		path = []
		x = v
		while ancestor[x]!=-1 and ancestor[ancestor[x]]!=-1:
			path.append(x)
			x = ancestor[x]
		for x in reversed(path):
			a = ancestor[x]
			if arr[semi[label[a]]]<arr[semi[label[x]]]:
				label[x] = label[a]
			ancestor[x] = ancestor[a]
		return label[v]

	N = len(rev)

	for i in range(N-1,0,-1):
		w = rev[i]
		for v in pred[w]:
			u = eval(v)
			if arr[semi[u]]<arr[semi[w]]:
				semi[w] = semi[u]
		bucket[semi[w]].append(w)
		ancestor[w] = par[w]
		for v in bucket[par[w]]:
			u = eval(v)
			if arr[semi[u]]<arr[semi[v]]:
				idom[v] = u
			else:
				idom[v] = par[w]
		bucket[par[w]].clear()

	idom[root] = root
	for i in range(1,N):
		w = rev[i]
		if idom[w]!=semi[w]:
			idom[w] = idom[idom[w]]

	idom[root] = -1
	return idom

def tarjan(gr):
	n = len(gr)
	parent = [-1]*n
	tin = [-1]*n
	tout = [-1]*n
	low = [float('inf')]*n
	visited = [False]*n
	for root in range(n):
		if visited[root]:
			continue
		parent[root] = -1
		stack = [(root,0)]
		while stack:
			u,idx = stack[-1]
			if not visited[u]:
				visited[u] = True
				tin[u] = low[u] = time
				time += 1
			if idx<len(gr[u]):
				v = gr[u][idx]
				stack[-1] = (u,idx+1)
				if v==parent[u]:
					continue
				if not visited[v]:
					parent[v] = u
					stack.append((v,0))
				else:
					low[u] = min(low[u],tin[v])
			else:
				tout[u] = time
				time += 1
				stack.pop()
				if parent[u]!=-1:
					low[parent[u]] = min(low[parent[u]],low[u])
	return tin,tout,low

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
