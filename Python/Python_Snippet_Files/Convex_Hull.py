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

class LiChao:
	__slots__ = ("lo","hi","mid","m","b","left","right")
	# lo = min value of x that you will query
	def __init__(self,lo,hi):
		self.lo = lo
		self.hi = hi
		self.mid = (lo+hi)>>1
		self.m = None
		self.b = None
		self.left = None
		self.right = None
	def add_line(self,m,b):
		node = self
		while True:
			lo,hi,mid = node.lo,node.hi,node.mid
			if node.m is None:
				node.m,node.b = m,b
				return
			cur_m,cur_b = node.m,node.b
			if m*mid+b>cur_m*mid+cur_b:
				node.m,m = m,cur_m
				node.b,b = b,cur_b
				cur_m,cur_b = node.m,node.b
			if lo==hi:
				return
			if m*lo+b>cur_m*lo+cur_b:
				if node.left is None:
					node.left = LiChao(lo,mid)
				node = node.left
			elif m*hi+b>cur_m*hi +cur_b:
				if node.right is None:
					node.right = LiChao(mid+1,hi)
				node = node.right
			else:
				return
	def query(self,x):
		node = self
		res = -10**18
		while node:
			if node.m is not None:
				v = node.m*x+node.b
				if v>res:
					res = v
			if node.lo==node.hi:
				break
			if x<=node.mid:
				node = node.left
			else:
				node = node.right
		return res
