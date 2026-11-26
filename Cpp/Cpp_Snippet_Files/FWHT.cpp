void fwht(vector<long long>& a, bool invert = false) {
	int n = a.size();
	for (int step = 1; step < n; step <<= 1) {
		for (int i = 0; i < n; i += (step << 1)) {
			for (int j = 0; j < step; j++) {
				long long u = a[i + j];
				long long v = a[i + j + step];
				a[i + j] = u + v;
				a[i + j + step] = u - v;
			}
		}
	}
	if (invert) {
		for (auto &x : a) x /= n;
	}
}

void fwt_or(vector<long long>& a, bool invert = false) {
	int n = a.size();
	for (int step = 1; step < n; step <<= 1) {
		for (int i = 0; i < n; i += (step << 1)) {
			for (int j = 0; j < step; j++) {
				long long u = a[i + j];
				long long v = a[i + j + step];
				if (!invert)
					a[i + j + step] = u + v;
				else
					a[i + j + step] = v - u;
			}
		}
	}
}

void fwt_and(vector<long long>& a, bool invert = false) {
	int n = a.size();
	for (int step = 1; step < n; step <<= 1) {
		for (int i = 0; i < n; i += (step << 1)) {
			for (int j = 0; j < step; j++) {
				long long u = a[i + j];
				long long v = a[i + j + step];
				if (!invert)
					a[i + j] = u + v;
				else
					a[i + j] = u - v;
			}
		}
	}
}

vector<long long> convolution(vector<long long> A, vector<long long> B) {
	int n = 1;
	int x = max(A.size(), B.size());
	while (n < x) n <<= 1;
	n <<= 1;

	A.resize(n);
	B.resize(n);

	fwht(A);
	fwht(B);

	for (int i = 0; i < n; i++)
		A[i] *= B[i];

	fwht(A, true);
	return A;
}
