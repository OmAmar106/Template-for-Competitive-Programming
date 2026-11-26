class MinCut:
	def __init__(self,n):
		self.n = n
		self.mc = HLPP(n)
		self.edges = []
		self.source_edges = []
	def add_edge(self,u,v,c):
		# u->v directed edge
		# add v->u as well for bidirectional edge
		i = len(self.mc.g[u])
		self.mc.add_edge(u,v,c)
		rev = self.mc.g[u][i][2]
		self.edges.append((u,v))
		self.source_edges.append((u,i,v,rev,c))
	def calc(self,s,t):
		self.mc.maxflow(s,t)
		residual = {}
		for u,i,v,rev,c in self.source_edges:
			if u==s:
				residual[i] = c-self.mc.g[v][rev][1]
		vis = [False]*self.n
		vis[s] = True
		q = [s]
		for u in q:
			for i,(v,c,rev) in enumerate(self.mc.g[u]):
				if u==s:
					c = residual.get(i,c)
				if c>0 and not vis[v]:
					vis[v] = True
					q.append(v)
		return [(u,v) for u,v in self.edges if vis[u] and not vis[v]]

class HLPP:
	# O(V²E), still sometime unexpectedly faster than Dinic
	def __init__(self,n):
		self.n=n
		self.g=[[] for _ in range(n)]
	def add_edge(self,u,v,c):
		self.g[u].append([v,c,len(self.g[v])])
		self.g[v].append([u,0,len(self.g[u])-1])
	def maxflow(self,s,t):
		n,g=self.n,self.g
		h=[0]*n; ex=[0]*n
		seen=[0]*n
		h[s]=n
		for v,c,rev in g[s]:
			if c:
				g[v][rev][1]+=c
				ex[v]+=c
		q=deque([i for i in range(n) if i!=s and i!=t and ex[i]>0])
		def push(u,e):
			v,c,rev=e
			d=min(ex[u],c)
			if h[u]==h[v]+1 and d>0:
				e[1]-=d; g[v][rev][1]+=d
				ex[u]-=d; ex[v]+=d
				if ex[v]==d and v!=s and v!=t:
					q.append(v)
				return True
			return False
		def relabel(u):
			h[u]=min(h[v]+1 for v,c,_ in g[u] if c>0)
		while q:
			u=q[0]
			while ex[u]:
				if seen[u]<len(g[u]):
					if not push(u,g[u][seen[u]]):
						seen[u]+=1
				else:
					relabel(u)
					seen[u]=0
			q.popleft()
		return ex[t]

class Dinic:
	# O(V²E)
	# Unit capacities/bipartite/DAG: ~O(E√V)
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
		INF = float('inf')
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
	def get_paths(self,s,t):
		# returns that paths taken for the maxflow
		paths=[]
		while True:
			stack=[(s,[],float('inf'),set([s]))]
			found=False
			while stack:
				v,path,f,visited=stack.pop()
				if v==t:
					pushed=f
					res_path=path
					found=True
					break
				for i,e in enumerate(self.adj[v]):
					to,rev,cap,flow=e
					if flow>0 and to not in visited:
						stack.append((to,path+[(v,to)],min(f,flow),visited|{to}))
			if not found:
				break
			f=pushed
			for u,w in res_path:
				for e in self.adj[u]:
					if e[0]==w and e[3]>0:
						e[3]-=f
						self.adj[w][e[1]][3]+=f
						break
			paths.append((pushed,res_path))
		return paths
