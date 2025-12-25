class HLD:
	def __init__(self, adj, values, root=0,func=max,unit=float('-inf')):
		self.adj = adj
		self.values = values
		self.parent = [-1] * len(adj)
		self.depth = [0] * len(adj)
		self.size = [0] * len(adj)
		self.heavy = [-1] * len(adj)
		self.head = [0] * len(adj)
		self.pos = [0] * len(adj)
		self.flat = [0] * len(adj)
		self.unit = unit
		self.func = func
		self._dfs(root)
		self._decompose(root)
		self.seg = SegmentTree([self.values[self.flat[i]] for i in range(len(self.adj))],func,unit)
	def _dfs(self,start=0):
		visited = [False] * len(self.adj)
		stack = [start]
		while stack:
			start = stack[-1]
			if not visited[start]:
				visited[start] = True
				for child in self.adj[start]:
					if not visited[child]:
						self.parent[child] = start
						self.depth[child] = self.depth[start]+1
						stack.append(child)
			else:
				self.size[stack.pop()] = 1
				k = 0
				for child in self.adj[start]:
					if self.parent[start]!=child:
						self.size[start] += self.size[child]
						if self.size[child]>k:
							k = self.size[child]
							self.heavy[start] = child
		return visited
	def _decompose(self, root):
		stack = [(root,root)]
		time = 0
		while stack:
			u, h = stack.pop()
			self.head[u] = h
			self.flat[time] = u
			self.pos[u] = time
			time += 1
			for v in reversed(self.adj[u]):
				if v!=self.parent[u] and v!=self.heavy[u]:
					stack.append((v, v))
			if self.heavy[u] != -1:
				stack.append((self.heavy[u], h))
	def query(self, u, v):
		res = self.unit
		while self.head[u] != self.head[v]:
			if self.depth[self.head[u]] < self.depth[self.head[v]]:
				u, v = v, u
			res = self.func(res, self.seg.query(self.pos[self.head[u]], self.pos[u] + 1))
			u = self.parent[self.head[u]]
		if self.depth[u] > self.depth[v]:
			u, v = v, u
		return self.func(res, self.seg.query(self.pos[u], self.pos[v] + 1))
	def update(self, u, value):
		self.seg.update(self.pos[u], value)
	def update_path(self, u, v, value):
		while self.head[u] != self.head[v]:
			if self.depth[self.head[u]] < self.depth[self.head[v]]:
				u, v = v, u
			self.seg.range_update(self.pos[self.head[u]], self.pos[u], value)
			u = self.parent[self.head[u]]
		if self.depth[u] > self.depth[v]:
			u, v = v, u
		self.seg.range_update(self.pos[u], self.pos[v], value)
	def add_to_subtree(self, u, value):
		self.seg.range_update(self.pos[u], self.pos[u] + self.size[u] - 1, value)