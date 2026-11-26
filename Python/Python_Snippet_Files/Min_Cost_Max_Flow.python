class MCMF:
	# better when the flow is not constant
	# O(FEV)
	def __init__(self, n):
		self.n = n
		self.g = [[] for _ in range(n)]
	def add_edge(self, u, v, cap, cost):
		self.g[u].append([v, cap, cost, len(self.g[v]), cap])
		self.g[v].append([u, 0, -cost, len(self.g[u]) - 1, 0])
	def min_cost(self, s, t, maxf=float('inf')):
		n = self.n
		flow, cost = 0, 0
		pot = [0] * n
		while flow < maxf:
			dist = [float('inf')] * n
			parent = [(-1, -1)] * n
			dist[s] = 0
			pq = [(0, s)]
			while pq:
				d, u = heappop(pq)
				if d > dist[u]:
					continue
				for i, (v, cap, w, rev, _) in enumerate(self.g[u]):
					if cap > 0:
						nd = d + w + pot[u] - pot[v]
						if nd < dist[v]:
							dist[v] = nd
							parent[v] = (u, i)
							heappush(pq, (nd, v))
			if dist[t] == float('inf'):
				break
			for i in range(n):
				if dist[i] < float('inf'):
					pot[i] += dist[i]
			f = maxf - flow
			cur = t
			while cur != s:
				u, i = parent[cur]
				f = min(f, self.g[u][i][1])
				cur = u
			flow += f
			cost += f * pot[t]
			cur = t
			while cur != s:
				u, i = parent[cur]
				v, cap, w, rev, orig = self.g[u][i]
				self.g[u][i][1] -= f
				self.g[cur][rev][1] += f
				cur = u
		return flow, cost
	def used_edges(self):
		res = []
		for u in range(self.n):
			for v, cap, cost, rev, orig in self.g[u]:
				if orig > 0 and cap == 0:
					res.append((u, v, cost))
		return res

def hungarian(cost):
	# better when the flow is 1 for every edge
	# for i in range(n):print(i+1,match[i]+1)
	# this is the final edges taken
	# O(n3)
	n = len(cost)
	u = [0]*(n+1)
	v = [0]*(n+1)
	p = [0]*(n+1)
	way = [0]*(n+1)
	for i in range(1, n+1):
		p[0] = i
		j0 = 0
		minv = [float('inf')]*(n+1)
		used = [False]*(n+1)
		while True:
			used[j0] = True
			i0 = p[j0]
			delta = float('inf')
			j1 = 0
			for j in range(1, n+1):
				if not used[j]:
					cur = cost[i0-1][j-1] - u[i0] - v[j]
					if cur < minv[j]:
						minv[j] = cur
						way[j] = j0
					if minv[j] < delta:
						delta = minv[j]
						j1 = j
			for j in range(n+1):
				if used[j]:
					u[p[j]] += delta
					v[j] -= delta
				else:
					minv[j] -= delta
			j0 = j1
			if p[j0] == 0:
				break
		while True:
			j1 = way[j0]
			p[j0] = p[j1]
			j0 = j1
			if j0 == 0:
				break
	match = [-1]*n
	for j in range(1, n+1):
		if p[j] != 0:
			match[p[j]-1] = j-1
	return -v[0], match
