def bfsf(d,start=0):
	bfs = [start]
	visited = [False]*(len(d))
	visited[start] = True
	for u in bfs:
		for j in d[u]:
			if visited[j]:
				continue
			visited[j] = True
			bfs.append(j)
	return bfs

def dfs(d,start=0):
	# I can also use this to replicate recursion
	# without facing the overhead
	n = len(d)
	visited = [False]*n
	dp = [0]*n
	finished = [False]*n
	stack = [start]
	while stack:
		start = stack[-1]
		# stack.pop() # use this if there is nothing after returning
		if not visited[start]:
			visited[start] = True
			for child in d[start]:
				if not visited[child]:
					stack.append(child)
		else:
			stack.pop()
			dp[start] += 1
			for child in d[start]:
				if finished[child]:
					dp[start] += dp[child]
			finished[start] = True
			# remove else if you are doing nothing here
			# add the stuff that you do post traversel here
			# and add the finished array
	return dp

def dijkstra(d,start=0):
	n = len(d)
	dist = [float("inf")]*n
	# parents = [-1]*n
	dist[start] = 0
	queue = [(0, start)]
	while queue:
		path_len, v = heappop(queue)
		if path_len == dist[v]:
			for w, edge_len in d[v]:
				new_dist = edge_len+path_len
				if new_dist<dist[w]:
					dist[w] = new_dist
					# parents[w] = v
					heappush(queue, (new_dist, w))
	return dist