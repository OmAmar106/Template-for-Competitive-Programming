class Xdict:
	def __init__(self,L=[],flag=1):
		self.d = {}
		self.flag = flag
		for j in L:self[j]+=1
	def __setitem__(self,key,value):
		self.d[w(key)] = value
	def __getitem__(self,key):
		return self.d.get(w(key),0) if self.flag else self.d[w(key)]
	def keys(self):
		return (w(i) for i in self.d)
	def values(self):
		return (self.d[i] for i in self.d)
	def items(self):
		return ((w(i),self.d[i]) for i in self.d)
	def __repr__(self):
		return '{'+','.join([str(w(i))+':'+str(self.d[i]) for i in self.d])+'}'
	def __delitem__(self,val):
		del self.d[w(val)]
	def get(self,key,other):
		return self.d.get(w(key),other)
	def __contains__(self,key):
		return w(key) in self.d
	def __len__(self):
		return len(self.d)
	def clear(self):
		self.d.clear()
	def __iter__(self):
		return iter(self.keys())

class Xset:
	def __init__(self,L=[]):
		self.s = set()
		for j in L:self.add(j)
	def add(self,key):
		self.s.add(w(key))
	def keys(self):
		return (w(i) for i in self.s)
	def __repr__(self):
		return '{'+','.join([str(w(i)) for i in self.s])+'}'
	def remove(self,val):
		self.s.remove(w(val))
	def __contains__(self,key):
		return w(key) in self.s
	def __len__(self):
		return len(self.s)
	def clear(self):
		self.s.clear()
	def __iter__(self):
		return iter(self.keys())