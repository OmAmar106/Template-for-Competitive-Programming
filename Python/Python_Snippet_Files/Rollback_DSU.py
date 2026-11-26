class RollbackDSU:
	def __init__(self,n):
		self.p=list(range(n)); self.sz=[1]*n; self.st=[]
	def find(self,x):
		while x!=self.p[x]: x=self.p[x]
		return x
	def union(self,a,b):
		a,b=self.find(a),self.find(b)
		if a==b: self.st.append((-1,-1,-1)); return
		if self.sz[a]>self.sz[b]: a,b=b,a
		self.st.append((a,b,self.sz[b]))
		self.p[a]=b; self.sz[b]+=self.sz[a]
	def rollback(self):
		a,b,s=self.st.pop()
		if a==-1: return
		self.p[a]=a; self.sz[b]=s

class ParPersistentDSU:
	# Partially Persistent DSU with no branching
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
