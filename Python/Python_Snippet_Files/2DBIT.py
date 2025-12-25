class BIT2D:
	def __init__(self, arr):
		self.n = len(arr)
		self.m = len(arr[0]) if self.n > 0 else 0
		# self.bit = [row[:] for row in arr]
		self.bit = arr # assuming that arr is not used after this
		for i in range(self.n):
			for j in range(self.m):
				ni = i | (i + 1)
				if ni < self.n:
					self.bit[ni][j] += self.bit[i][j]
		for i in range(self.n):
			for j in range(self.m):
				nj = j | (j + 1)
				if nj < self.m:
					self.bit[i][nj] += self.bit[i][j]
	def add(self, x, y, delta):
		# 0-based in log n * log m
		i = x
		while i < self.n:
			j = y
			while j < self.m:
				self.bit[i][j] += delta
				j |= j + 1
			i |= i + 1
	def sum(self, x, y):
		# sum from 0,0 to x,y inclusive in log n * log m
		if not (0<=x<self.n) or not (0<=y<self.m):
			return 0
		res = 0
		i = x
		while i >= 0:
			j = y
			while j >= 0:
				res += self.bit[i][j]
				j = (j & (j + 1)) - 1
			i = (i & (i + 1)) - 1
		return res
	def query(self, x1, y1, x2, y2):
		# sum of L[x1:x2+1][y1:y2+1]
		return (self.sum(x2,y2)-self.sum(x1-1,y2)-self.sum(x2,y1-1)+(self.sum(x1-1,y1-1)))