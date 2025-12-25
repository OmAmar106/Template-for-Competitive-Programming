class SegmentTree {
public:
	int n;
	vector<int> tree;
	vector<int> lazy_add;
	vector<int> lazy_set;
	int NO_ASSIGNMENT = LLONG_MIN;
	SegmentTree(vector<int>& arr) {
		n = arr.size();
		tree.assign(4 * n, 0);
		lazy_add.assign(4 * n, 0);
		lazy_set.assign(4 * n, NO_ASSIGNMENT);
		build_tree(1, 0, n - 1, arr);
	}
	static int func(int a, int b) {
		return a + b;
	}
	void build_tree(int node, int start, int end, vector<int>& arr) {
		if (start == end) {
			tree[node] = arr[start];
		} else {
			int mid = start + (end - start) / 2;
			build_tree(2 * node, start, mid, arr);
			build_tree(2 * node + 1, mid + 1, end, arr);
			tree[node] = func(tree[2 * node], tree[2 * node + 1]);
		}
	}
	void propagate_lazy(int node, int start, int end) {
		int current_range_size = (end - start + 1);
		if (lazy_set[node] != NO_ASSIGNMENT) {
			tree[node] = lazy_set[node] * current_range_size;
			if (start != end) {
				lazy_set[2 * node] = lazy_set[node];
				lazy_set[2 * node + 1] = lazy_set[node];
				lazy_add[2 * node] = 0;
				lazy_add[2 * node + 1] = 0;
			}
			lazy_set[node] = NO_ASSIGNMENT;
		}
		if (lazy_add[node] != 0) {
			tree[node] += lazy_add[node] * current_range_size;
			if (start != end) {
				lazy_add[2 * node] += lazy_add[node];
				lazy_add[2 * node + 1] += lazy_add[node];
			}
			lazy_add[node] = 0;
		}
	}
	void update(int node, int start, int end, int l, int r, int value, bool is_add) {
		propagate_lazy(node, start, end);
		if (start > r || end < l) {
			return;
		}
		if (start >= l && end <= r) {
			if (is_add) {
				tree[node] += value * (end - start + 1);
				if (start != end) {
					lazy_add[2 * node] += value;
					lazy_add[2 * node + 1] += value;
				}
			} else {
				tree[node] = value * (end - start + 1);
				if (start != end) {
					lazy_set[2 * node] = value;
					lazy_set[2 * node + 1] = value;
					lazy_add[2 * node] = 0;
					lazy_add[2 * node + 1] = 0;
				}
			}
			return;
		}
		int mid = start + (end - start) / 2;
		update(2 * node, start, mid, l, r, value, is_add);
		update(2 * node + 1, mid + 1, end, l, r, value, is_add);
		tree[node] = func(tree[2 * node], tree[2 * node + 1]);
	}
	int query(int node, int start, int end, int l, int r) {
		propagate_lazy(node, start, end);
		if (start > r || end < l) {
			return 0;
		}
		if (start >= l && end <= r) {
			return tree[node];
		}
		int mid = start + (end - start) / 2;
		return func(query(2 * node, start, mid, l, r), query(2 * node + 1, mid + 1, end, l, r));
	}
	void range_update(int l, int r, int value, bool is_add = true) {
		update(1, 0, n - 1, l, r, value, is_add);
	}
	int range_query(int l, int r) {
		return query(1, 0, n - 1, l, r);
	}
	vector<int> to_list() {
		vector<int> result(n);
		for (int i = 0; i < n; ++i) {
			result[i] = range_query(i, i);
		}
		return result;
	}
};