class SqrtDecomposition:
	def __init__(self, arr, func= sum, default: int = 0):
		self.n = len(arr)
		self.a = list(arr)
		self.func = func
		self.default = default
		self.block_size = int(math.sqrt(self.n)) + 1
		self.blocks = [self.default] * self.block_size

		for i in range(self.n):
			self.blocks[i // self.block_size] = self.func([self.blocks[i//self.block_size],self.a[i]])
	def query(self, l: int, r: int) -> int:
		# from [L,R]
		res = self.default
		i = l
		while i <= r:
			if i % self.block_size == 0 and i + self.block_size - 1 <= r:
				res = self.func([res, self.blocks[i // self.block_size]])
				i += self.block_size
			else:
				res = self.func([res, self.a[i]])
				i += 1
		return res
	def update(self, index: int, value: int):
		block = index // self.block_size
		self.a[index] = value
		start = block * self.block_size
		end = min(self.n, (block + 1) * self.block_size)
		self.blocks[block] = self.default
		for i in range(start, end):
			self.blocks[block] = self.func([self.blocks[block], self.a[i]])