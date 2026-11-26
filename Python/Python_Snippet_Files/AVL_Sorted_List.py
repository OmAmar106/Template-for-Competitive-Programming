from typing import Generic, Iterable, Iterator, TypeVar, Optional
T = TypeVar('T')
class Node(Generic[T]):
	__slots__ = ('key', 'cnt', 'size', 'height', 'left', 'right')
	def __init__(self, key):
		self.key = key
		self.cnt = 1
		self.size = 1
		self.height = 1
		self.left = None
		self.right = None
class SortedList(Generic[T]):
	def __init__(self, a: Iterable[T] = ()) -> None:
		self.root = None
		self.size = 0
		for x in a:
			self.add(x)
	def _h(self, p):
		return p.height if p else 0
	def _s(self, p):
		return p.size if p else 0
	def _pull(self, p):
		p.height = 1 + max(self._h(p.left), self._h(p.right))
		p.size = p.cnt + self._s(p.left) + self._s(p.right)
	def _rotate_right(self, p):
		q = p.left
		p.left = q.right
		q.right = p
		self._pull(p)
		self._pull(q)
		return q
	def _rotate_left(self, p):
		q = p.right
		p.right = q.left
		q.left = p
		self._pull(p)
		self._pull(q)
		return q
	def _balance(self, p):
		if not p:
			return None
		self._pull(p)
		b = self._h(p.left) - self._h(p.right)
		if b > 1:
			if self._h(p.left.left) < self._h(p.left.right):
				p.left = self._rotate_left(p.left)
			return self._rotate_right(p)
		if b < -1:
			if self._h(p.right.right) < self._h(p.right.left):
				p.right = self._rotate_right(p.right)
			return self._rotate_left(p)
		return p
	def _insert(self, p, x):
		if not p:
			return Node(x)
		if x == p.key:
			p.cnt += 1
			self._pull(p)
			return p
		if x < p.key:
			p.left = self._insert(p.left, x)
		else:
			p.right = self._insert(p.right, x)
		return self._balance(p)
	def add(self, x):
		self.insert(x)
	def insert(self, x: T) -> None:
		self.root = self._insert(self.root, x)
		self.size += 1
	def _remove_min(self, p):
		if not p.left:
			return p.right, p.key, p.cnt
		p.left, key, cnt = self._remove_min(p.left)
		return self._balance(p), key, cnt
	def _remove_root(self, p):
		if not p.left:
			return p.right
		if not p.right:
			return p.left
		p.right, key, cnt = self._remove_min(p.right)
		p.key = key
		p.cnt = cnt
		return self._balance(p)
	def _erase(self, p, x):
		if not p:
			return None, False
		if x < p.key:
			p.left, found = self._erase(p.left, x)
		elif x > p.key:
			p.right, found = self._erase(p.right, x)
		else:
			if p.cnt > 1:
				p.cnt -= 1
				return self._balance(p), True
			return self._remove_root(p), True
		if not found:
			return p, False
		return self._balance(p), True
	def remove(self, x: T) -> bool:
		self.root, found = self._erase(self.root, x)
		if found:
			self.size -= 1
		return found
	def _rank(self, x, inclusive=False):
		p = self.root
		ans = 0
		while p:
			if x < p.key or (not inclusive and x == p.key):
				p = p.left
			else:
				ans += self._s(p.left) + p.cnt
				if x == p.key:
					return ans
				p = p.right
		return ans
	def bisect_left(self, x):
		return self._rank(x)
	def bisect_right(self, x):
		return self._rank(x, True)
	def index(self, x):
		return self.bisect_left(x)
	def index_right(self, x):
		return self.bisect_right(x)
	def count(self, x):
		return self.bisect_right(x) - self.bisect_left(x)
	def __contains__(self, x):
		return self.count(x) > 0
	def _kth(self, k):
		if k < 0 or k >= self.size:
			raise IndexError
		p = self.root
		while p:
			left = self._s(p.left)
			if k < left:
				p = p.left
			elif k < left + p.cnt:
				return p.key
			else:
				k -= left + p.cnt
				p = p.right
		raise IndexError
	def __getitem__(self, k):
		if k < 0:
			k += self.size
		return self._kth(k)
	def _pop_kth(self, p, k):
		left = self._s(p.left)
		if k < left:
			p.left, ans = self._pop_kth(p.left, k)
		elif k < left + p.cnt:
			ans = p.key
			if p.cnt > 1:
				p.cnt -= 1
				return self._balance(p), ans
			return self._remove_root(p), ans
		else:
			p.right, ans = self._pop_kth(p.right, k - left - p.cnt)
		return self._balance(p), ans
	def pop(self, i=-1):
		if i < 0:
			i += self.size
		if i < 0 or i >= self.size:
			raise IndexError
		self.root, ans = self._pop_kth(self.root, i)
		self.size -= 1
		return ans
	def lt(self, x) -> Optional[T]:
		p = self.root
		ans = None
		while p:
			if p.key < x:
				ans = p.key
				p = p.right
			else:
				p = p.left
		return ans
	def le(self, x) -> Optional[T]:
		p = self.root
		ans = None
		while p:
			if p.key <= x:
				ans = p.key
				p = p.right
			else:
				p = p.left
		return ans
	def gt(self, x) -> Optional[T]:
		p = self.root
		ans = None
		while p:
			if p.key > x:
				ans = p.key
				p = p.left
			else:
				p = p.right
		return ans
	def ge(self, x) -> Optional[T]:
		p = self.root
		ans = None
		while p:
			if p.key >= x:
				ans = p.key
				p = p.left
			else:
				p = p.right
		return ans
	def find_closest(self, k) -> Optional[T]:
		if not self.size:
			return None
		a = self.le(k)
		b = self.ge(k)
		if a is None:
			return b
		if b is None:
			return a
		return a if abs(k - a) <= abs(k - b) else b
	def __len__(self):
		return self.size
	def __iter__(self) -> Iterator[T]:
		stack = []
		p = self.root
		while stack or p:
			while p:
				stack.append(p)
				p = p.left
			p = stack.pop()
			for _ in range(p.cnt):
				yield p.key
			p = p.right
	def __reversed__(self):
		stack = []
		p = self.root
		while stack or p:
			while p:
				stack.append(p)
				p = p.right
			p = stack.pop()
			for _ in range(p.cnt):
				yield p.key
			p = p.left
	def __eq__(self, other):
		return list(self) == list(other)
	def __repr__(self):
		return "SortedMultiset" + str(list(self))
	def __str__(self):
		return "{" + ", ".join(map(str, self)) + "}"
