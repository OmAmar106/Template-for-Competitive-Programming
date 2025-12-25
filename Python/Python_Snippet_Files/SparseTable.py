class SparseTable:
	@staticmethod
	def func(a,b):
		# func(a,a) should be a
		return gcd(a,b)
	def __init__(self, arr):
		self.n = len(arr)
		self.table = [[0 for i in range(int((math.log(self.n, 2)+1)))] for j in range(self.n)]
		self.build(arr)
	def build(self, arr):
		for i in range(0, self.n):
			self.table[i][0] = arr[i]
		j = 1
		while (1 << j) <= self.n:
			i = 0
			while i <= self.n - (1 << j):
				self.table[i][j] = self.func(self.table[i][j - 1], self.table[i + (1 << (j - 1))][j - 1])
				i += 1
			j += 1
	def query(self, L, R):
		# query from [L,R]
		j = int(math.log2(R - L + 1))
		return self.func(self.table[L][j], self.table[R - (1 << j) + 1][j])