class Node:
	__slots__ = ("val", "priority", "left", "right", "size")
	def __init__(self, val):
		self.val = val
		self.priority = random.random()
		self.left = None
		self.right = None
		self.size = 1
class Treap:
	def __init__(self, iterable=None):
		self.root = None
		if iterable:
			for x in iterable:
				self.root = Treap._merge(self.root, Node(x))
	@staticmethod
	def _size(node):
		return node.size if node else 0
	@staticmethod
	def _update(node):
		if node:
			node.size = 1 + Treap._size(node.left) + Treap._size(node.right)
	@staticmethod
	def _merge(left, right):
		if not left or not right:
			return left or right

		if left.priority > right.priority:
			left.right = Treap._merge(left.right, right)
			Treap._update(left)
			return left
		else:
			right.left = Treap._merge(left, right.left)
			Treap._update(right)
			return right
	def _kth(node, k):
		if not node:
			return None

		left_size = Treap._size(node.left)

		if k < left_size:
			return Treap._kth(node.left, k)
		elif k == left_size:
			return node.val
		else:
			return Treap._kth(node.right, k - left_size - 1)
	def kth(self, k):
		if k < 0 or k >= Treap._size(self.root):
			return None
		return Treap._kth(self.root, k)
	@staticmethod
	def merge(t1, t2):
		t = Treap()
		t.root = Treap._merge(t1.root, t2.root)
		return t
	@staticmethod
	def _split(node, k):
		if not node:
			return (None, None)
		left_size = Treap._size(node.left)
		if k <= left_size:
			left, node.left = Treap._split(node.left, k)
			Treap._update(node)
			return (left, node)
		else:
			node.right, right = Treap._split(node.right, k - left_size - 1)
			Treap._update(node)
			return (node, right)
	def insert(self, pos, val):
		new_node = Node(val)
		left, right = Treap._split(self.root, pos)
		merged = Treap._merge(left, new_node)
		self.root = Treap._merge(merged, right)
	def split(self, k):
		left_root, right_root = Treap._split(self.root, k)
		t1 = Treap()
		t2 = Treap()
		t1.root = left_root
		t2.root = right_root
		return t1, t2
	def __iter__(self):
		stack = []
		node = self.root
		while stack or node:
			while node:
				stack.append(node)
				node = node.left

			node = stack.pop()
			yield node.val
			node = node.right
