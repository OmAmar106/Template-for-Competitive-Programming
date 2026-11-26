class OfflineDynamicConnectivity:
	def __init__(self,n):
		self.n = n
		self.active = {}
		self.ranges = []
		self.max_time = 0
	def add_edge(self,u,v,t):
		if u>v:
			u,v = v,u
		self.active[(u,v)] = t
		self.max_time = max(self.max_time,t)
	def remove_edge(self,u,v,t):
		if u>v:
			u,v = v,u
		start = self.active.pop((u,v))
		self.ranges.append((start,t,u,v))
		self.max_time = max(self.max_time,t)
	def run(self):
		dsu = RollbackDSU(self.n)
		for (u,v), start in self.active.items():
			self.ranges.append((start,self.max_time+1,u,v))
		T = self.max_time + 1
		base = T
		tree = [[] for _ in range(2 * base)]
		for l,r,u,v in self.ranges:
			l += base
			r += base
			while l<r:
				if l&1:
					tree[l].append((u,v))
					l += 1
				if r&1:
					r -= 1
					tree[r].append((u,v))
				l >>= 1
				r >>= 1
		ans = [None] * T
		stack = [(1,0)]
		while stack:
			node,state = stack.pop()
			if state==0:
				for u,v in tree[node]:
					dsu.union(u,v)
				stack.append((node,1))
				if node<base:
					stack.append((node*2+1,0))
					stack.append((node*2,0))
				else:
					t = node-base
					if t<T:
						ans[t] = dsu.size
						# implement a size function
						# size-- on union
			else:
				for _ in tree[node]:
					dsu.rollback()
		return ans
