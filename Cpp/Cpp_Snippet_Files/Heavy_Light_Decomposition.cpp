struct HLD {
	int n, N;
	vector<vector<int>> adj;
	vector<int> parent, depth, size, heavy, head, pos, seg;

	HLD(vector<vector<int>>& g, vector<int>& val) {
		adj = g;
		n = adj.size();

		parent.assign(n, -1);
		depth.assign(n, 0);
		size.assign(n, 0);
		heavy.assign(n, -1);
		head.assign(n, 0);
		pos.assign(n, 0);

		stack<tuple<int,int,int>> st;
		st.push({0, -1, 0});

		while (!st.empty()) {
			auto [u, p, state] = st.top(); st.pop();
			if (state == 0) {
				st.push({u, p, 1});
				for (int v : adj[u]) {
					if (v == p) continue;
					parent[v] = u;
					depth[v] = depth[u] + 1;
					st.push({v, u, 0});
				}
			} else {
				size[u] = 1;
				int mx = 0;
				for (int v : adj[u]) {
					if (v == p) continue;
					size[u] += size[v];
					if (size[v] > mx) {
						mx = size[v];
						heavy[u] = v;
					}
				}
			}
		}

		int cur = 0;
		stack<pair<int,int>> st2;
		st2.push({0, 0});

		while (!st2.empty()) {
			auto [u, h] = st2.top(); st2.pop();
			while (u != -1) {
				head[u] = h;
				pos[u] = cur++;

				int hu = heavy[u];
				for (int v : adj[u]) {
					if (v != parent[u] && v != hu)
						st2.push({v, v});
				}
				u = hu;
			}
		}

		N = 1;
		while (N < n) N <<= 1;
		seg.assign(2*N, 0);

		for (int i = 0; i < n; i++)
			seg[N + pos[i]] = val[i];

		for (int i = N - 1; i > 0; i--)
			seg[i] = max(seg[2*i], seg[2*i+1]);
	}

	void update(int u, int x) {
		int i = pos[u] + N;
		seg[i] = x;
		for (i >>= 1; i; i >>= 1)
			seg[i] = max(seg[2*i], seg[2*i+1]);
	}

	int query(int u, int v) {
		int res = 0;

		while (head[u] != head[v]) {
			if (depth[head[u]] < depth[head[v]])
				swap(u, v);

			int l = pos[head[u]] + N;
			int r = pos[u] + N + 1;

			while (l < r) {
				if (l & 1) res = max(res, seg[l++]);
				if (r & 1) res = max(res, seg[--r]);
				l >>= 1; r >>= 1;
			}

			u = parent[head[u]];
		}

		if (depth[u] > depth[v]) swap(u, v);

		int l = pos[u] + N;
		int r = pos[v] + N + 1;

		while (l < r) {
			if (l & 1) res = max(res, seg[l++]);
			if (r & 1) res = max(res, seg[--r]);
			l >>= 1; r >>= 1;
		}

		return res;
	}
};
