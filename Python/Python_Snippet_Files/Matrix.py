class Matrix:
	MOD = 10**9+7
	@staticmethod
	def transpose(mat):
		return [list(c) for c in zip(*mat)]
	def __init__(self,M):
		self.M=M
	def minmul(self,o):
		L,B=self.M,o.M
		r=len(L); c=len(B[0])
		return Matrix([[min(L[i][k]+B[k][j] for k in range(len(B)))%self.MOD for j in range(c)] for i in range(r)])
	def __matmul__(self,o):
		L,B=self.M,o.M
		r=len(L); c=len(B[0])
		return Matrix([[sum(L[i][k]*B[k][j] for k in range(len(B)))%self.MOD for j in range(c)] for i in range(r)])
	def __pow__(self,p):
		M=self; n=len(M.M)
		R=Matrix([[i==j for j in range(n)] for i in range(n)])
		while p:
			R = R@M if p&1 else R
			M = M@M
			p//=2
		return R
	@staticmethod
	def gauss(A,mod=10**9+7):
		m,n=len(A),len(A[0])-1; r=0; L=[-1]*n
		for c in range(n):
			for i in range(r,m):
				if A[i][c]: A[r],A[i]=A[i],A[r]
				break
			else:
				continue
			k=pow(A[r][c],-1,mod)
			for j in range(c,n+1):
				A[r][j]=A[r][j]*k%mod
			for i in range(m):
				if i!=r and A[i][c]:
					f=A[i][c]
					for j in range(c,n+1):
						A[i][j]=(A[i][j]-f*A[r][j])%mod
			L[c]=r
			r+=1
		if any(A[i][n] for i in range(r,m)):
			return None
		return [A[L[i]][n] if L[i]!=-1 else 0 for i in range(n)]
	def __str__(self):
		return '\n'.join(' '.join(map(str,row)) for row in self.M)
	def __repr__(self):
		return f"Matrix({self.M})"
	def __iter__(self):
		return iter(self.M)
