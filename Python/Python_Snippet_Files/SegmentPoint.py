class SegmentTree:
	"""
		Remember to change the func content as well as the initializer to display the content
	"""
	@staticmethod
	def func(a, b):
		# Change this function depending upon needs
		return max(a, b)
	def __init__(self, data):
		self.n = len(data)
		self.tree = [0] * (self.n<<1)
		self.build(data)
	def build(self, data):
		for i in range(self.n):
			self.tree[self.n + i] = data[i]
		for i in range(self.n - 1, 0, -1):
			self.tree[i] = self.func(self.tree[i<<1], self.tree[(i<<1) + 1])
	def update(self, pos, value):
		# Update the value at the leaf node
		pos += self.n
		# For updating
		self.tree[pos] = value
		# self.tree[pos] += value
		# If you want to add rather than update
		while pos > 1:
			pos >>= 1
			self.tree[pos] = self.func(self.tree[pos<<1], self.tree[(pos<<1) + 1])
	def query(self, left, right):
		# Query the maximum value in the range [left, right)
		left += self.n
		right += self.n
		# Change the initializer depending upon the self.func
		max_val = float('-inf')
		##
		while left < right:
			if left&1:
				max_val = self.func(max_val, self.tree[left])
				left += 1
			if right&1:
				right -= 1
				max_val = self.func(max_val, self.tree[right])
			left >>= 1
			right >>= 1
		return max_val
	def __repr__(self):
		values = [str(self.query(i, i + 1)) for i in range(self.n)]
		return f"Seg[{', '.join(values)}]"