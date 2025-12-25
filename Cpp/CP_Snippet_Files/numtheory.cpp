int mod_exp(int base, int exp, int mod = MOD) {
	int res = 1;
	while (exp) {
		if (exp % 2) res = res * base % mod;
		base = base * base % mod;
		exp /= 2;
	}
	return res;
}

vector<vector<int>> matmul(const vector<vector<int>> &A, const vector<vector<int>> &B) {
	int n = A.size(), m = B[0].size(), p = B.size();
	vector<vector<int>> ans(n, vector<int>(m, 0));
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			for (int k = 0; k < p; ++k) {
				ans[i][j] = (ans[i][j] + A[i][k] * B[k][j]) % MOD;
			}
		}
	}
	return ans;
}

vector<vector<int>> matpow(vector<vector<int>> M, int power) {
	int size = M.size();
	vector<vector<int>> result(size, vector<int>(size, 0));
	for (int i = 0; i < size; ++i) result[i][i] = 1;
	while (power) {
		if (power % 2 == 1) result = matmul(result, M);
		M = matmul(M, M);
		power /= 2;
	}
	return result;
}

vector<int> sieve(int n) {
	vector<int> primes;
	vector<bool> isp(n + 1, true);
	isp[0] = isp[1] = false;
	for (int i = 2; i <= n; ++i) {
		if (isp[i]) {
			primes.push_back(i);
			for (int j = i * i; j <= n; j += i) isp[j] = false;
		}
	}
	return primes;
}

bool is_prime(int n) {
	if (n <= 1) return false;
	if (n <= 3) return true;
	if (n % 2 == 0 || n % 3 == 0) return false;
	for (int i = 5; i * i <= n; i += 6) {
		if (n % i == 0 || n % (i + 2) == 0) return false;
	}
	return true;
}

vector<int> all_factors(int n) {
	vector<int> small, large;
	for (int i = 1; i * i <= n; i += (n & 1) ? 2 : 1) {
		if (n % i == 0) {
			small.push_back(i);
			if (i != n / i) large.push_back(n / i);
		}
	}
	reverse(large.begin(), large.end());
	small.insert(small.end(), large.begin(), large.end());
	return small;
}

vector<int> sieve_unique(int N) {
	vector<int> mini(N);
	iota(mini.begin(), mini.end(), 0);
	for (int i = 2; i < N; ++i) {
		if (mini[i] == i) {
			for (int j = 2 * i; j < N; j += i) mini[j] = i;
		}
	}
	return mini;
}

vector<int> prime_factors(int k, const vector<int>& Lmini) {
	vector<int> ans;
	while (k != 1) {
		ans.push_back(Lmini[k]);
		k /= Lmini[k];
	}
	return ans;
}

int mod_inverse(int a, int mod = MOD) {
	return mod_exp(a, mod - 2, mod);
}
