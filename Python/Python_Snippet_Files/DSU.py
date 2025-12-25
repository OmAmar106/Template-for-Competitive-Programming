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

	def union(self, a, b):
		self.parent[self.find(b)] = self.find(a)


class DisjointSetUnion:
	def __init__(self, n):
		self.parent = list(range(n))
		# self.s = set(self.parent)
		self.size = [1] * n

	def find(self, a):
		acopy = a
		while a != self.parent[a]:
			a = self.parent[a]
		while acopy != a:
			self.parent[acopy], acopy = a, self.parent[acopy]
		return a

	def union(self, a, b):
		a, b = self.find(a), self.find(b)
		if a != b:
			if self.size[a] < self.size[b]:
				a, b = b, a
			# self.s.remove(b)
			self.parent[b] = a
			self.size[a] += self.size[b]

	def set_size(self, a):
		return self.size[self.find(a)]

	def __len__(self):
		return len(self.s)

	def notfind(self, a):
		k = self.find(a)
		for j in self.s:
			if j!=k:
				return j
		return -1