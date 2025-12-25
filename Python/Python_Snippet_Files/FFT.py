class FastFFT:
	# This is a bit faster, one log n factor is less but it's accuracy is not 100%
	# use this when coeffecient does not matter(set coeffecient to 1 repeatedly)
	# or you could just risk it :)
	def __init__(self, MOD=998244353):
		FastFFT.MOD = MOD
		# g = self.primitive_root_constexpr()
		g = 3
		ig = pow(g, FastFFT.MOD - 2, FastFFT.MOD)
		FastFFT.W = [pow(g, (FastFFT.MOD - 1) >> i, FastFFT.MOD) for i in range(30)]
		FastFFT.iW = [pow(ig, (FastFFT.MOD - 1) >> i, FastFFT.MOD) for i in range(30)]
	def primitive_root_constexpr(self):
		if FastFFT.MOD == 998244353:
			return 3
		elif FastFFT.MOD == 200003:
			return 2
		elif FastFFT.MOD == 167772161:
			return 3
		elif FastFFT.MOD == 469762049:
			return 3
		elif FastFFT.MOD == 754974721:
			return 11
		divs = [0] * 20
		divs[0] = 2
		cnt = 1
		x = (FastFFT.MOD - 1) // 2
		while x % 2 == 0:
			x //= 2
		i = 3
		while i * i <= x:
			if x % i == 0:
				divs[cnt] = i
				cnt += 1
				while x % i == 0:
					x //= i
			i += 2
		if x > 1:
			divs[cnt] = x
			cnt += 1
		g = 2
		while 1:
			ok = True
			for i in range(cnt):
				if pow(g, (FastFFT.MOD - 1) // divs[i], FastFFT.MOD) == 1:
					ok = False
					break
			if ok:
				return g
			g += 1
	def fft(self, k, f):
		for l in range(k, 0, -1):
			d = 1 << l - 1
			U = [1]
			for i in range(d):
				U.append(U[-1] * FastFFT.W[l] % FastFFT.MOD)
			for i in range(1 << k - l):
				for j in range(d):
					s = i * 2 * d + j
					f[s], f[s + d] = (f[s] + f[s + d]) % FastFFT.MOD, U[j] * (f[s] - f[s + d]) % FastFFT.MOD
	def ifft(self, k, f):
		for l in range(1, k + 1):
			d = 1 << l - 1
			for i in range(1 << k - l):
				u = 1
				for j in range(i * 2 * d, (i * 2 + 1) * d):
					f[j+d] *= u
					f[j], f[j + d] = (f[j] + f[j + d]) % FastFFT.MOD, (f[j] - f[j + d]) % FastFFT.MOD
					u = u * FastFFT.iW[l] % FastFFT.MOD
	def convolve(self, A, B):
		n0 = len(A) + len(B) - 1
		k = (n0).bit_length()
		n = 1 << k
		A += [0] * (n - len(A))
		B += [0] * (n - len(B))
		self.fft(k, A)
		self.fft(k, B)
		A = [a * b % FastFFT.MOD for a, b in zip(A, B)]
		self.ifft(k, A)
		inv = pow(n, FastFFT.MOD - 2, FastFFT.MOD)
		del A[n0:]
		for i in range(n0):
			A[i] = (A[i]*inv)%FastFFT.MOD
		return A

class FFT:
	def __init__(self, MOD=998244353,MOD1=469762049):
		FFT.MOD = MOD
		FFT.MOD1 = MOD1
		FFT.MOD2 = pow(MOD,MOD1-2,MOD1)
		FFT.mod_inv = (self.XT_GCD(MOD,MOD1)[1])%MOD1
		# g = self.primitive_root_constexpr()
		g = 3
		ig = pow(g, FFT.MOD - 2, FFT.MOD)
		ig1 = pow(g, FFT.MOD1 - 2, FFT.MOD1)
		FFT.W = [pow(g, (FFT.MOD - 1) >> i, FFT.MOD) for i in range(30)]
		FFT.W1 = [pow(g, (FFT.MOD1 - 1) >> i, FFT.MOD1) for i in range(30)]
		FFT.iW = [pow(ig, (FFT.MOD - 1) >> i, FFT.MOD) for i in range(30)]
		FFT.iW1 = [pow(ig1, (FFT.MOD1 - 1) >> i, FFT.MOD1) for i in range(30)]
	def primitive_root_constexpr(self):
		if FFT.MOD == 998244353:
			return 3
		elif FFT.MOD == 200003:
			return 2
		elif FFT.MOD == 167772161:
			return 3
		elif FFT.MOD == 469762049:
			return 3
		elif FFT.MOD == 754974721:
			return 11
		divs = [0] * 20
		divs[0] = 2
		cnt = 1
		x = (FFT.MOD - 1) // 2
		while x % 2 == 0:
			x //= 2
		i = 3
		while i * i <= x:
			if x % i == 0:
				divs[cnt] = i
				cnt += 1
				while x % i == 0:
					x //= i
			i += 2
		if x > 1:
			divs[cnt] = x
			cnt += 1
		g = 2
		while 1:
			ok = True
			for i in range(cnt):
				if pow(g, (FFT.MOD - 1) // divs[i], FFT.MOD) == 1:
					ok = False
					break
			if ok:
				return g
			g += 1
	def fft(self, k, f,f1):
		for l in range(k, 0, -1):
			d = 1 << l - 1
			U = [(1,1)]
			for i in range(d):
				U.append((U[-1][0] * FFT.W[l] % FFT.MOD,U[-1][1] * FFT.W1[l] % FFT.MOD1))
			for i in range(1 << k - l):
				for j in range(d):
					s = i * 2 * d + j
					f[s], f[s + d] = (f[s] + f[s + d]) % FFT.MOD, U[j][0] * (f[s] - f[s + d]) % FFT.MOD
					f1[s], f1[s + d] = (f1[s] + f1[s + d]) % FFT.MOD1, U[j][1] * (f1[s] - f1[s + d]) % FFT.MOD1
	def ifft(self, k, f,f1):
		for l in range(1, k + 1):
			d = 1 << l - 1
			for i in range(1 << k - l):
				u = 1
				u1 = 1
				for j in range(i * 2 * d, (i * 2 + 1) * d):
					f[j+d] *= u
					f[j], f[j + d] = (f[j] + f[j + d]) % FFT.MOD, (f[j] - f[j + d]) % FFT.MOD
					u = u * FFT.iW[l] % FFT.MOD
					f1[j+d] *= u1
					f1[j], f1[j + d] = (f1[j] + f1[j + d]) % FFT.MOD1, (f1[j] - f1[j + d]) % FFT.MOD1
					u1 = u1 * FFT.iW1[l] % FFT.MOD1
	def XT_GCD(self,a,b):
		if b == 0:
			return a,1,0
		g,x1,y1 = self.XT_GCD(b,a%b)
		x = y1
		y = x1-(a//b)*y1
		return g,x,y
	def CRT(self,a, mod1, b, mod2):
		k = (a+(b-a)*self.mod_inv%mod2*mod1)%(mod1*mod2)
		return k
	def convolve(self, A, B):
		n0 = len(A) + len(B) - 1
		k = (n0).bit_length()
		n = 1 << k
		A += [0] * (n - len(A))
		B += [0] * (n - len(B))
		A1 = A[:]
		B1 = B[:]
		self.fft(k, A,A1)
		self.fft(k, B,B1)
		A = [a * b % FFT.MOD for a, b in zip(A, B)]
		A1 = [a * b % FFT.MOD1 for a, b in zip(A1, B1)]
		self.ifft(k, A,A1)
		inv = pow(n, FFT.MOD - 2, FFT.MOD)
		inv1 = pow(n, FFT.MOD1 - 2, FFT.MOD1)
		del A[n0:]
		for i in range(n0):
			A[i] = self.CRT(A[i]*inv,FFT.MOD,A1[i]*inv1,FFT.MOD1)
		return A
