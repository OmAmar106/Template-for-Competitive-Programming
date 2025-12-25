from typing import Generic, Iterable, Iterator, List, Tuple, TypeVar, Optional
T = TypeVar('T')
class SortedList(Generic[T]):
	BUCKET_RATIO = 16
	SPLIT_RATIO = 24
	def __init__(self, a: Iterable[T] = []) -> None:
		a = list(a)
		n = self.size = len(a)
		if any(a[i] > a[i + 1] for i in range(n - 1)):
			a.sort()
		num_bucket = int(math.ceil(math.sqrt(n / self.BUCKET_RATIO)))
		self.a = [a[n * i // num_bucket : n * (i + 1) // num_bucket] for i in range(num_bucket)]
	def __iter__(self) -> Iterator[T]:
		for i in self.a:
			for j in i: yield j
	def __reversed__(self) -> Iterator[T]:
		for i in reversed(self.a):
			for j in reversed(i): yield j
	def __eq__(self, other) -> bool:return list(self) == list(other)
	def __len__(self) -> int:return self.size
	def __repr__(self) -> str:return "SortedMultiset" + str(self.a)
	def __str__(self) -> str:
		s = str(list(self))
		return "{" + s[1 : len(s) - 1] + "}"
	def _position(self, x: T) -> Tuple[List[T], int, int]:
		for i, a in enumerate(self.a):
			if x <= a[-1]: break
		return (a, i, bisect_left(a, x))
	def __contains__(self, x: T) -> bool:
		if self.size == 0: return False
		a, _, i = self._position(x)
		return i != len(a) and a[i] == x
	def count(self, x: T) -> int:return self.index_right(x) - self.index(x)
	def add(self,x):return self.insert(x)
	def insert(self, x: T) -> None:
		if self.size == 0:
			self.a = [[x]]
			self.size = 1
			return
		a, b, i = self._position(x)
		a.insert(i, x)
		self.size += 1
		if len(a) > len(self.a) * self.SPLIT_RATIO:
			mid = len(a) >> 1
			self.a[b:b+1] = [a[:mid], a[mid:]]
	def _pop(self, a: List[T], b: int, i: int) -> T:
		ans = a.pop(i)
		self.size -= 1
		if not a: del self.a[b]
		return ans
	def remove(self, x: T) -> bool:
		if self.size == 0: return False
		a, b, i = self._position(x)
		if i == len(a) or a[i] != x: return False
		self._pop(a, b, i)
		return True
	def lt(self, x: T) -> Optional[T]:
		for a in reversed(self.a):
			if a[0] < x:
				return a[bisect_left(a, x) - 1]
	def le(self, x: T) -> Optional[T]:
		for a in reversed(self.a):
			if a[0] <= x:
				return a[bisect_right(a, x) - 1]
	def gt(self, x: T) -> Optional[T]:
		for a in self.a:
			if a[-1] > x:
				return a[bisect_right(a, x)]
	def ge(self, x: T) -> Optional[T]:
		for a in self.a:
			if a[-1] >= x:
				return a[bisect_left(a, x)]
	def __getitem__(self, i: int) -> T:
		if i < 0:
			for a in reversed(self.a):
				i += len(a)
				if i >= 0: return a[i]
		else:
			for a in self.a:
				if i < len(a): return a[i]
				i -= len(a)
		raise IndexError
	def pop(self, i: int = -1) -> T:
		if i < 0:
			for b, a in enumerate(reversed(self.a)):
				i += len(a)
				if i >= 0: return self._pop(a, ~b, i)
		else:
			for b, a in enumerate(self.a):
				if i < len(a): return self._pop(a, b, i)
				i -= len(a)
		raise IndexError
	def bisect_left(self,x):return self.index(x)
	def index(self, x: T) -> int:
		ans = 0
		for a in self.a:
			if a[-1] >= x:
				return ans + bisect_left(a, x)
			ans += len(a)
		return ans
	def bisect_right(self,x):return self.index_right(x)
	def index_right(self, x: T) -> int:
		ans = 0
		for a in self.a:
			if a[-1] > x:
				return ans + bisect_right(a, x)
			ans += len(a)
		return ans
	def find_closest(self, k: T) -> Optional[T]:
		if self.size == 0:return None
		ltk = self.le(k);gtk = self.ge(k)
		if ltk is None:return gtk
		if gtk is None:return ltk
		return ltk if abs(k-ltk)<=abs(k-gtk) else gtk