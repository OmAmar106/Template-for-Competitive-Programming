class Node():
	def __init__(self):
		self.data=0
		self.left=None
		self.right=None
		self.count=0
class Trie():
	def __init__(self,k=30):
		self.root=Node()
		self.k = k
	def add(self,val):
		self.temp=self.root
		for i in range(self.k,-1,-1):
			if (val)&(1<<i):
				if not self.temp.right:
					self.temp.right=Node()
				self.temp=self.temp.right
				self.temp.count+=1
			else:
				if not self.temp.left:
					self.temp.left=Node()
				self.temp=self.temp.left
				self.temp.count+=1
		self.temp.data=val
	def __delitem__(self,val):
		self.temp=self.root
		for i in range(self.k,-1,-1):
			if val&(1<<i):
				self.temp=self.temp.right
				self.temp.count-=1
			else:
				self.temp=self.temp.left
				self.temp.count-=1
	def query_max(self,val):
		self.temp=self.root
		for i in range(self.k,-1,-1):
			if val&(1<<i):
				if self.temp.left and self.temp.left.count>0:
					self.temp=self.temp.left
				elif self.temp.right and self.temp.right.count>0:
					self.temp=self.temp.right
			else:
				if self.temp.right and self.temp.right.count>0:
					self.temp=self.temp.right
				elif self.temp.left and self.temp.left.count>0:
					self.temp=self.temp.left
		return val^self.temp.data
	def query_min(self,val):
		self.temp=self.root
		for i in range(self.k,-1,-1):
			if val&(1<<i)==0:
				if self.temp.left and self.temp.left.count>0:
					self.temp=self.temp.left
				elif self.temp.right and self.temp.right.count>0:
					self.temp=self.temp.right
			else:
				if self.temp.right and self.temp.right.count>0:
					self.temp=self.temp.right
				elif self.temp.left and self.temp.left.count>0:
					self.temp=self.temp.left
		return val^self.temp.data