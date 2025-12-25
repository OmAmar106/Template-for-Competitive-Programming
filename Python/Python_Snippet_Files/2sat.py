def kahn(graph):
	n = len(graph)
	indeg, idx = [0] * n, [0] * n
	for i in range(n):
		for e in graph[i]:
			indeg[e] += 1
	q, res = [], []
	for i in range(n):
		if indeg[i] == 0:
			q.append(i)
	nr = 0
	while q:
		res.append(q.pop())
		idx[res[-1]], nr = nr, nr + 1
		for e in graph[res[-1]]:
			indeg[e] -= 1
			if indeg[e] == 0:
				q.append(e)
	return res, idx, nr == n

def find_SCC(graph):
	SCC, S, P = [], [], []
	depth = [0] * len(graph)
	stack = list(range(len(graph)))
	while stack:
		node = stack.pop()
		if node < 0:
			d = depth[~node] - 1
			if P[-1] > d:
				SCC.append(S[d:])
				del S[d:], P[-1]
				for node in SCC[-1]:
					depth[node] = -1
		elif depth[node] > 0:
			while P[-1] > depth[node]:
				P.pop()
		elif depth[node] == 0:
			S.append(node)
			P.append(len(S))
			depth[node] = len(S)
			stack.append(~node)
			stack += graph[node]
	return SCC[::-1]

class TwoSat:
	def __init__(self, n):
		self.n = n
		self.graph = [[] for _ in range(2 * n)]
	def negate(self, x):
		return x+self.n if x<self.n else x-self.n
	def _imply(self, x, y):
		# agar x hoga , toh y hoga
		self.graph[x].append(y)
		self.graph[self.negate(y)].append(self.negate(x))
	def either(self, x, y):
		# koi ek true ho sakta hain ya dono bhi
		self._imply(self.negate(x),y)
		self._imply(self.negate(y),x)
	def set(self, x):
		self._imply(self.negate(x),x)
	def solve(self):
		SCC = find_SCC(self.graph)
		order = [0] * (2 * self.n)
		for i, comp in enumerate(SCC):
			for x in comp:
				order[x] = i
		for i in range(self.n):
			if order[i] == order[self.negate(i)]:
				return False, None
		return True, [+(order[i] > order[self.negate(i)]) for i in range(self.n)]