n = len(gr)
visited = [False]*n
finished = [False]*n
stack = [0]
while stack:
	start = stack[-1]
	if not visited[start]:
		visited[start] = True
		for child in gr[start]:
			if not visited[child]:
				stack.append(child)
	else:
		stack.pop()
		for child in gr[start]:
			if finished[child]:
				# perform the post rec operations here
				pass
		finished[start] = True