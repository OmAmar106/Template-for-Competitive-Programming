class SegmentTree {
public:
	int n;
	vector<int> tree;

	static int func(int a, int b) {
		return max(a, b);
	}

	SegmentTree(const vector<int>& data) {
		n = data.size();
		tree.resize(2 * n);
		build(data);
	}

	void build(const vector<int>& data) {
		for (int i = 0; i < n; ++i) {
			tree[n + i] = data[i];
		}
		for (int i = n - 1; i > 0; --i) {
			tree[i] = func(tree[i * 2], tree[i * 2 + 1]);
		}
	}

	void update(int pos, int value) {
		pos += n;
		tree[pos] = value;
		while (pos > 1) {
			pos /= 2;
			tree[pos] = func(tree[2 * pos], tree[2 * pos + 1]);
		}
	}

	int query(int left, int right) {
		left += n;
		right += n;
		int max_val = LLONG_MIN;
		while (left < right) {
			if (left % 2 == 1) {
				max_val = func(max_val, tree[left]);
				left++;
			}
			if (right % 2 == 1) {
				right--;
				max_val = func(max_val, tree[right]);
			}
			left /= 2;
			right /= 2;
		}
		return max_val;
	}
};