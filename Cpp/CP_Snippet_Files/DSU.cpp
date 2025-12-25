class DisjointSetUnion {
public:
	vector<int> parent, size;

	DisjointSetUnion(int n) : parent(n), size(n, 1) {
		iota(parent.begin(), parent.end(), 0);
	}

	int find(int a) {
		if (parent[a] != a) {
			parent[a] = find(parent[a]);
		}
		return parent[a];
	}

	void unite(int a, int b) {
		a = find(a);
		b = find(b);
		if (a != b) {
			if (size[a] < size[b]) swap(a, b);
			parent[b] = a;
			size[a] += size[b];
		}
	}

	int set_size(int a) {
		return size[find(a)];
	}

	int notfind(int a) {
		int k = find(a);
		for (int i = 0; i < parent.size(); i++) {
			if (find(i) != k) {
				return i;
			}
		}
		return -1;
	}
};