from typing import Callable, TypeVar, Generic, List
T = TypeVar('T')
class MonoStack(Generic[T]):
	def __init__(self, op: Callable[[T, T], T], e: Callable[[], T]):
		self.s: List[T] = []
		self.sMono: List[T] = []
		self.op = op
		self.e = e
	def push(self, x: T):
		self.s.append(x)
		if not self.sMono:
			self.sMono.append(x)
		else:
			self.sMono.append(self.op(self.sMono[-1], x))
	def pop(self) -> T:
		if not self.s:
			return self.e()
		self.sMono.pop()
		return self.s.pop()
	def get(self) -> T:
		return self.sMono[-1] if self.sMono else self.e()
	def empty(self) -> bool:
		return not self.s

class MonoDeque(Generic[T]):
	def __init__(self, op: Callable[[T, T], T] = lambda a,b: max(a,b), e: Callable[[], T] = lambda : -float('inf')):
		# e is the unit value in form of lambda : 0
		# The Function op must be associative, f(a,b)==f(b,a)
		self.op = op
		self.e = e
		self.front = MonoStack(op, e)
		self.back = MonoStack(op, e)
	def push_back(self, x: T):
		self.back.push(x)
	def pop_front(self):
		if self.front.empty():
			while not self.back.empty():
				self.front.push(self.back.pop())
		self.front.pop()
	def get(self) -> T:
		# returns the function op of the elements present in the deque
		return self.op(self.front.get(), self.back.get())