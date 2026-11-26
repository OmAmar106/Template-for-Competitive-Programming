class SegTree2DInlined:
	def __init__(self, a, combine, modify_op, identity):
		self.n = len(a)
		self.m = len(a[0])
		self.vals = (
			[[identity]*(2*self.m) for _ in range(self.n)] +
			[[identity]*self.m + row for row in a]
		)
		for i in range(self.n, 2*self.n):
			bar = self.vals[i]
			for j in reversed(range(1, self.m)):
				bar[j] = combine(bar[j<<1], bar[j<<1|1])
		for i in reversed(range(1, self.n)):
			bar = self.vals[i]
			lbar = self.vals[i<<1]
			rbar = self.vals[i<<1|1]
			for j in range(1, 2*self.m):
				bar[j] = combine(lbar[j], rbar[j])
		self.combine = combine
		self.modify_op = modify_op
		self.identity = identity


	def modify(self, i, j, x):
		i += self.n
		j0 = j + self.n
		basebar = self.vals[i]
		basebar[j0] = self.modify_op(basebar[j0], x)
		j = j0 // 2
		while j:
			basebar[j] = self.combine(basebar[j<<1], basebar[j<<1|1])
			j //= 2
		i //= 2
		while i:
			bar = self.vals[i]
			lbar = self.vals[i<<1]
			rbar = self.vals[i<<1|1]
			j = j0
			while j:
				bar[j] = self.combine(lbar[j], rbar[j])
				j //= 2
			i //= 2

	def _get_tour(self, l, r):
		l += self.n
		r += self.n
		ltour = []
		rtour = []
		while l < r:
			if l & 1:
				ltour.append(l)
				l += 1
			if r & 1:
				r -= 1
				rtour.append(r)
			l //= 2
			r //= 2
		rtour.reverse()
		return ltour + rtour

	# [i,I) [j,J)
	def query(self, i, j, I, J):
		tour = self._get_tour(j, J)
		if i == I or j == J:
			return self.identity
		u = i + self.n
		d = I + self.n

		ret = self.identity
		while u < d:
			if u & 1:
				bar = self.vals[u]
				for pos in tour:
					ret = self.combine(ret, bar[pos])
				u += 1
			if d & 1:
				d -= 1
				bar = self.vals[d]
				for pos in tour:
					ret = self.combine(ret, bar[pos])
			u //= 2
			d //= 2

		return ret
