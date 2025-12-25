def fwht(a, invert=False):
	# In-place Fast Walsh–Hadamard Transform for XOR convolution.
	# invert: if True, computes inverse transform
	n = len(a);step = 1
	while step<n:
		for i in range(0,n,step*2):
			for j in range(step):
				a[i+j],a[i+j+step] = a[i+j]+a[i+j+step],a[i+j]-a[i+j+step]
		step *= 2
	if invert:
		for i in range(n):
			a[i] //= n

def fwt_or(a, invert=False):
	n = len(a);step = 1
	while step<n:
		for i in range(0,n,step*2):
			for j in range(step):
				u = a[i+j]
				v = a[i+j+step]
				if not invert:
					a[i+j+step] = u+v
				else:
					a[i+j+step] = v-u
		step *= 2

def fwt_and(a, invert=False):
	n = len(a);step = 1
	while step<n:
		for i in range(0,n,step*2):
			for j in range(step):
				u = a[i+j]
				v = a[i+j+step]
				if not invert:
					a[i+j] = u+v
				else:
					a[i+j] = u-v
		step *= 2

def convolution(A, B, fwt=fwht):
	# Computes XOR convolution of arrays A and B using FWHT
	# res[i] = summation of A[j]*B[k] such that j xor k = i
	n = 1;x = max(len(A),len(B))
	while n<x:n <<= 1
	n <<= 1
	fa = A + [0] * (n - len(A))
	fb = B + [0] * (n - len(B))
	fwt(fa)
	fwt(fb)
	for i in range(n):
		fa[i] *= fb[i]
	fwt(fa, invert=True)
	return fa