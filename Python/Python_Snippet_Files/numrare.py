def memodict(f):
	class memodict(dict):
		def __missing__(self, key):
			ret = self[key] = f(key)
			return ret
	return memodict().__getitem__

def pollard_rho(n):
	# returns a random factor of n
	if n & 1 == 0:
		return 2
	if n % 3 == 0:
		return 3
	s = ((n - 1) & (1 - n)).bit_length() - 1
	d = n >> s
	for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
		p = pow(a, d, n)
		if p == 1 or p == n - 1 or a % n == 0:
			continue
		for _ in range(s):
			prev = p
			p = (p * p) % n
			if p == 1:
				return gcd(prev - 1, n)
			if p == n - 1:
				break
		else:
			for i in range(2, n):
				x, y = i, (i * i + 1) % n
				f = gcd(abs(x - y), n)
				while f == 1:
					x, y = (x * x + 1) % n, (y * y + 1) % n
					y = (y * y + 1) % n
					f = gcd(abs(x - y), n)
				if f != n:
					return f
	return n

@memodict
def prime_factors_large(n):
	# returns prime factor in n^(1/4) but is probablistic
	if n <= 1:
		return Counter()
	f = pollard_rho(n)
	return Counter([n]) if f == n else prime_factors_large(f) + prime_factors_large(n // f)

def extended_gcd(a, b):
	# returns gcd(a, b), s, r s.t. a * s + b * r == gcd(a, b)
	s, old_s = 0, 1
	r, old_r = b, a
	while r:
		q = old_r // r
		old_r, r = r, old_r - q * r
		old_s, s = s, old_s - q * s
	return old_r, old_s, (old_r - old_s * a) // b if b else 0

def composite_crt(b, m):
	# returns x s.t. x = b[i] (mod m[i]) for all i
	x, m_prod = 0, 1
	for bi, mi in zip(b, m):
		g, s, _ = extended_gcd(m_prod, mi)
		if ((bi - x) % mi) % g:
			return None
		x += m_prod * (s * ((bi - x) % mi) // g)
		m_prod = (m_prod * mi) // gcd(m_prod, mi)
	return x % m_prod

def phi(n):
	ph = [i if i & 1 else i // 2 for i in range(n + 1)]
	for i in range(3,n+1,2):
		if ph[i]==i:
			for j in range(i,n+1,i):
				ph[j] = (ph[j]//i)*(i-1)
	return ph