def solve_quadratic(a, b, c):
	if a == 0:return None
	D = b*b - 4*a*c
	if D < 0:return None
	s = math.isqrt(D)
	if s*s != D:return None
	den = 2*a
	if den == 0:return None
	x1, r1 = divmod(-b + s, den)
	x2, r2 = divmod(-b - s, den)
	if r1!=0 or r2!=0:return None
	return (x1, x2)

def solve_cubic(a, b, c, d):
	if a == 0:return None
	roots = []
	for x in range(-math.isqrt(abs(d)) - 1, math.isqrt(abs(d)) + 2):
		if a*x*x*x + b*x*x + c*x + d == 0:
			roots.append(x)
	return tuple(roots) if roots else None

def compute_rank(A):
	EPS = 1e-9
	A = [row[:] for row in A]
	n = len(A)
	m = len(A[0])
	rank = 0
	row_selected = [False] * n
	for i in range(m):
		j = 0
		while j < n:
			if not row_selected[j] and abs(A[j][i]) > EPS:
				break
			j += 1
		if j != n:
			rank += 1
			row_selected[j] = True
			for p in range(i + 1, m):
				A[j][p] /= A[j][i]
			for k in range(n):
				if k != j and abs(A[k][i]) > EPS:
					for p in range(i + 1, m):
						A[k][p] -= A[j][p] * A[k][i]
	return rank

class XorBasis:
	def __init__(self,A=[]):
		self.reduced_base = {}
		self.how = {}
		self.base = {}
		for i in A:
			self.add(i)
	def max(self):
		base = self.base; reduced_base = self.reduced_base
		how = self.how
		x = 0;tmp = 0;ans=[]
		for j in sorted(reduced_base, reverse=True):
			if not x & (1 << j):
				x ^= reduced_base[j]
				tmp ^= how[j]
				ans.append(base[j])
		# xor of these elements return the max element
		return ans
	def make(self,k):
		# returns True if can make x with these elements
		reduced_base = self.reduced_base
		for j in range(k.bit_length()-1,-1,-1):
			if ((1<<j)&k):
				if j in reduced_base:
					k ^= reduced_base[j]
				else:
					return False
		return k==0
	def add(self,a):
		# adds a to the basis
		reduced_base = self.reduced_base
		how = self.how;base = self.base
		tmp = 0
		while a:
			b = a.bit_length() - 1
			if b in reduced_base:
				a ^= reduced_base[b]
				tmp ^= how[b]
			else:
				reduced_base[b] = a
				how[b] = tmp | (1 << len(base))
				base[b] = a
				break

def simplex_bland(c, A, b, frac=False):
	# maximize ci.xi
	# given ai.xi <= bi and xi >= 0
	if not frac:
		n = len(c)
		m = len(b)
		T = [A[i] + [0]*i + [1] + [0]*(m-i-1) + [b[i]] for i in range(m)]
		T.append([-ci for ci in c] + [0]*m + [0])
		N = list(range(n)) # non-basic
		B = list(range(n, n+m)) # basic
		def pivot(r, s):
			# Make coeffecient of pivot row 1 and Eliminate column s in all other rows
			T[r] = [v / T[r][s] for v in T[r]]
			for i in range(len(T)):
				if i != r:
					fac = T[i][s]
					T[i] = [T[i][j] - fac * T[r][j] for j in range(len(T[0]))]
		while True:
			s = None
			for j in range(len(T[0]) - 1):
				if T[-1][j] < 0:
					s = j
					break
			if s is None:
				break
			# leaving row
			r = None
			for i in range(m):
				if T[i][s] > 1e-12:
					ratio = T[i][-1] / T[i][s]
					if r is None or ratio < T[r][-1] / T[r][s]:
						r = i
			if r is None:
				return None
			pivot(r, s)
			B[r], N[s] = N[s], B[r]
		x = [0] * (n + m)
		for i in range(m):
			x[B[i]] = T[i][-1]
		return x[:n], T[-1][-1]
	else:
		from fractions import Fraction
		n = len(c)
		m = len(b)
		c = [Fraction(ci) for ci in c]
		A = [[Fraction(aij) for aij in row] for row in A]
		b = [Fraction(bi) for bi in b]
		T = [A[i] + [Fraction(1 if i == j else 0) for j in range(m)] + [b[i]]
			 for i in range(m)]
		T.append([-ci for ci in c] + [Fraction(0)] * (m + 1))
		N = list(range(n))
		B = list(range(n, n+m))
		def pivot(r, s):
			piv = T[r][s]
			T[r] = [v / piv for v in T[r]]
			for i in range(m + 1):
				if i != r:
					fac = T[i][s]
					T[i] = [T[i][j] - fac * T[r][j] for j in range(len(T[0]))]
		while True:
			s = None
			for j in range(len(T[0]) - 1):
				if T[-1][j] < 0:
					s = j
					break
			if s is None:
				break
			r = None
			for i in range(m):
				if T[i][s] > 0:
					ratio = T[i][-1] / T[i][s]
					if r is None or ratio < T[r][-1] / T[r][s]:
						r = i
			if r is None:
				return None
			pivot(r, s)
			B[r], N[s] = N[s], B[r]
		x = [Fraction(0)] * (n + m)
		for i in range(m):
			x[B[i]] = T[i][-1]
		return x[:n], T[-1][-1]

def s_lr(l,r,pow=1):
	if l>r:return 0
	if pow==1:return (r*(r+1)//2) - ((l-1)*l//2)
	elif pow==2:return (r*(r+1)*(2*r+1)//6) - ((l-1)*l*(2*l-1)//6)
	elif pow==3:return (r*(r+1)//2)**2 - ((l-1)*l//2)**2
	else:return None
