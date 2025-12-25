class PersistentDSU:
	def __init__(self,n):
		self.parent = list(range(n))
		self.size = [1]*n
		self.time = [float('inf')]*n
	def find(self,node,version):
		# returns root at given version
		while not (self.parent[node]==node or self.time[node]>version):
			node = self.parent[node]
		return node
	def union(self,a,b,time):
		# merges a and b
		a = self.find(a,time)
		b = self.find(b,time)
		if a==b:
			return False
		if self.size[a]>self.size[b]:
			a,b = b,a
		self.parent[a] = b
		self.time[a] = time
		self.size[b] += self.size[a]
		return True
	def isconnected(self,a,b,time):
		return self.find(a,time)==self.find(b,time)