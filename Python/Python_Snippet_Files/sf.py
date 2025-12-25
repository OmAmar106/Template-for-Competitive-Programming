def SuffArr(st,flag=True):
	if flag:L = [ord(i) for i in st]
	else:L=st
	n = len(L)
	buckets = [0] * (max(L) + 2)
	for a in L:
		buckets[a + 1] += 1
	for b in range(1, len(buckets)):
		buckets[b] += buckets[b - 1]
	isL = [1] * n
	for i in reversed(range(n - 1)):
		isL[i] = +(L[i] > L[i + 1]) if L[i] != L[i + 1] else isL[i + 1]
	def induced_sort(LMS):
		SA = [-1] * (n)
		SA.append(n)
		endpoint = buckets[1:]
		for j in reversed(LMS):
			endpoint[L[j]] -= 1
			SA[endpoint[L[j]]] = j
		startpoint = buckets[:-1]
		for i in range(-1, n):
			j = SA[i] - 1
			if j >= 0 and isL[j]:
				SA[startpoint[L[j]]] = j
				startpoint[L[j]] += 1
		SA.pop()
		endpoint = buckets[1:]
		for i in reversed(range(n)):
			j = SA[i] - 1
			if j >= 0 and not isL[j]:
				endpoint[L[j]] -= 1
				SA[endpoint[L[j]]] = j
		return SA
	isLMS = [+(i and isL[i - 1] and not isL[i]) for i in range(n)]
	isLMS.append(1)
	LMS = [i for i in range(n) if isLMS[i]]
	if len(LMS) > 1:
		SA = induced_sort(LMS)
		LMS2 = [i for i in SA if isLMS[i]]
		prev = -1
		j = 0
		for i in LMS2:
			i1 = prev
			i2 = i
			while prev >= 0 and L[i1] == L[i2]:
				i1 += 1
				i2 += 1
				if isLMS[i1] or isLMS[i2]:
					j -= isLMS[i1] and isLMS[i2]
					break
			j += 1
			prev = i
			SA[i] = j
		LMS = [LMS[i] for i in SuffArr([SA[i] for i in LMS],False)]
	return induced_sort(LMS)

def LCPArray(L,SA=None):
	# Longest Common prefix in between S[i:] and S[i+1:]
	if not SA:
		SA = SuffArr(L)
	n = len(L)
	rank = [0] * n
	for i in range(n):
		rank[SA[i]] = i
	LCP = [0] * (n - 1)
	k = 0
	for i in range(n):
		l = rank[i]
		if l==n-1:
			k = 0
			continue
		j = SA[l+1]
		while i+k<n and L[i+k] == L[j+k]:
			k += 1
		LCP[l] = k
		k -= k > 0
	return LCP

def z_function(S):
	# return: the Z array, where Z[i] = length of the longest common prefix of S[i:] and S
	n = len(S)
	Z = [0] * n
	l = r = 0
	for i in range(1, n):
		z = Z[i - l]
		if i + z >= r:
			z = max(r - i, 0)
			while i + z < n and S[z] == S[i + z]:
				z += 1
			l, r = i, i + z
		Z[i] = z
	Z[0] = n
	return Z

def manacher(s):
	# returns longest palindrome in s
	t = '#' + '#'.join(s) + '#'
	n = len(t)
	L = [0] * n
	c = r = 0
	ml = 0
	mc = 0
	for i in range(n):
		mirror = 2*c-i
		if i<r:
			L[i] = min(r-i,L[mirror])
		a = i+L[i]+1
		b = i-L[i]-1
		while a<n and b>=0 and t[a]==t[b]:
			L[i] += 1
			a += 1
			b -= 1
		if i+L[i]>r:
			c = i
			r = i+L[i]
		if L[i]>ml:
			ml = L[i]
			mc = i
	start = (mc-ml)//2
	return s[start:start+ml]

def SuffArray(s):
	# Starting position of ith suffix
	# in lexographic order
	s += "$"
	n = len(s)
	k = 0
	rank = [ord(c) for c in s]
	tmp = [0] * n
	sa = list(range(n))
	def sort_key(i):
		return (rank[i], rank[i + (1 << k)] if i + (1 << k) < n else -1)
	while True:
		sa.sort(key=sort_key)
		tmp[sa[0]] = 0
		for i in range(1, n):
			tmp[sa[i]] = tmp[sa[i-1]] + (sort_key(sa[i-1]) != sort_key(sa[i]))
		rank, tmp = tmp, rank
		k += 1
		if (1 << k) >= n:
			break
	return sa