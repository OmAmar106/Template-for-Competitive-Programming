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


class HLD_F:
	def __init__(self, adj, val):
		n = len(adj)
		parent = [-1]*n
		depth = [0]*n
		size = [0]*n
		heavy = [-1]*n
		head = [0]*n
		pos = [0]*n
		stack = [(0, -1, 0)]
		while stack:
			u, p, state = stack.pop()
			if state == 0:
				stack.append((u, p, 1))
				du = depth[u]
				for v in adj[u]:
					if v == p: continue
					parent[v] = u
					depth[v] = du + 1
					stack.append((v, u, 0))
			else:
				size[u] = 1
				mx = 0
				pu = parent[u]
				for v in adj[u]:
					if v == pu: continue
					sv = size[v]
					size[u] += sv
					if sv > mx:
						mx = sv
						heavy[u] = v
		cur = 0
		stack = [(0, 0)]
		while stack:
			u, h = stack.pop()
			while u != -1:
				head[u] = h
				pos[u] = cur
				cur += 1
				hu = heavy[u]
				pu = parent[u]
				for v in adj[u]:
					if v != pu and v != hu:
						stack.append((v, v))
				u = hu
		sizeN = 1 << (n.bit_length())
		seg = [0] * (2 * sizeN)
		for i in range(n):
			seg[sizeN + pos[i]] = val[i]
		for i in range(sizeN - 1, 0, -1):
			left = seg[2*i]
			right = seg[2*i+1]
			seg[i] = left if left > right else right
		self.parent = parent
		self.depth = depth
		self.size = size
		self.heavy = heavy
		self.head = head
		self.pos = pos
		self.seg = seg
		self.N = sizeN
	def update(self, u, x):
		seg = self.seg
		i = self.pos[u] + self.N
		seg[i] = x
		i >>= 1
		while i:
			seg[i] = max(seg[2*i],seg[2*i+1])
			i >>= 1
	def query(self, u, v):
		res = 0
		seg = self.seg; N = self.N
		head = self.head; depth = self.depth
		parent = self.parent; pos = self.pos
		while head[u]!=head[v]:
			if depth[head[u]] < depth[head[v]]:
				u, v = v, u
			l = pos[head[u]] + N
			r = pos[u] + N + 1
			while l < r:
				if l & 1: res = max(res, seg[l]); l += 1
				if r & 1: r ^= 1; res = max(res, seg[r])
				l >>= 1; r >>= 1
			u = parent[head[u]]

		if depth[u] > depth[v]:
			u, v = v, u

		l = pos[u]+N
		r = pos[v]+N+1
		while l < r:
			if l & 1: res = max(res, seg[l]); l += 1
			if r & 1: r ^= 1; res = max(res, seg[r])
			l >>= 1; r >>= 1

		return res
