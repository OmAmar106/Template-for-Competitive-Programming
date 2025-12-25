vector<int> bfsf(vector<vector<int>>& graph, int start = 0) {
	vector<int> bfs;
	vector<bool> visited(graph.size(), false);
	queue<int> q;
	q.push(start);
	visited[start] = true;
	while (!q.empty()) {
		int u = q.front(); q.pop();
		bfs.push_back(u);
		for (int j : graph[u]) {
			if (!visited[j]) {
				visited[j] = true;
				q.push(j);
			}
		}
	}
	return bfs;
}

pair<vector<int>, vector<int>> dijkstra(vector<vector<pair<int, int>>>& graph, int start, int n) {
	vector<int> dist(n, INF), parents(n, -1);
	priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
	dist[start] = 0;
	pq.emplace(0, start);
	while (!pq.empty()) {
		int path_len = pq.top().first; int v = pq.top().second; pq.pop();
		if (path_len > dist[v]) continue;
		for (const auto& p : graph[v]) {
			int w = p.first, edge_len = p.second;
			if (edge_len + path_len < dist[w]) {
				dist[w] = edge_len + path_len;
				parents[w] = v;
				pq.emplace(dist[w], w);
			}
		}
	}
	return {dist, parents};
}


vector<bool> dfs(vector<vector<int>>& graph, int start = 0) {
	int n = graph.size();
	vector<bool> visited(n, false);
	stack<int> st;
	st.push(start);
	while (!st.empty()) {
		int node = st.top();
		if (!visited[node]) {
			visited[node] = true;
			for (int child : graph[node]) {
				if (!visited[child]) {
					st.push(child);
				}
			}
		} else {
			st.pop();
		}
	}
	return visited;
}