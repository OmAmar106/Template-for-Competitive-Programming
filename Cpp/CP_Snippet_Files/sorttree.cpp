class MergeSortTree {
	public:
		int n;
		vector<vector<int>> tree;
		static vector<int> merge(const vector<int>& a, const vector<int>& b) {
			int i = 0, j = 0, k =0;
			int t = a.size();
			int t1 = b.size();
			vector<int> L(t+t1);
			while (i < t && j < t1) {
				if (a[i] < b[j]) {
					L[k++] = (a[i++]);
				} else {
					L[k++] = (b[j++]);
				}
			}
			while (i < t) L[k++] = (a[i++]);
			while (j < t1) L[k++] = (b[j++]);
			return L;
		}
		static int func(const vector<int>& L, int l, int r) {
			return upper_bound(L.begin(), L.end(), r) - lower_bound(L.begin(), L.end(), l);
		}
		MergeSortTree(const vector<int>& data) {
			n = data.size();
			tree.resize(2 * n);
			build(data);
		}
		void build(const vector<int>& data) {
			for (int i = 0; i < n; ++i) {
				tree[n + i] = {data[i]};
			}
			for (int i = n - 1; i > 0; --i) {
				tree[i] = merge(tree[i * 2], tree[i * 2 + 1]);
			}
		}
		void update(int pos, int value) {
			pos += n;
			tree[pos] = {value};
			while (pos > 1) {
				pos /= 2;
				tree[pos] = merge(tree[pos * 2], tree[pos * 2 + 1]);
			}
		}
		int query(int left, int right, int l, int r) {
			left += n;
			right += n;
			int res = 0;
			while (left < right) {
				if (left % 2 == 1) {
					res += func(tree[left], l, r);
					left++;
				}
				if (right % 2 == 1) {
					right--;
					res += func(tree[right], l, r);
				}
				left >>= 1;
				right >>= 1;
			}
			return res;
		}
	};