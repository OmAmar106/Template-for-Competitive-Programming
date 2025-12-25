vector<int> bellman_ford(int n, vector<tuple<int, int, int>> &edges, int start){
	vector<int> dist(n, INF), pred(n, -1);
	dist[start] = 0;
	for (int i = 0; i < n - 1; i++) {
		for (int i = 0; i < edges.size(); i++) {
		int u = get<0>(edges[i]);
		int v = get<1>(edges[i]);
		int d = get<2>(edges[i]);
			if (dist[u] != INF && dist[u] + d < dist[v]) {
				dist[v] = dist[u] + d;
				pred[v] = u;
			}
		}
	}
	return dist;
}

class BinaryLift {
public:
	int n, L;
	vector<int> depth;
	vector<vector<int>> parent;

	BinaryLift(vector<vector<int>>& graph, int root = 0) {
		n = graph.size();
		L = 32 - __builtin_clz(n);
		parent.assign(L, vector<int>(n, -1));
		depth.assign(n, -1);
		queue<int> bfs;
		bfs.push(root);
		depth[root] = 0;
		while (!bfs.empty()) {
			int node = bfs.front(); bfs.pop();
			for (int nei : graph[node]) {
				if (depth[nei] == -1) {
					parent[0][nei] = node;
					depth[nei] = depth[node] + 1;
					bfs.push(nei);
				}
			}
		}
		for (int i = 1; i < L; i++) {
			for (int v = 0; v < n; v++) {
				if (parent[i - 1][v] != -1)
					parent[i][v] = parent[i - 1][parent[i - 1][v]];
			}
		}
	}

	int lca(int a, int b) {
		if (depth[a] < depth[b]) swap(a, b);
		int d = depth[a] - depth[b];
		for (int i = 0; i < L; i++) {
			if (d & (1LL << i)) a = parent[i][a];
		}
		if (a == b) return a;
		for (int i = L - 1; i >= 0; i--) {
			if (parent[i][a] != parent[i][b]) {
				a = parent[i][a];
				b = parent[i][b];
			}
		}
		return parent[0][a];
	}

	int distance(int a, int b) {
		return depth[a] + depth[b] - 2 * depth[lca(a, b)];
	}

	int kth_ancestor(int a, int k) {
		if (depth[a] < k) return -1;
		for (int i = 0; i < L; i++) {
			if (k & (1LL << i)) a = parent[i][a];
		}
		return a;
	}
};

vector<int> kahn(vector<vector<int>>& graph) {
	int n = graph.size();
	vector<int> indeg(n, 0), res;
	for (int i = 0; i < n; i++)
		for (int e : graph[i])
			indeg[e]++;
	queue<int> q;
	for (int i = 0; i < n; i++)
		if (indeg[i] == 0) q.push(i);
	while (!q.empty()) {
		int node = q.front(); q.pop();
		res.push_back(node);
		for (int e : graph[node]) {
			indeg[e]--;
			if (indeg[e] == 0) q.push(e);
		}
	}
	return res.size() == n ? res : vector<int>();
}

vector<pair<int, int>> dfs(vector<vector<int>>& graph) {
	int n = graph.size(), time = 0;
	vector<pair<int, int>> starttime(n, {0, 0});
	stack<tuple<int, int, int>> stack;
	stack.emplace(0, -1, 0);
	while (!stack.empty()) {
		int cur, prev, state;
		cur = get<0>(stack.top());
		prev = get<1>(stack.top());
		state = get<2>(stack.top());
		stack.pop();
		if (state == 0) {
			starttime[cur].first = time++;
			stack.emplace(cur, prev, 1);
			for (int neighbor : graph[cur]) {
				if (neighbor == prev) continue;
				stack.emplace(neighbor, cur, 0);
			}
		} else {
			starttime[cur].second = time;
		}
	}
	return starttime;
}

vector<int> euler_path(unordered_map<int, multiset<int>>& d) {
	vector<int> ans;
	stack<int> start;
	start.push(1);
	while (!start.empty()) {
		int cur = start.top();
		if (d[cur].empty()) {
			ans.push_back(cur);
			start.pop();
		} else {
			int k1 = *d[cur].begin();
			d[cur].erase(d[cur].begin());
			d[k1].erase(d[k1].find(cur));
			start.push(k1);
		}
	}
	return ans;
}

class TwoSat {
public:
	int n;
	vector<vector<int>> graph;

	TwoSat(int n) : n(n), graph(2 * n) {}

	int negate(int x) {
		return x < n ? x + n : x - n;
	}

	void _imply(int x, int y) {
		graph[x].push_back(y);
		graph[negate(y)].push_back(negate(x));
	}

	void either(int x, int y) {
		_imply(negate(x), y);
		_imply(negate(y), x);
	}

	void set(int x) {
		_imply(negate(x), x);
	}

	vector<vector<int>> find_SCC() {
		int n = graph.size();
		vector<int> order, comp(n, -1), low(n), depth(n, -1);
		vector<vector<int>> SCC;
		stack<int> st;
		int timer = 0;

		function<void(int)> dfs = [&](int v) {
			low[v] = depth[v] = timer++;
			st.push(v);
			for (int u : graph[v]) {
				if (depth[u] == -1) dfs(u);
				if (comp[u] == -1) low[v] = min(low[v], low[u]);
			}
			if (low[v] == depth[v]) {
				SCC.emplace_back();
				while (true) {
					int u = st.top(); st.pop();
					comp[u] = SCC.size() - 1;
					SCC.back().push_back(u);
					if (u == v) break;
				}
			}
		};

		for (int i = 0; i < n; i++) {
			if (depth[i] == -1) dfs(i);
		}
		return SCC;
	}

	pair<bool, vector<int>> solve() {
		auto SCC = find_SCC();
		vector<int> order(2 * n, 0);
		for (int i = 0; i < SCC.size(); i++)
			for (int x : SCC[i])
				order[x] = i;
		vector<int> res(n);
		for (int i = 0; i < n; i++) {
			if (order[i] == order[negate(i)])
				return {false, {}};
			res[i] = order[i] > order[negate(i)];
		}
		return {true, res};
	}
};