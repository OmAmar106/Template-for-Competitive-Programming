struct Node {
	int val;

	Node(){val=0;}
	Node(int v = 0) { val = v; }

	// merge
	static Node func(const Node* left, const Node* right) {
		if (!right) {
			if (!left) return Node(0);
			return *left;
		}
		if (!left) return *right;
		return Node(left->val + right->val);
	}

	void add(int v) { val += v; }
	void set(int v) { val = v; }
};

class SegmentTree {
public:
	int n;
	vector<Node> tree;
	vector<int> lazy_add;
	vector<int> lazy_set;
	vector<bool> has_set;

	SegmentTree(vector<int>& data) {
		n = data.size();
		tree.resize(4*n);
		lazy_add.assign(4*n, 0);
		lazy_set.assign(4*n, 0);
		has_set.assign(4*n, false);
		build(1, 0, n-1, data);
	}

	void build(int idx, int l, int r, vector<int>& data) {
		if (l == r) {
			tree[idx] = Node(data[l]);
			return;
		}
		int mid = (l + r) / 2;
		build(idx*2, l, mid, data);
		build(idx*2+1, mid+1, r, data);
		tree[idx] = Node::func(&tree[idx*2], &tree[idx*2+1]);
	}

	void apply_set(int idx, int l, int r, int val) {
		tree[idx].set(val * (r - l + 1));
		lazy_set[idx] = val;
		has_set[idx] = true;
		lazy_add[idx] = 0;
	}

	void apply_add(int idx, int l, int r, int val) {
		tree[idx].add(val * (r - l + 1));
		if (has_set[idx]) lazy_set[idx] += val;
		else lazy_add[idx] += val;
	}

	void push(int idx, int l, int r) {
		if (l == r) return;
		int mid = (l + r) / 2;

		if (has_set[idx]) {
			apply_set(idx*2, l, mid, lazy_set[idx]);
			apply_set(idx*2+1, mid+1, r, lazy_set[idx]);
			has_set[idx] = false;
		}
		if (lazy_add[idx]) {
			apply_add(idx*2, l, mid, lazy_add[idx]);
			apply_add(idx*2+1, mid+1, r, lazy_add[idx]);
			lazy_add[idx] = 0;
		}
	}

	// Range Update in [L,R] if flag, then add
	void update(int idx, int l, int r, int ql, int qr, int val, bool add_flag) {
		if (qr < l || r < ql) return;

		if (ql <= l && r <= qr) {
			if (add_flag) apply_add(idx, l, r, val);
			else apply_set(idx, l, r, val);
			return;
		}

		push(idx, l, r);

		int mid = (l + r) / 2;
		update(idx*2, l, mid, ql, qr, val, add_flag);
		update(idx*2+1, mid+1, r, ql, qr, val, add_flag);

		tree[idx] = Node::func(&tree[idx*2], &tree[idx*2+1]);
	}

	// Range Query in [L,R]
	Node query(int idx, int l, int r, int ql, int qr) {
		if (qr < l || r < ql) return Node(0);

		if (ql <= l && r <= qr) return tree[idx];

		push(idx, l, r);

		int mid = (l + r) / 2;
		Node left = query(idx*2, l, mid, ql, qr);
		Node right = query(idx*2+1, mid+1, r, ql, qr);

		return Node::func(&left, &right);
	}
};
