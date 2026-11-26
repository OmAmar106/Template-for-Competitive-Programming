class PersistentSegmentTree:
	# Everything is 0 based indexing and [l,r]
	class Node:
		def __init__(self, value=0, left=None, right=None):
			self.value = value
			self.left = left
			self.right = right
	@staticmethod
	def func(a, b):
		return a+b
	def __init__(self, data):
		self.n = len(data)
		self.versions = []
		self.versions.append(self._build(data))
	def _build(self, data):
		stack = [(0, self.n - 1, False)]
		nodes = {}
		while stack:
			left, right, visited = stack.pop()
			if left == right:
				nodes[(left, right)] = self.Node(data[left])
			else:
				if visited:
					mid = (left + right) // 2
					left_child = nodes[(left, mid)]
					right_child = nodes[(mid + 1, right)]
					nodes[(left, right)] = self.Node(self.func(left_child.value,right_child.value),left_child, right_child)
				else:
					stack.append((left, right, True))
					mid = (left + right) // 2
					stack.append((mid + 1, right, False))
					stack.append((left, mid, False))
		return nodes[(0, self.n - 1)]
	def update(self, version, pos, value):
		# Returns the root to the new tree,
		# now you must add it to versions yourself
		# seg.versions[version] = seg.update(version, pos, value)
		old_root = self.versions[version]
		stack, path = [(old_root, 0, self.n - 1)], []
		while stack:
			node, left, right = stack.pop()
			path.append((node, left, right))
			if left == right:
				break
			mid = (left + right) // 2
			if pos <= mid:
				stack.append((node.left, left, mid))
			else:
				stack.append((node.right, mid + 1, right))
		new_nodes = {}
		for node, left, right in reversed(path):
			if left == right:
				k = value
				# k = self.func(node.value,value) # if i want to update
				new_nodes[(left, right)] = self.Node(k)
			else:
				mid = (left + right) // 2
				left_child = new_nodes.get((left, mid), node.left)
				right_child = new_nodes.get((mid + 1, right), node.right)
				new_nodes[(left, right)] = self.Node(self.func(left_child.value,right_child.value),left_child, right_child)
		return new_nodes[(0, self.n - 1)]
	def create_version(self, version, pos, value):
		new_root = self.update(version, pos, value)
		self.versions.append(new_root)
		return len(self.versions) - 1
	def query(self, version, ql, qr):
		node, left, right = self.versions[version], 0, self.n - 1
		stack = [(node, left, right)]
		result = 0 # change this depending on the problem
		while stack:
			node, left, right = stack.pop()
			if ql > right or qr < left:
				continue
			if ql <= left and right <= qr:
				result = self.func(result,node.value)
			else:
				mid = (left + right) // 2
				stack.append((node.left, left, mid))
				stack.append((node.right, mid + 1, right))
		return result

class PersistentSegTree:
	# slightly faster than the first one
	# everything is inclusive of [l,r]
	# everything is 0 indexed
	def __init__(self,a,op=lambda x,y:x+y, node_max=1<<23):
		self.n = len(a)
		self.op = op
		self.m = len(a)<<2
		self.root = [0]
		self.left = [0]*node_max
		self.right = [0]*node_max
		self.val = [0]*node_max
		self.build(0, a, 0, len(a) - 1)
	def build(self,i,a,l,r):
		if l==r:
			self.val[i] = a[l]
			return
		mid = (l+r)>>1
		self.left[i],self.right[i] = i<<1,i<<1|1
		self.build(i<<1,a,l,mid)
		self.build(i<<1|1,a,mid+1,r)
		self.val[i] = self.op(self.val[self.left[i]], self.val[self.right[i]])
	def new_node(self, old):
		self.m += 1
		self.left[self.m-1] = self.left[old]
		self.right[self.m-1] = self.right[old]
		self.val[self.m-1] = self.val[old]
		return self.m-1
	def update(self, old, x, v):
		# returns the id of the version
		# you can directly use it without having to update
		# versions like the previous implementation
		new = self.new_node(self.root[old])
		self.root.append(new)
		i,l,r = self.root[-1],0,self.n - 1
		stack = [(i,l,r,0)]
		while stack:
			i,l,r,col = stack.pop()
			if l==r:
				self.val[i] = v
				continue
			if col==0:
				stack.append((i,l,r,1))
				mid = (l+r)>>1
				if x<=mid:
					self.left[i] = self.new_node(self.left[i])
					stack.append((self.left[i],l,mid,0))
				else:
					self.right[i] = self.new_node(self.right[i])
					stack.append((self.right[i],mid+1,r,0))
			else:
				self.val[i] = self.op(self.val[self.left[i]],self.val[self.right[i]])
		return len(self.root)-1
	def query(self, t, L, R):
		res = 0
		stack = [(self.root[t], 0, self.n - 1)]
		while stack:
			i, l, r = stack.pop()
			if L <= l <= r <= R:
				res = self.op(res, self.val[i])
			elif not (L > r or R < l):
				mid = (l + r) >> 1
				stack.append((self.right[i], mid + 1, r))
				stack.append((self.left[i], l, mid))
		return res
