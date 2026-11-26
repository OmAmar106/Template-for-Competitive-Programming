class BWT:
	# Burrow's Wheeler Transform
	def bwt(s):
		# Returns last character of sorted
		# array of all rotations
		s += '#'
		n = len(s)
		rotations = [s[i:] + s[:i] for i in range(n)]
		rotations.sort()
		return ''.join(row[-1] for row in rotations)
	def inverse_bwt(bwt):
		# returns inverse of string formed by
		# bwt
		n = len(bwt)
		cnt = [0]*256
		for c in bwt:
			cnt[ord(c)] += 1
		start = [0]*256
		for i in range(1,256):
			start[i] = start[i-1]+cnt[i-1]
		occ = [0]*256
		nxt = [0]*n
		for i,c in enumerate(bwt):
			o = occ[ord(c)]
			nxt[i] = start[ord(c)] + o
			occ[ord(c)] += 1
		res = []
		idx = bwt.index('#')
		for _ in range(n):
			res.append(bwt[idx])
			idx = nxt[idx]
		return ''.join(res[::-1])
