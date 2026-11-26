class LinkCutTree:
	class Node:
		__slots__=('l','r','p','rev','val','sm')
		def __init__(self,val=0):
			self.l=-1
			self.r=-1
			self.p=-1
			self.rev=False
			self.val=val
			self.sm=val
	def __init__(self,n):
		self.n=n
		self.t=[self.Node() for _ in range(n)]
	def _is_root(self,x):
		p=self.t[x].p
		return p==-1 or (self.t[p].l!=x and self.t[p].r!=x)
	def _push(self,x):
		if x==-1:
			return
		t=self.t[x]
		if t.rev:
			t.l,t.r=t.r,t.l
			if t.l!=-1:
				self.t[t.l].rev^=1
			if t.r!=-1:
				self.t[t.r].rev^=1
			t.rev=False
	def _pull(self,x):
		t=self.t[x]
		t.sm=t.val
		if t.l!=-1:
			t.sm+=self.t[t.l].sm
		if t.r!=-1:
			t.sm+=self.t[t.r].sm
	def _rotate(self,x):
		p=self.t[x].p
		g=self.t[p].p
		if self.t[p].l==x:
			b=self.t[x].r
			self.t[x].r=p
			self.t[p].l=b
			if b!=-1:
				self.t[b].p=p
		else:
			b=self.t[x].l
			self.t[x].l=p
			self.t[p].r=b
			if b!=-1:
				self.t[b].p=p
		self.t[p].p=x
		self.t[x].p=g
		if g!=-1:
			if self.t[g].l==p:
				self.t[g].l=x
			elif self.t[g].r==p:
				self.t[g].r=x
		self._pull(p)
		self._pull(x)
	def _splay(self,x):
		stk=[]
		y=x
		while True:
			stk.append(y)
			if self._is_root(y):
				break
			y=self.t[y].p
		while stk:
			self._push(stk.pop())
		while not self._is_root(x):
			p=self.t[x].p
			g=self.t[p].p
			if not self._is_root(p):
				if (self.t[g].l==p)==(self.t[p].l==x):
					self._rotate(p)
				else:
					self._rotate(x)
			self._rotate(x)
	def _access(self,x):
		last=-1
		while x!=-1:
			self._splay(x)
			self.t[x].r=last
			self._pull(x)
			last=x
			x=self.t[x].p
	def makeroot(self,x):
		self._access(x)
		self._splay(x)
		self.t[x].rev^=1
	def findroot(self,x):
		self._access(x)
		self._splay(x)
		while True:
			self._push(x)
			if self.t[x].l==-1:
				break
			x=self.t[x].l
		self._splay(x)
		return x
	def connected(self,u,v):
		return self.findroot(u)==self.findroot(v)
	def link(self,u,v):
		self.makeroot(u)
		if self.findroot(v)==u:
			return False
		self.t[u].p=v
		return True
	def cut(self,u,v):
		self.makeroot(u)
		self._access(v)
		self._splay(v)
		if self.t[v].l!=u or self.t[u].r!=-1:
			return False
		self.t[u].p=-1
		self.t[v].l=-1
		self._pull(v)
		return True
	def set_value(self,u,val):
		self._access(u)
		self._splay(u)
		self.t[u].val=val
		self._pull(u)
	def path_sum(self,u,v):
		self.makeroot(u)
		self._access(v)
		self._splay(v)
		return self.t[v].sm
