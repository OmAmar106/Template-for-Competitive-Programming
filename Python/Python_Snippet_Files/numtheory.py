def miller_is_prime(n):
	"""
		Miller-Rabin test - O(7 * log2n)
		Has 100% success rate for numbers less than 3e+9
		use it in case of TC problem
	"""
	if n < 5 or n & 1 == 0 or n % 3 == 0:
		return 2 <= n <= 3
	s = ((n - 1) & (1 - n)).bit_length() - 1
	d = n >> s
	for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
		p = pow(a, d, n)
		if p == 1 or p == n - 1 or a % n == 0:
			continue
		for _ in range(s):
			p = (p * p) % n
			if p == n - 1:
				break
		else:
			return False
	return True

def is_prime(n):
	if n <= 1:
		return False
	if n <= 3:
		return True
	if n % 2 == 0 or n % 3 == 0:
		return False
	i = 5
	while i * i <= n:
		if n % i == 0 or n % (i + 2) == 0:
			return False
		i += 6
	return True

def sieve(n):
	primes = []
	isp = [1] * (n+1)
	isp[0] = isp[1] = 0
	for i in range(2,n+1):
		if isp[i]:
			primes.append(i)
			for j in range(i*i,n+1,i):
				isp[j] = 0
	return primes

def all_fact(n):
	"""
	returns a sorted list of all distinct factors of n in root n
	"""
	small, large = [], []
	for i in range(1, int(n**0.5) + 1, 2 if n & 1 else 1):
		if not n % i:
			small.append(i)
			large.append(n // i)
	if small[-1] == large[-1]:
		large.pop()
	large.reverse()
	small.extend(large)
	return small

calc = False
if calc:
	def sieve_unique(N):
		mini = [i for i in range(N)]
		for i in range(2,N):
			if mini[i]==i:
				for j in range(2*i,N,i):
					mini[j] = i
		return mini

	MAX_N = 10**6+1
	Lmini = sieve_unique(MAX_N)

	def prime_factors(k,typ=0):
		"""
			When the numbers are large this is the best method to get
			unique prime factors, precompute n log log n , then each query is log n
		"""
		if typ==0:
			ans = Counter()
		elif typ==1:
			ans = set()
		else:
			ans = []
		while k!=1:
			if typ==0:
				ans[Lmini[k]] += 1
			elif typ==1:
				ans.add(Lmini[k])
			else:
				ans.append(Lmini[k])
			k //= Lmini[k]
		return ans

	def all_factors(x):
		# returns all factors of x in log x + d
		L = list(prime_factors(x).items())
		st = [1]
		for i in range(len(L)):
			for j in range(len(st)-1,-1,-1):
				k = L[i][0]
				for l in range(L[i][1]):
					st.append(st[j]*k)
					k *= L[i][0]
		return st