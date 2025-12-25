class SparseTable {
public:
	int n;
	vector<vector<int>> table;

	static int func(int a, int b) {
		return gcd(a, b);
	}

	SparseTable(const vector<int>& arr) {
		n = arr.size();
		int log = log2(n) + 1;
		table.assign(n, vector<int>(log, 0));
		build(arr);
	}

	void build(const vector<int>& arr) {
		for (int i = 0; i < n; ++i) {
			table[i][0] = arr[i];
		}
		for (int j = 1; (1 << j) <= n; ++j) {
			for (int i = 0; i + (1 << j) <= n; ++i) {
				table[i][j] = func(table[i][j - 1], table[i + (1 << (j - 1))][j - 1]);
			}
		}
	}

	int query(int L, int R) {
		int j = log2(R - L + 1);
		return func(table[L][j], table[R - (1 << j) + 1][j]);
	}
};