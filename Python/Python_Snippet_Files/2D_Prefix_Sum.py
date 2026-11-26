class Prefix2D:
	def __init__(self,mat):
		self.pref = [[0]*(len(mat[0])+1) for i in range(len(mat)+1)]
		for i in range(len(mat)):
			for j in range(len(mat[0])):
				self.pref[i+1][j+1] = self.pref[i][j+1]+self.pref[i+1][j]-self.pref[i][j]+mat[i][j]
	def query(self,x1,y1,x2,y2):
		# mat[x1:x2+1][y1:y2+1] -> inclusive
		# 0-indexed
		if x1>x2 or y1>y2:
			return 0
		return self.pref[x2+1][y2+1]-self.pref[x1][y2+1]-self.pref[x2+1][y1]+self.pref[x1][y1]
