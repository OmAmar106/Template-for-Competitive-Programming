def Knuths(n,C = lambda x: x):
	# conditions
	# For all a<=b<=c<=d:
	#	 cost(a,c)+cost(b,d)<=cost(a,d)+cost(b,c)
	# opt[l][r-1] <= opt[l][r] <= opt[l+1][r]
	dp = [[0]*n for _ in range(n)]
	opt = [[0]*n for _ in range(n)]
	for i in range(n):
		dp[i][i] = 0
		opt[i][i] = i
	for i in range(n-2,-1,-1):
		for j in range(i+1,n):
			cost = C(i, j)
			mini = float('inf')
			L = opt[i][j-1]
			R = min(j-1, opt[i+1][j])
			for k in range(L, R+1):
				val = dp[i][k] + dp[k+1][j] + cost
				if val<=mini:
					mini = val
					opt[i][j] = k
			dp[i][j] = mini
	return dp[0][n-1]

def DnC(prev, dp, cost):
	# conditions
	# opt[i][j] <= opt[i][j+1]

	# for i in range(1, K + 1):
	#	 DnC(dp_prev, dp_cur, cost, n)
	#	 dp_prev, dp_cur = dp_cur, dp_prev
	def solve(l, r, opt_l, opt_r):
		if l > r:
			return

		mid = (l + r) // 2
		best_k = -1
		best_val = float('inf')
		end = max(0,min(mid - 1, opt_r))
		for k in range(opt_l, end + 1):
			val = prev[k] + cost(k, mid)
			if val < best_val:
				best_val = val
				best_k = k
		dp[mid] = best_val
		solve(l, mid - 1, opt_l, best_k)
		solve(mid + 1, r, best_k, opt_r)
	solve(0,len(dp)-1,0,len(dp)-1)
