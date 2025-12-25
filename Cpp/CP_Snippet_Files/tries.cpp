vector<int> left_child = {0}, right_child = {0}, treap_keys = {0};
vector<double> treap_prior = {0.0};

int treap_create_node(int key) {
	treap_keys.push_back(key);
	treap_prior.push_back((double)rand() / RAND_MAX);
	left_child.push_back(0);
	right_child.push_back(0);
	return treap_keys.size() - 1;
}

pair<int, int> treap_split(int root, int key) {
	int left_pos = 0, right_pos = 0;
	while (root) {
		if (key < treap_keys[root]) {
			left_child[right_pos] = right_pos = root;
			root = left_child[root];
		} else {
			right_child[left_pos] = left_pos = root;
			root = right_child[root];
		}
	}
	int left = right_child[0], right = left_child[0];
	right_child[left_pos] = left_child[right_pos] = right_child[0] = left_child[0] = 0;
	return {left, right};
}

int treap_merge(int left, int right) {
	int where = 0, pos = 0;
	while (left && right) {
		if (treap_prior[left] > treap_prior[right]) {
			right_child[where] = where = left;
			left = right_child[left];
		} else {
			left_child[where] = where = right;
			right = left_child[right];
		}
	}
	right_child[where] = left ? left : right;
	int node = right_child[0];
	right_child[0] = 0;
	return node;
}

int treap_insert(int root, int key) {
	auto [left, right] = treap_split(root, key);
	return treap_merge(treap_merge(left, treap_create_node(key)), right);
}

class Trie {
public:
	unordered_map<char, Trie*> children;
	bool is_end = false;

	void add(const string& word) {
		Trie* node = this;
		for (char ch : word) {
			if (!node->children.count(ch)) {
				node->children[ch] = new Trie();
			}
			node = node->children[ch];
		}
		node->is_end = true;
	}

	bool contains(const string& word) const {
		const Trie* node = this;
		for (char ch : word) {
			if (!node->children.count(ch)) {
				return false;
			}
			node = node->children.at(ch);
		}
		return node->is_end;
	}

	void remove(const string& word) {
		vector<Trie*> nodes;
		Trie* node = this;
		for (char ch : word) {
			if (!node->children.count(ch)) return;
			nodes.push_back(node);
			node = node->children[ch];
		}
		node->is_end = false;
		for (int i = nodes.size() - 1; i >= 0; --i) {
			char ch = word[i];
			if (!nodes[i]->children[ch]->is_end && nodes[i]->children[ch]->children.empty()) {
				delete nodes[i]->children[ch];
				nodes[i]->children.erase(ch);
			}
		}
	}
};