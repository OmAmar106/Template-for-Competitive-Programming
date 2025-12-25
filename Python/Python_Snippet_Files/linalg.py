def max_xor(A,flag=True):
	base = []
	how = {}
	reduced_base = {}
	for i in range(len(A)):
		a = A[i]
		tmp = 0
		while a:
			b = a.bit_length() - 1
			if b in reduced_base:
				a ^= reduced_base[b]
				tmp ^= how[b]
			else:
				reduced_base[b] = a
				how[b] = tmp | (1 << len(base))
				base.append(i)
				break
	x = 0
	tmp = 0
	for j in sorted(reduced_base, reverse=True):
		if not x & (1 << j):
			x ^= reduced_base[j]
			tmp ^= how[j]
	if flag:
		# elements whose combination returns all possible
		# subet xors
		return list(reduced_base.values())
	# elements whose xor is maximum
	return [base[j] for j in range(len(base)) if tmp & (1 << j)]

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