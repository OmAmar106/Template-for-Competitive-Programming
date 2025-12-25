class ConvexHull:
	def __init__(self, n=100000):
		# put n equal to max value of ai , bi , you may need to do coordinate compression in case it is upto 10**9
		# works for value which are not increasing as well
		self.n = n
		self.seg = [Line(0, float('inf'))] * (4 * n)
		self.lo = [0] * (4 * n)
		self.hi = [0] * (4 * n)
		self.build(1,1,n)
	def build(self, i, l, r):
		stack = [(i, l, r)]
		while stack:
			idx, left, right = stack.pop()
			self.lo[idx] = left
			self.hi[idx] = right
			self.seg[idx] = Line(0, float('inf'))
			if left == right:
				continue
			mid = (left + right) // 2
			stack.append((2 * idx + 1, mid + 1, right))
			stack.append((2 * idx, left, mid))
	def insert(self,L):
		pos = 1
		while True:
			l, r = self.lo[pos], self.hi[pos]
			if l == r:
				if L(l) < self.seg[pos](l):
					self.seg[pos] = L
				break
			m = (l + r) // 2
			if self.seg[pos].m < L.m:
				self.seg[pos], L = L, self.seg[pos]
			if self.seg[pos](m) > L(m):
				self.seg[pos], L = L, self.seg[pos]
				pos = 2*pos
			else:
				pos = 2*pos+1
	def query(self,x):
		i = 1
		res = self.seg[i](x)
		pos = i
		while True:
			l, r = self.lo[pos], self.hi[pos]
			if l == r:
				return min(res, self.seg[pos](x))
			m = (l + r) // 2
			if x < m:
				res = min(res, self.seg[pos](x))
				pos = 2 * pos
			else:
				res = min(res, self.seg[pos](x))
				pos = (2 * pos + 1)

def f(line, x):
	return line[0] * x + line[1]
class LiChao:
	def __init__(self, lo=0, hi=10**9):
		self.lo = lo
		self.hi = hi
		self.m = (lo + hi) // 2
		self.line = None
		self.left = None
		self.right = None
	def add_line(self, new_line):
		l, r, m = self.lo, self.hi, self.m
		if self.line is None:
			self.line = new_line
			return
		if f(new_line, m) > f(self.line, m):
			self.line, new_line = new_line, self.line
		if l == r:
			return
		if f(new_line, l) > f(self.line, l):
			if self.left is None:
				self.left = LiChao(l, m)
			self.left.add_line(new_line)
		elif f(new_line, r) > f(self.line, r):
			if self.right is None:
				self.right = LiChao(m + 1, r)
			self.right.add_line(new_line)
	def query(self, x):
		res = f(self.line, x) if self.line is not None else -10**18
		if self.lo == self.hi:
			return res
		if x <= self.m and self.left is not None:
			res = max(res, self.left.query(x))
		elif x > self.m and self.right is not None:
			res = max(res, self.right.query(x))
		return res

class Line:
	def __init__(self, m, b, c=0):
		# c is an identifier for the line
		self.m = m;self.b = b;self.c = c
	def __call__(self, x):
		return self.m * x + self.b
class CHT:
	def __init__(self):
		self.dq = []
		self.fptr = 0
	def clear(self):
		self.dq = [Line(0, 0, 0)]
		self.fptr = 0
	def pop_back(self, L, L1, L2):
		v1 = (L.b - L2.b) * (L2.m - L1.m)
		v2 = (L2.m - L.m) * (L1.b - L2.b)
		return (L.c > L1.c if v1 == v2 else v1 < v2)
	def pop_front(self, L1, L2, x):
		v1 = L1(x)
		v2 = L2(x)
		return (L1.c < L2.c if v1 == v2 else v1 > v2)
	def insert(self, L):
		while len(self.dq) - self.fptr >= 2 and self.pop_back(L, self.dq[-1], self.dq[-2]):
			self.dq.pop()
		self.dq.append(L)
	def query(self, x):
		while len(self.dq) - self.fptr >= 2 and self.pop_front(self.dq[self.fptr], self.dq[self.fptr + 1], x):
			self.fptr += 1
		line = self.dq[self.fptr]
		return line(x),line.c