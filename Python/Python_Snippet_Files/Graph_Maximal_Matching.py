def kuhn(d,n,m):
	# n -> left side
	# m -> right side
	# d[left side] -> [right side]
	# Maximal Bipartite matching
	# O(E V)
	match_r = [-1]*m
	match_l = [-1]*n
	for start in range(n):
		if match_l[start]!=-1:
			continue
		stack = [start]
		parent_l = [-1]*n
		parent_r = [-1]*m
		vis_r = [False]*m
		found_v = -1
		while stack:
			u = stack.pop()
			for v in d[u]:
				if vis_r[v]:
					continue
				vis_r[v] = True
				parent_r[v] = u

				if match_r[v]==-1:
					found_v = v
					stack = []
					break
				else:
					next_u = match_r[v]
					if parent_l[next_u]==-1:
						parent_l[next_u] = v
						stack.append(next_u)
		if found_v==-1:
			continue
		v = found_v
		while v!=-1:
			u = parent_r[v]
			next_v = match_l[u]
			match_l[u] = v
			match_r[v] = u
			v = next_v
	result = []
	for u in range(n):
		if match_l[u]!=-1:
			result.append((u, match_l[u]))
	return result

class HopcroftKarp:
	# n_left on left side and n_right on right side
	# O(E root(V))
	def __init__(self, n_left, n_right):
		self.n_left = n_left
		self.n_right = n_right
		self.g = [[] for _ in range(n_left)]
		self.matchL = [-1] * n_left
		self.matchR = [-1] * n_right
		self.dist = [-1] * n_left
	def add(self, u, v):
		self.g[u].append(v)
	def bfs(self):
		q = deque()
		for u in range(self.n_left):
			if self.matchL[u] == -1:
				self.dist[u] = 0
				q.append(u)
			else:
				self.dist[u] = -1
		while q:
			u = q.popleft()
			for v in self.g[u]:
				if self.matchR[v] != -1 and self.dist[self.matchR[v]] == -1:
					self.dist[self.matchR[v]] = self.dist[u] + 1
					q.append(self.matchR[v])
	def dfs(self, u):
		for v in self.g[u]:
			if self.matchR[v] == -1 or (self.dist[self.matchR[v]] == self.dist[u] + 1 and self.dfs(self.matchR[v])):
				self.matchL[u] = v
				self.matchR[v] = u
				return True
		return False
	def max_matching(self,flag=True):
		flow = 0
		if flag:
			for adj in self.g:
				random.shuffle(adj)
		while True:
			self.bfs()
			aug = 0
			for u in range(self.n_left):
				if self.matchL[u] == -1:
					if self.dfs(u):
						aug += 1
			if aug == 0:
				break
			flow += aug
		return flow
	def get_edges(self):
		return [(u, self.matchL[u]) for u in range(self.n_left) if self.matchL[u] != -1]
	def vertex_cover(self):
		visL = [False]*self.n_left
		visR = [False]*self.n_right
		q = deque()
		for u in range(self.n_left):
			if self.matchL[u]==-1:
				q.append(u)
				visL[u] = True
		while q:
			u = q.popleft()
			for v in self.g[u]:
				if not visR[v] and self.matchL[u]!=v:
					visR[v] = True
					if self.matchR[v]!=-1 and not visL[self.matchR[v]]:
						visL[self.matchR[v]] = True
						q.append(self.matchR[v])
		coverL = [u for u in range(self.n_left) if not visL[u]]
		coverR = [v for v in range(self.n_right) if visR[v]]
		return coverL,coverR
