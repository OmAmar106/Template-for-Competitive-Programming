class DiophantineEquations {
public:
	DiophantineEquations() {}

	tuple<int, int, int> euclidean_gcd(int a, int b) {
		if (b == 0) return make_tuple(a, 1, 0);
		tuple<int, int, int> result = euclidean_gcd(b, a % b);
		int g = get<0>(result);
		int x1 = get<1>(result);
		int y1 = get<2>(result);
		int x = y1;
		int y = x1 - (a / b) * y1;
		return make_tuple(g, x, y);
	}

	pair<int, int> soln(int a, int b, int c, int t = 1e18, int t1 = 1e18) {
		int g = gcd(a, b);
		if (c % g != 0) return make_pair(-1, -1);
		tuple<int, int, int> result = euclidean_gcd(a, b);
		int x = get<1>(result);
		int y = get<2>(result);
		int k3 = x * (c / g);
		int n1 = y * (c / g);
		int k1 = max((int)ceil(-k3 * g / (double)b), (int)ceil((n1 - t1) / (a / (double)g)));
		int kmaxi = min((int)floor((t - k3) / (b / (double)g)), (int)floor(n1 / (a / (double)g)));
		if (k1 <= kmaxi) {
			int k = k1;
			int m = k3 + k * (b / g);
			int n = n1 - k * (a / g);
			return make_pair(m, n);
		}
		return make_pair(-1, -1);
	}

	pair<int, int> sollnll(int a, int b, int c, int t, int t1, int m_lower, int n_lower) {
		int g = gcd(a, b);
		if (c % g != 0) return make_pair(-1, -1);
		tuple<int, int, int> result = euclidean_gcd(a, b);
		int x = get<1>(result);
		int y = get<2>(result);
		int k3 = x * (c / g);
		int n1 = y * (c / g);
		int k1 = max((int)ceil((m_lower - k3 * g) / (double)b), (int)ceil((n1 - t1) / (a / (double)g)));
		int kmaxi = min((int)floor((t - k3) / (b / (double)g)), (int)floor((n1 - n_lower) / (a / (double)g)));
		if (k1 <= kmaxi) {
			int k = k1;
			int m = k3 + k * (b / g);
			int n = n1 - k * (a / g);
			if (m_lower <= m && m <= t && n_lower <= n && n <= t1) {
				return make_pair(m, n);
			}
		}
		return make_pair(-1, -1);
	}
};