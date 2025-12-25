class BIT {
public:
	int n;
	vector<int> bit;

	BIT(vector<int>& arr) {
		n = arr.size();
		bit = arr;
		for (int i = 0; i < n; ++i) {
			int j = i | (i + 1);
			if (j < n) bit[j] += bit[i];
		}
	}

	void update(int idx, int x) {
		while (idx < n) {
			bit[idx] += x;
			idx |= idx + 1;
		}
	}

	int query(int end) {
		int x = 0;
		while (end > 0) {
			x += bit[end - 1];
			end &= end - 1;
		}
		return x;
	}

	int findkth(int k) {
		int idx = -1;
		for (int d = 63 - __builtin_clzll(n); d >= 0; --d) {
			int right_idx = idx + (1LL << d);
			if (right_idx < n && k >= bit[right_idx]) {
				idx = right_idx;
				k -= bit[idx];
			}
		}
		return idx + 1;
	}
};