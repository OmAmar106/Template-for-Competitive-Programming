class SegmentTree:
	def func(self,a,b):
		return max(a,b)
	def __init__(self, arr):
		self.n = len(arr)
		self.seg = [0] * (4 * self.n)
		self.lazy = [0] * (4 * self.n)
		self.build(1, 0, self.n - 1, arr)
	def build(self, idx, l, r, arr):
		if l == r:
			self.seg[idx] = arr[l]
			return
		mid = (l + r) // 2
		self.build(2*idx, l, mid, arr)
		self.build(2*idx+1, mid+1, r, arr)
		self.seg[idx] = self.func(self.seg[2*idx], self.seg[2*idx+1])
	def push(self, idx, l, r):
		if self.lazy[idx] != 0:
			self.seg[idx] += self.lazy[idx]
			if l != r:
				self.lazy[2*idx] += self.lazy[idx]
				self.lazy[2*idx+1] += self.lazy[idx]
			self.lazy[idx] = 0
	def update(self, idx, l, r, ql, qr, val):
		# [l,r]
		self.push(idx, l, r)
		if r < ql or l > qr:
			return
		if ql <= l and r <= qr:
			self.lazy[idx] += val
			self.push(idx, l, r)
			return
		mid = (l + r) // 2
		self.update(2*idx, l, mid, ql, qr, val)
		self.update(2*idx+1, mid+1, r, ql, qr, val)
		self.seg[idx] = self.func(self.seg[2*idx],self.seg[2*idx+1])
	def query(self, idx, l, r, ql, qr):
		# [l,r]
		self.push(idx, l, r)
		if r < ql or l > qr:
			return -10**18
		if ql <= l and r <= qr:
			return self.seg[idx]
		mid = (l + r)>>1
		return self.func(self.query(2*idx, l, mid, ql, qr),self.query(2*idx+1, mid+1, r, ql, qr))
