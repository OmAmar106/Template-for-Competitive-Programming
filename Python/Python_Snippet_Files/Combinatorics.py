def derangements(n):
	# Number of permutations of n objects where no object appears in its original position
	return int(math.factorial(n)/math.e+0.5)

def precompute_stirling_1(n,MOD):
	# number of permutations of first n elements that has exactly k cycles
	dp = [[0]*(n+1) for _ in range(n+1)]
	dp[0][0] = 1
	for i in range(1,n+1):
		for j in range(1,i+1):
			dp[i][j] = (dp[i-1][j-1]+(i-1)*dp[i-1][j])%MOD
	return dp

def precompute_stirling_2(n,MOD=MOD):
	# stirling[n][k] = No of ways to partition n elements into k non-empty subsets
	stirling = [[0]*(n+1) for i in range(n+1)]
	stirling[0][0] = 1
	for i in range(1,n+1):
		for j in range(1,i+1):
			stirling[i][j] = (j*stirling[i-1][j]+stirling[i-1][j-1])%MOD
	return stirling

def partition(n,k):
	# Ways to partition n into k or fewer parts of size 1 or greater
	# add dp[(n,k)] and memoize it if using it.
	if n<0 or (k<1 and n>0):return 0
	if n==0:return 1
	return 1 if n==1 else partition(n,k-1)+partition(n-k,k)

def eularian_number(n):
	# eularian number (n,k) ->
	# permutation of length n with k ascents or k descents or k excedances
	# ascents -> p[i]<p[i+1]
	# descents -> p[i]>p[i+1]
	# excedances -> p[i]>i
	A = [[0]*(n+1) for i in range(n+1)]
	A[0][0] = 1

	for i in range(1,n+1):
		for j in range(i):
			A[i][j] = ((j+1)*A[i-1][j]+(i-j)*A[i-1][j-1])%MOD
	return A

def eularian(n):
	# eularian number (n,k) ->
	# permutation of length n with k ascents or k descents or k excedances
	# ascents -> p[i]<p[i+1]
	# descents -> p[i]>p[i+1]
	# excedances -> p[i]>i
	A = [[0]*(n+1) for i in range(n+1)]
	A[0][0] = 1
	for i in range(1,n+1):
		for j in range(i):
			A[i][j] = ((j+1)*A[i-1][j]+(i-j)*A[i-1][j-1])%MOD
	return A

class Factorial:
	def __init__(self, N, mod):
		assert(N<mod)
		N += 1
		self.mod = mod
		self.f = [1 for _ in range(N)]
		self.g = [1 for _ in range(N)]
		for i in range(1, N):
			self.f[i] = self.f[i - 1] * i % self.mod
		self.g[-1] = pow(self.f[-1], mod - 2, mod)
		for i in range(N - 2, -1, -1):
			self.g[i] = self.g[i + 1] * (i + 1) % self.mod
	def precompute_bell(self,n):
		# number of ways to divide n distinct
		# elements into non empty sets
		# bell[n] = (sum of stirling[n][j])
		bell = [0]*(n+1)
		bell[0] = bell[1] = 1
		for i in range(2,n+1):
			for j in range(i):
				bell[i] += self.combi(i-1,j)*bell[j]
			bell[i] %= MOD
		return bell
	def eulerian_number(self,n,k):
		if k<0 or k>=n:
			return 0
		ans = 0
		for j in range(k+2):
			term = Lfac.combi(n+1,j)*pow(k+1-j,n,self.mod)
			ans += (-1 if j&1 else 1)*term
		return ans % self.mod
	def der(self, n):
		if n==0: return 1
		if n==1: return 0
		a, b = 1, 0  # der(0), der(1)
		for i in range(2,n+1):
			a,b = b,((i-1)*(a+b)) % self.mod
		return b
	def stirling_2_mod(self,n,k):
		# Number of ways to partition n elements into k non-empty subsets
		return (sum(((-1)**(k - j))*self.combi(k, j)*pow(j,n,self.mod) for j in range(k + 1)) * self.fac_inv(k))%self.mod
	def lucas_nCk(self,n,k):
		# Lucas's theorem for finding ((nCk)%p) for large n,k
		# in log p(n)
		ans = 1
		p = self.mod
		while n or k:
			x = n%p
			y = k%p
			ans *= self.combi(x,y)
			ans %= p
			n //= p
			k //= p
		return ans
	def catalan(self,n):
		return (self.combi(2*n,n)-self.combi(2*n,n-1))%self.mod
	def fac(self, n):
		return self.f[n]
	def fac_inv(self, n):
		return self.g[n]
	def combi(self, n, m):
		if m == 0: return 1
		if n < m or m < 0 or n < 0: return 0
		return self.f[n] * self.g[m] % self.mod * self.g[n - m] % self.mod
	def permu(self, n, m):
		if n < m or m < 0 or n < 0: return 0
		return self.f[n] * self.g[n - m] % self.mod
	def inv(self, n):
		return self.f[n-1] * self.g[n] % self.mod
	def beggar(self,n,sumi):
		# number of ways n elements >=0 have sum sumi
		if n==0:return int(sumi==0)
		if sumi<0:return 0
		return self.combi(n+sumi-1,sumi)

Lfac = Factorial(200001,MOD)
