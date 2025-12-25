class Line1 {
public:
	int m, b;
	Line1(int m = 0, int b = INF) : m(m), b(b) {}
	int operator()(int x) const {
		return m * x + b;
	}
};
class ConvexHull {
public:
	int n;
	vector<Line1> seg;
	vector<int> lo, hi;
	ConvexHull(int n = 1000000) : n(n), seg(4 * n, Line1()), lo(4 * n), hi(4 * n) {
		build(1, 1, n);
	}
	void build(int i, int l, int r) {
		stack<tuple<int, int, int>> stack;
		stack.emplace(i, l, r);
		while (!stack.empty()) {
			auto [idx, left, right] = stack.top();
			stack.pop();
			lo[idx] = left;
			hi[idx] = right;
			seg[idx] = Line1(0, INF);
			if (left == right) continue;
			int mid = (left + right) / 2;
			stack.emplace(2 * idx + 1, mid + 1, right);
			stack.emplace(2 * idx, left, mid);
		}
	}
	void insert(Line1 L) {
		int pos = 1;
		while (true) {
			int l = lo[pos], r = hi[pos];
			if (l == r) {
				if (L(l) < seg[pos](l)) seg[pos] = L;
				break;
			}
			int m = (l + r) / 2;
			if (seg[pos].m < L.m) swap(seg[pos], L);
			if (seg[pos](m) > L(m)) {
				swap(seg[pos], L);
				pos = 2 * pos;
			} else {
				pos = 2 * pos + 1;
			}
		}
	}
	int query(int x) {
		int i = 1, res = seg[i](x), pos = i;
		while (true) {
			int l = lo[pos], r = hi[pos];
			res = min(res, seg[pos](x));
			if (l == r) return res;
			int m = (l + r) / 2;
			pos = (x < m) ? 2 * pos : 2 * pos + 1;
		}
	}
};


struct Line {
	int m, b, c;
	int operator()(int x){
		return m * x + b;
	}
};
struct CHT {
	Line dq[200000];
	int fptr, bptr;
	void clear(){
		dq[0] = {0, 0, 0};
		fptr = 0; bptr = 1;
	}
	bool pop_back(Line& L, Line& L1, Line& L2){
		int v1 = (L.b - L2.b) * (L2.m - L1.m);
		int v2 = (L2.m - L.m) * (L1.b - L2.b);
		return (v1 == v2 ? L.c > L1.c : v1 < v2);
	}
	bool pop_front(Line& L1, Line& L2, int x){
		int v1 = L1(x);
		int v2 = L2(x);
		return (v1 == v2 ? L1.c < L2.c : v1 > v2);
	}
	void insert(Line L){
		while(bptr-fptr >= 2 && pop_back(L, dq[bptr-1], dq[bptr-2]))	bptr--;
		dq[bptr++] = L;
	}
	pi query(int x){
		while(bptr-fptr >= 2 && pop_front(dq[fptr], dq[fptr+1], x))	 fptr++;
		return {dq[fptr](x), dq[fptr].c};
	}
};