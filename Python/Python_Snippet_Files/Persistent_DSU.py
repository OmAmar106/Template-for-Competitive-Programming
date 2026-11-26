class Node:
	def __init__(self,left=None,right=None,parent=0,size=1):
		self.left = left
		self.right = right
		self.parent = parent
		self.size = size
class PersistentDSU:
	def __init__(self,n):
		self.n = n
		self.versions = [self._build(0,n)]
	def _build(self,l,r):
		if r-l==1:
			return Node(parent=l,size=1)
		mid=(l+r)//2
		return Node(self._build(l,mid),self._build(mid,r))
	def _get(self,node,l,r,idx):
		if r-l==1:
			return node.parent,node.size
		mid=(l+r)//2
		if idx<mid:
			return self._get(node.left,l,mid,idx)
		return self._get(node.right,mid,r,idx)
	def _update(self,node,l,r,idx,parent=None,size=None):
		if r-l==1:
			return Node(parent if parent is not None else node.parent,size if size is not None else node.size)
		mid=(l+r)//2
		if idx<mid:
			return Node(self._update(node.left,l,mid,idx,parent,size),node.right)
		return Node(node.left,self._update(node.right,mid,r,idx,parent,size))
	def find(self,root,node):
		parent,_ = self._get(root,0,self.n,node)
		return node if parent==node else self.find(root,parent)
	def union(self,version,u,v):
		root=self.versions[version]
		u=self.find(root,u)
		v=self.find(root,v)
		if u==v:
			self.versions.append(root)
			return len(self.versions)-1
		_,size_u=self._get(root,0,self.n,u)
		_,size_v=self._get(root,0,self.n,v)
		if size_u>size_v:
			u,v=v,u
		root=self._update(root,0,self.n,u,parent=v)
		root=self._update(root,0,self.n,v,size=size_u+size_v)
		self.versions.append(root)
		return len(self.versions)-1
