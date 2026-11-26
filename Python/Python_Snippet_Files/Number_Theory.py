def miller_is_prime(n):
	# Miller-Rabin test - O(7 * log2n)
	# Has 100% success rate for numbers less than 3e+9
	# use it in case of TC problem
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
	# returns a sorted list of all distinct factors of n in root n
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

def prime_factors_slow(n):
	factors = []
	if n%2==0:
		factors.append(2)
		while n%2==0:
			n //= 2
	i = 3
	while i*i<=n:
		if n%i==0:
			factors.append(i)
			while n%i==0:
				n//=i
		i += 2
	if n>1:
		factors.append(n)
	return factors
