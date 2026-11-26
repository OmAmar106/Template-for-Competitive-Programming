struct Node {
	int val, pr, sz;
	Node *l, *r;
	Node(int v) : val(v), pr(rng()), sz(1), l(nullptr), r(nullptr) {}
};

int sz(Node* t) { return t ? t->sz : 0; }

void upd(Node* t) {
	if (t) t->sz = 1 + sz(t->l) + sz(t->r);
}

Node* merge(Node* a, Node* b) {
	if (!a || !b) return a ? a : b;

	if (a->pr > b->pr) {
		a->r = merge(a->r, b);
		upd(a);
		return a;
	} else {
		b->l = merge(a, b->l);
		upd(b);
		return b;
	}
}

pair<Node*,Node*> split(Node* t, int k) {
	if (!t) return {nullptr,nullptr};

	if (sz(t->l) >= k) {
		auto p = split(t->l, k);
		t->l = p.second;
		upd(t);
		return {p.first, t};
	} else {
		auto p = split(t->r, k - sz(t->l) - 1);
		t->r = p.first;
		upd(t);
		return {t, p.second};
	}
}

void inorder(Node* t, string &s, string &out) {
	if (!t) return;
	inorder(t->l, s, out);
	out += s[t->val];
	inorder(t->r, s, out);
}
