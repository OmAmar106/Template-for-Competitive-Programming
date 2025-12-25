class UnionFind:
	def __init__(self, n):
		self.parent = list(range(n))
	def find(self, a):
		acopy = a
		while a != self.parent[a]:
			a = self.parent[a]
		while acopy != a:
			self.parent[acopy], acopy = a, self.parent[acopy]
		return a
	def merge(self, a, b):
		self.parent[self.find(b)] = self.find(a)

def kruskal(edges,n=None):
	if not n:
		n = len(edges)+1
	edges = sorted(edges,key=lambda x:x[2])
	union = UnionFind(n)
	ans = []
	val = 0
	for u,v,w in edges:
		t = union.find(u)
		t1 = union.find(v)
		if t!=t1:
			val += w
			union.parent[t1] = t
			ans.append((u,v,w))
	return ans,val

def dfs(graph):
	starttime = [[0,0] for i in range(len(graph))]
	time = 0
	stack = [(0,-1,0)]
	while stack:
		cur, prev, state = stack.pop()
		if state == 0:
			starttime[cur][0] = time
			time += 1
			stack.append((cur, prev, 1))
			for neighbor in graph[cur]:
				if neighbor == prev:
					continue
				stack.append((neighbor, cur, 0))
		elif state == 1:
			starttime[cur][1] = time
	return starttime

def is_bipartite(graph):
	n = len(graph)
	color = [-1] * n
	for start in range(n):
		if color[start] == -1:
			color[start] = 0
			stack = [start]
			while stack:
				parent = stack.pop()
				for child in graph[parent]:
					if color[child] == -1:
						color[child] = 1 - color[parent]
						stack.append(child)
					elif color[parent] == color[child]:
						return False, color
	return True, color