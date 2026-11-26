int ctz(int x) { return __builtin_ctz(x); }

pair<vector<vector<int>>, int> shallowest_decomposition_tree(const vector<vector<int>>& graph, int root = 0) {
	int n = graph.size();
	vector<int> forbidden(n, 0);
	vector<vector<int>> decomposition_tree(n);
	vector<vector<int>> stacks(32);

	auto extract_chain = [&](int labels, int u) {
		while (labels) {
			int label = 31 - __builtin_clz(labels);
			labels ^= (1 << label);
			int v = stacks[label].back();
			stacks[label].pop_back();
			decomposition_tree[u].push_back(v);
			u = v;
		}
	};

	vector<int> dfs;
	dfs.push_back(root);

	while (!dfs.empty()) {
		int u = dfs.back(); dfs.pop_back();
		if (u >= 0) {
			forbidden[u] = -1;
			dfs.push_back(~u);
			for (int v : graph[u])
				if (!forbidden[v]) dfs.push_back(v);
		} else {
			u = ~u;
			int forbidden_once = 0, forbidden_twice = 0;
			for (int v : graph[u]) {
				forbidden_twice |= forbidden_once & (forbidden[v] + 1);
				forbidden_once |= forbidden[v] + 1;
			}
			forbidden[u] = forbidden_once | ((1 << (32 - __builtin_clz(forbidden_twice))) - 1);
			int label_u = ctz(forbidden[u] + 1);
			stacks[label_u].push_back(u);
			for (int v : graph[u])
				extract_chain((forbidden[v] + 1) & ((1 << label_u) - 1), u);
		}
	}

	int max_label = 31 - __builtin_clz(forbidden[root] + 1);
	int decomposition_root = stacks[max_label].back();
	stacks[max_label].pop_back();
	extract_chain((forbidden[root] + 1) & ((1 << max_label) - 1), decomposition_root);

	return {decomposition_tree, decomposition_root};
}
