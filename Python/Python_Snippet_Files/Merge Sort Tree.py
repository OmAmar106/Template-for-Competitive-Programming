class MergeSortTree:
	def merge(L,L1):
		L2 = []
		L = list(L);L1 = list(L1)
		i = j = 0
		while j<len(L) and i<len(L1):
			if L[j]<L1[i]:
				L2.append(L[j])
				j += 1
			else:
				L2.append(L1[i])
				i += 1
		L2.extend(L[j:]+L1[i:])
		return L2
	def __init__(self, data):
		self.n = len(data)
		self.tree = [SortedList() for _ in range(2 * self.n)]
		self.build(data)
	def build(self, data):
		for i in range(self.n):
			self.tree[self.n + i].insert(data[i])
		for i in range(self.n - 1, 0, -1):
			self.tree[i] = SortedList(MergeSortTree.merge(self.tree[i << 1],self.tree[i<<1|1]))
	def query(self, left, right,l,r):
		res = 0
		left += self.n
		right += self.n
		while left < right:
			if left & 1:
				res += self.func(self.tree[left], l, r);left += 1
			if right & 1:
				right -= 1;res += self.func(self.tree[right], l, r)
			left >>= 1;right >>= 1
		return res
	def func(self, L, l, r):
		return L.bisect_right(r)-L.bisect_left(l)
	def update(self,pos,value):
		pos += self.n;old_val = self.tree[pos][0]
		self.tree[pos].remove(old_val)
		self.tree[pos].add(value)
		while pos:
			pos >>= 1
			self.tree[pos].remove(old_val)
			self.tree[pos].add(value)