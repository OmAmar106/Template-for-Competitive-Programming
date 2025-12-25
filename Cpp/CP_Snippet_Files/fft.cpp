class FFT {
public:
	static const int MOD = 998244353;
	static const int MOD1 = 469762049;
	int MOD2, mod_inv;
	vector<int> W, W1, iW, iW1;

	FFT() {
		MOD2 = power(MOD, MOD1 - 2, MOD1);
		mod_inv = XT_GCD(MOD, MOD1).second % MOD1;
		int g = 3;
		int ig = power(g, MOD - 2, MOD);
		int ig1 = power(g, MOD1 - 2, MOD1);
		W.resize(30); W1.resize(30); iW.resize(30); iW1.resize(30);
		for (int i = 0; i < 30; ++i) {
			W[i] = power(g, (MOD - 1) >> i, MOD);
			W1[i] = power(g, (MOD1 - 1) >> i, MOD1);
			iW[i] = power(ig, (MOD - 1) >> i, MOD);
			iW1[i] = power(ig1, (MOD1 - 1) >> i, MOD1);
		}
	}

	int power(int base, int exp, int mod) {
		int res = 1;
		while (exp) {
			if (exp % 2) res = res * base % mod;
			base = base * base % mod;
			exp /= 2;
		}
		return res;
	}

	pair<int, int> XT_GCD(int a, int b) {
		if (b == 0) return {a, 1};
		pair<int,int> k9 = XT_GCD(b, a % b);
		int g = k9.first;int x1 = k9.second;
		return {g, x1 - (a / b) * x1};
	}

	int CRT(int a, int mod1, int b, int mod2) {
		return (a + (b - a) * mod_inv % mod2 * mod1) % (mod1 * mod2);
	}

	void fft(int k, vector<int>& f, vector<int>& f1) {
		for (int l = k; l > 0; --l) {
			int d = 1 << (l - 1);
			vector<pair<int, int>> U = {{1, 1}};
			for (int i = 0; i < d; ++i)
				U.emplace_back(U.back().first * W[l] % MOD, U.back().second * W1[l] % MOD1);
			for (int i = 0; i < (1 << (k - l)); ++i) {
				for (int j = 0; j < d; ++j) {
					int s = i * 2 * d + j;
					int tmp_f = f[s] - f[s + d];
					int tmp_f1 = f1[s] - f1[s + d];
					f[s] = (f[s] + f[s + d]) % MOD;
					f[s + d] = U[j].first * tmp_f % MOD;
					f1[s] = (f1[s] + f1[s + d]) % MOD1;
					f1[s + d] = U[j].second * tmp_f1 % MOD1;
				}
			}
		}
	}

	void ifft(int k, vector<int>& f, vector<int>& f1) {
		for (int l = 1; l <= k; ++l) {
			int d = 1 << (l - 1);
			for (int i = 0; i < (1 << (k - l)); ++i) {
				int u = 1, u1 = 1;
				for (int j = i * 2 * d; j < (i * 2 + 1) * d; ++j) {
					f[j + d] = f[j + d] * u % MOD;
					f[j] = (f[j] + f[j + d]) % MOD;
					f[j + d] = (f[j] - f[j + d] + MOD) % MOD;
					u = u * iW[l] % MOD;
					f1[j + d] = f1[j + d] * u1 % MOD1;
					f1[j] = (f1[j] + f1[j + d]) % MOD1;
					f1[j + d] = (f1[j] - f1[j + d] + MOD1) % MOD1;
					u1 = u1 * iW1[l] % MOD1;
				}
			}
		}
	}

	vector<int> convolve(vector<int> A, vector<int> B) {
		int n0 = A.size() + B.size() - 1;
		int k = 0;
		while ((1 << k) < n0) ++k;
		int n = 1 << k;
		A.resize(n, 0);
		B.resize(n, 0);
		vector<int> A1 = A, B1 = B;
		fft(k, A, A1);
		fft(k, B, B1);
		for (int i = 0; i < n; ++i) {
			A[i] = A[i] * B[i] % MOD;
			A1[i] = A1[i] * B1[i] % MOD1;
		}
		ifft(k, A, A1);
		int inv = power(n, MOD - 2, MOD);
		int inv1 = power(n, MOD1 - 2, MOD1);
		A.resize(n0);
		for (int i = 0; i < n0; ++i) {
			A[i] = CRT(A[i] * inv % MOD, MOD, A1[i] * inv1 % MOD1, MOD1);
		}
		return A;
	}
};