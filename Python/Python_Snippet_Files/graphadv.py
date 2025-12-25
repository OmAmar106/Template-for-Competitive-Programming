INF = float("inf")
class Dinic:
	def __init__(self, n):
		self.lvl = [0] * n
		self.ptr = [0] * n
		self.q = [0] * n
		self.adj = [[] for _ in range(n)]
	def add_edge(self, a, b, c, rcap=0):
		self.adj[a].append([b, len(self.adj[b]), c, 0])
		self.adj[b].append([a, len(self.adj[a]) - 1, rcap, 0])
	def dfs(self, v, t, f):
		if v == t or not f:
			return f
		for i in range(self.ptr[v], len(self.adj[v])):
			e = self.adj[v][i]
			if self.lvl[e[0]] == self.lvl[v] + 1:
				p = self.dfs(e[0], t, min(f, e[2] - e[3]))
				if p:
					self.adj[v][i][3] += p
					self.adj[e[0]][e[1]][3] -= p
					return p
			self.ptr[v] += 1
		return 0
	def calc(self, s, t):
		flow, self.q[0] = 0, s
		for l in range(31):  # l = 30 maybe faster for random data
			while True:
				self.lvl, self.ptr = [0] * len(self.q), [0] * len(self.q)
				qi, qe, self.lvl[s] = 0, 1, 1
				while qi < qe and not self.lvl[t]:
					v = self.q[qi]
					qi += 1
					for e in self.adj[v]:
						if not self.lvl[e[0]] and (e[2] - e[3]) >> (30 - l):
							self.q[qe] = e[0]
							qe += 1
							self.lvl[e[0]] = self.lvl[v] + 1
				p = self.dfs(s, t, INF)
				while p:
					flow += p
					p = self.dfs(s, t, INF)
				if not self.lvl[t]:
					break
		return flow

class AuxiliaryTree:
	def __init__(self, edge, root = 0):
		self.n = len(edge)
		self.order = [-1] * self.n
		self.path = [-1] * (self.n-1)
		self.depth = [0] * self.n
		if self.n == 1: return
		parent = [-1] * self.n
		que = [root]
		t = -1
		while que:
			u = que.pop()
			self.path[t] = parent[u]
			t += 1
			self.order[u] = t
			for v in edge[u]:
				if self.order[v] == -1:
					que.append(v)
					parent[v] = u
					self.depth[v] = self.depth[u] + 1
		self.n -= 1
		self.h = self.n.bit_length()
		self.data = [0] * (self.n * self.h)
		self.data[:self.n] = [self.order[u] for u in self.path]
		for i in range(1, self.h):
			for j in range(self.n - (1<<i) + 1):
				self.data[i*self.n + j] = min(self.data[(i-1)*self.n + j], self.data[(i-1)*self.n + j+(1<<(i-1))])

	def lca(self, u, v):
		if u == v: return u
		l = self.order[u]
		r = self.order[v]
		if l > r:
			l,r = r,l
		level = (r - l).bit_length() - 1
		return self.path[min(self.data[level*self.n + l], self.data[level*self.n + r-(1<<level)])]

	def dis(self, u, v):
		if u == v: return 0
		l = self.order[u]
		r = self.order[v]
		if l > r:
			l,r = r,l
		level = (r - l).bit_length() - 1
		p = self.path[min(self.data[level*self.n + l], self.data[level*self.n + r-(1<<level)])]
		return self.depth[u] + self.depth[v] - 2 * self.depth[p]

	def make(self, vs):
		k = len(vs)
		vs.sort(key = self.order.__getitem__)

		par = dict()
		edge = dict()
		edge[vs[0]] = []

		st = [vs[0]]

		for i in range(k - 1):
			l = self.order[vs[i]]
			r = self.order[vs[i+1]]
			level = (r - l).bit_length() - 1
			w = self.path[min(self.data[level*self.n + l], self.data[level*self.n + r-(1<<level)])]
			if w != vs[i]:
				p = st.pop()
				while st and self.depth[w] < self.depth[st[-1]]:
					par[p] = st[-1]
					edge[st[-1]].append(p)
					p = st.pop()

				if not st or st[-1] != w:
					st.append(w)
					edge[w] = [p]
				else:
					edge[w].append(p)
				par[p] = w

			st.append(vs[i+1])
			edge[vs[i+1]] = []

		for i in range(len(st) - 1):
			edge[st[i]].append(st[i+1])
			par[st[i+1]] = st[i]

		par[st[0]] = -1
		return st[0], edge, par

class binary_lift:
	def __init__(self, graph, f=max, root=0, flag=False):
		n = len(graph)
		parent = [-1] * (n + 1)
		depth = self.depth = [-1] * n
		bfs = [root]
		depth[root] = 0
		data = [0]*n
		for node in bfs:
			# for nei,w in graph[node]:
			for nei in graph[node]:
				if depth[nei] == -1:
					# data[nei] = w
					parent[nei] = node
					depth[nei] = depth[node] + 1
					bfs.append(nei)
		parent = self.parent = [parent]
		self.f = f
		if flag:
			data = self.data = [data]
			for _ in range(max(depth).bit_length()):
				old_data = data[-1]
				old_parent = parent[-1]
				data.append([f(val, old_data[p]) for val,p in zip(old_data, old_parent)])
				parent.append([old_parent[p] for p in old_parent])
		else:
			for _ in range(max(depth).bit_length()):
				old_parent = parent[-1]
				parent.append([old_parent[p] for p in old_parent])
	def lca(self, a, b):
		depth = self.depth
		parent = self.parent
		if depth[a] < depth[b]:
			a,b = b,a
		d = depth[a] - depth[b]
		for i in range(d.bit_length()):
			if (d >> i) & 1:
				a = parent[i][a]
		for i in range(depth[a].bit_length())[::-1]:
			if parent[i][a] != parent[i][b]:
				a = parent[i][a]
				b = parent[i][b]
		if a != b:
			return parent[0][a]
		else:
			return a
	def distance(self, a, b):
		return self.depth[a] + self.depth[b] - 2 * self.depth[self.lca(a,b)]
	def kth_ancestor(self, a, k):
		parent = self.parent
		if self.depth[a] < k:
			return -1
		for i in range(k.bit_length()):
			if (k >> i) & 1:
				a = parent[i][a]
		return a
	def __call__(self, a, b, c=0):
		depth = self.depth
		parent = self.parent
		data = self.data
		f = self.f
		c = self.lca(a, b)
		val = c
		for x,d in (a, depth[a] - depth[c]), (b, depth[b] - depth[c]):
			for i in range(d.bit_length()):
				if (d >> i) & 1:
					val = f(val, data[i][x])
					x = parent[i][x]
		return val