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
	# When the numbers are large this is the best method to get
	# unique prime factors, precompute n log log n , then each query is log n
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
