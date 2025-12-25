class Factorial {
public:
	int mod;
	vector<int> f, g;

	Factorial(int N, int mod) : mod(mod) {
		N += 1;
		f.resize(N, 1);
		g.resize(N, 1);
		for (int i = 1; i < N; i++) {
			f[i] = f[i - 1] * i % mod;
		}
		g[N - 1] = pow_mod(f[N - 1], mod - 2, mod);
		for (int i = N - 2; i >= 0; i--) {
			g[i] = g[i + 1] * (i + 1) % mod;
		}
	}

	int pow_mod(int a, int b, int m) {
		int res = 1;
		while (b) {
			if (b & 1) res = res * a % m;
			a = a * a % m;
			b >>= 1;
		}
		return res;
	}

	int fac(int n) { return f[n]; }
	int fac_inv(int n) { return g[n]; }

	int combi(int n, int m) {
		if (m == 0) return 1;
		if (n < m || m < 0 || n < 0) return 0;
		return f[n] * g[m] % mod * g[n - m] % mod;
	}

	int permu(int n, int m) {
		if (n < m || m < 0 || n < 0) return 0;
		return f[n] * g[n - m] % mod;
	}

	int catalan(int n) {
		return (combi(2 * n, n) - combi(2 * n, n - 1) + mod) % mod;
	}

	int inv(int n) {
		return f[n - 1] * g[n] % mod;
	}
};