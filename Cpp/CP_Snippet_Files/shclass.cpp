int HMOD = 2147483647;
int HBASE1 = rand() % HMOD;
int HBASE2 = rand() % HMOD;

class Hashing {
public:
	int mod, base1, base2, _len;
	vector<int> f_hash, f_pow, s_hash, s_pow;

	Hashing(const string& s, int mod = HMOD, int base1 = HBASE1, int base2 = HBASE2) : mod(mod), base1(base1), base2(base2) {
		_len = s.size();
		f_hash.assign(_len + 1, 0);
		f_pow.assign(_len + 1, 1);
		s_hash.assign(_len + 1, 0);
		s_pow.assign(_len + 1, 1);

		for (int i = 0; i < _len; ++i) {
			f_hash[i + 1] = (base1 * f_hash[i] + s[i]) % mod;
			s_hash[i + 1] = (base2 * s_hash[i] + s[i]) % mod;
			f_pow[i + 1] = base1 * f_pow[i] % mod;
			s_pow[i + 1] = base2 * s_pow[i] % mod;
		}
	}

	pair<int, int> hashed(int start, int stop) {
		int hash1 = (f_hash[stop] - f_pow[stop - start] * f_hash[start] % mod + mod) % mod;
		int hash2 = (s_hash[stop] - s_pow[stop - start] * s_hash[start] % mod + mod) % mod;
		return {hash1, hash2};
	}

	pair<vector<int>, vector<int>> get_hashes(int length) {
		vector<int> f_res, s_res;
		for (int i = 0; i <= _len - length; ++i) {
			f_res.push_back((f_hash[i + length] - f_pow[length] * f_hash[i] % mod + mod) % mod);
			s_res.push_back((s_hash[i + length] - s_pow[length] * s_hash[i] % mod + mod) % mod);
		}
		return {f_res, s_res};
	}
};