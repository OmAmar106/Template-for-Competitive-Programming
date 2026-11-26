struct RollbackDSU {
	vector<int> parent, sz;
	vector<tuple<int,int,int>> st;
	int components;

	RollbackDSU(int n) {
		parent.resize(n);
		sz.assign(n, 1);
		iota(parent.begin(), parent.end(), 0);
		components = n;
	}

	int find(int x) {
		while (x != parent[x])
			x = parent[x];
		return x;
	}

	void unite(int a, int b) {
		a = find(a);
		b = find(b);

		if (a == b) {
			st.emplace_back(-1, -1, -1);
			return;
		}

		components--;

		if (sz[a] > sz[b])
			swap(a, b);

		st.emplace_back(a, b, sz[b]);
		parent[a] = b;
		sz[b] += sz[a];
	}

	void rollback() {
		auto [a, b, s] = st.back();
		st.pop_back();

		if (a == -1) return;

		components++;
		parent[a] = a;
		sz[b] = s;
	}
};

struct ParPersistentDSU {
	vector<int> parent, sz;
	vector<int> time;

	ParPersistentDSU(int n) {
		parent.resize(n);
		sz.assign(n, 1);
		time.assign(n, INT_MAX);
		iota(parent.begin(), parent.end(), 0);
	}

	int find(int node, int version) {
		while (!(parent[node] == node || time[node] > version)) {
			node = parent[node];
		}
		return node;
	}

	bool unite(int a, int b, int t) {
		a = find(a, t);
		b = find(b, t);

		if (a == b)
			return false;

		if (sz[a] > sz[b])
			swap(a, b);

		parent[a] = b;
		time[a] = t;
		sz[b] += sz[a];

		return true;
	}

	bool isConnected(int a, int b, int version) {
		return find(a, version) == find(b, version);
	}
};
