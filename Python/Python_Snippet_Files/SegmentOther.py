class SegmentTree:
	@staticmethod
	def func(a, b):
		return a+b
	def __init__(self, data, default=0, mode='s'):
		self.mode = mode
		self._default = default
		self.n = len(data)
		self.size = 1 << (self.n - 1).bit_length()
		self.tree = [default] * (2 * self.size)
		self._size = [0] * (2 * self.size)
		self._size[self.size:] = [1] * self.size
		for i in range(self.size - 1, 0, -1):
			self._size[i] = self._size[i << 1] + self._size[i << 1 | 1]
		self.lazy_add = 0 if self.mode == 's' else 0
		self.lazy_set = None
		self.lazy_add = [0] * self.size
		self.lazy_set = [None] * self.size
		for i in range(self.n):
			self.tree[self.size + i] = data[i]
		for i in range(self.size - 1, 0, -1):
			self.tree[i] = self.func(self.tree[i << 1], self.tree[i << 1 | 1])
	def _apply_set(self, pos, value):
		if self.mode == 's':
			self.tree[pos] = value * self._size[pos]
		else:
			self.tree[pos] = value
		if pos < self.size:
			self.lazy_set[pos] = value
			self.lazy_add[pos] = 0
	def _apply_add(self, pos, value):
		if self.mode == 's':
			self.tree[pos] += value * self._size[pos]
		else:
			self.tree[pos] += value
		if pos < self.size:
			if self.lazy_set[pos] is not None:
				self.lazy_set[pos] += value
			else:
				self.lazy_add[pos] += value
	def _build(self, pos):
		while pos > 1:
			pos >>= 1
			self.tree[pos] = self.func(self.tree[pos << 1], self.tree[pos << 1 | 1])
			if self.lazy_set[pos] is not None:
				if self.mode == 's':
					self.tree[pos] = self.lazy_set[pos] * self._size[pos]
				else:
					self.tree[pos] = self.lazy_set[pos]
			if self.lazy_add[pos] != 0:
				if self.mode == 's':
					self.tree[pos] += self.lazy_add[pos] * self._size[pos]
				else:
					self.tree[pos] += self.lazy_add[pos]
	def _push(self, pos):
		for shift in range(self.size.bit_length() - 1, 0, -1):
			i = pos >> shift
			set_val = self.lazy_set[i]
			if set_val is not None:
				self._apply_set(i << 1, set_val)
				self._apply_set(i << 1 | 1, set_val)
				self.lazy_set[i] = None
			add_val = self.lazy_add[i]
			if add_val != 0:
				self._apply_add(i << 1, add_val)
				self._apply_add(i << 1 | 1, add_val)
				self.lazy_add[i] = 0
	def range_update(self, left, right, value,flag=True):
		# Range Update in [L,R] if flag, then add
		if flag:
			l = left + self.size
			r = right + self.size
			l0, r0 = l, r
			self._push(l0)
			self._push(r0)
			while l <= r:
				if l & 1: self._apply_add(l, value); l += 1
				if not r & 1: self._apply_add(r, value); r -= 1
				l >>= 1; r >>= 1
			self._build(l0)
			self._build(r0)
		else:
			l = left + self.size
			r = right + self.size
			l0, r0 = l, r
			self._push(l0)
			self._push(r0)
			while l <= r:
				if l & 1: self._apply_set(l, value); l += 1
				if not r & 1: self._apply_set(r, value); r -= 1
				l >>= 1; r >>= 1
			self._build(l0)
			self._build(r0)
	def range_query(self, left, right):
		# Range Query in [L,R]
		l = left + self.size
		r = right + self.size
		self._push(l)
		self._push(r)
		res = self._default
		while l <= r:
			if l & 1: res = self.func(res, self.tree[l]); l += 1
			if not r & 1: res = self.func(res, self.tree[r]); r -= 1
			l >>= 1; r >>= 1
		return res
	def __repr__(self):
		return f"SegmentTree({[self.range_query(i,i) for i in range(self.n)]})"