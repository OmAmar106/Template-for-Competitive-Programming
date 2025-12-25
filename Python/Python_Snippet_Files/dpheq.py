class DiophantineEquations:
	"""
		used for solving equations of the form a*x + b*y = c,
		solnll takes the lower limit as well
	"""
	def __init__(self):
		pass
	def euclidean_gcd(self,a, b):
		"""
			euclidean gcd , returns x and y such that
			a*x + b*y = gcd(a,b)
		"""
		if b == 0:
			return a,1,0
		g,x1,y1 = self.euclidean_gcd(b, a % b)
		x = y1
		y = x1-(a//b)*y1
		return g,x,y
	def soln(self,a,b,c,t=10**18,t1=10**18):
		"""
			return m and n such that a*m + b*n = c and 0<=m<=t and 0<=n<=t1
			don't input t,t1 for any possible value
		"""
		g = gcd(a, b)
		if c%g!=0:
			return -1,-1
		_, x, y = self.euclidean_gcd(a, b)
		k3 = x*(c//g)
		n1 = y*(c//g)
		k1 = max(math.ceil(-k3*g/b),math.ceil((n1-t1)/(a/g)))
		kmaxi = min(math.floor((t-k3)/(b/g)), math.floor(n1/(a/g)))
		if k1<=kmaxi:
			k = k1
			m = k3+k*(b//g)
			n = n1-k*(a//g)
			return m, n
		else:
			return -1,-1
	def sollnll(self,a,b,c,t,t1,m_lower,n_lower):
		"""
			return m and n such that a*m + b*n = c and
			m_lower <= m <= t and n_lower <= n <= t1
		"""
		g = gcd(a, b)
		if c % g != 0:
			return -1, -1
		_, x, y = self.euclidean_gcd(a, b)
		k3 = x * (c // g)
		n1 = y * (c // g)
		k1 = max(math.ceil((m_lower - k3 * g) / b), math.ceil((n1 - t1) / (a / g)))
		kmaxi = min(math.floor((t - k3) / (b / g)), math.floor((n1 - n_lower) / (a / g)))
		if k1 <= kmaxi:
			k = k1
			m = k3 + k * (b // g)
			n = n1 - k * (a // g)
			if m_lower <= m <= t and n_lower <= n <= t1:
				return m, n
			else:
				return -1,-1
		else:
			return -1, -1
Leq = DiophantineEquations()