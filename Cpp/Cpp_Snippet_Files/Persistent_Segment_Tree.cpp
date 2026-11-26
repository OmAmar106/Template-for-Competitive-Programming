struct PersistentSegmentTree {
	// Everything is 0 based indexing and [l,r]
	struct Node {
		int value;
		Node* left;
		Node* right;

		Node(int v = 0, Node* l = nullptr, Node* r = nullptr) {
			value = v;
			left = l;
			right = r;
		}
	};

	int n;
	vector<Node*> versions;

	static int func(int a, int b) {
		return a + b;
	}

	Node* build(int l,int r,vector<int>& data){
		if(l==r) return new Node(data[l]);
		int mid=(l+r)/2;
		Node* left=build(l,mid,data);
		Node* right=build(mid+1,r,data);
		return new Node(func(left->value,right->value),left,right);
	}

	PersistentSegmentTree(vector<int>& data) {
		n = data.size();
		versions.push_back(build(0,n-1,data));
	}

	Node* update(int version, int pos, int value) {
		// Returns the root to the new tree,
		// now you must add it to versions yourself
		// seg.versions[version] = seg.update(version, pos, value)

		function<Node*(Node*,int,int)> dfs = [&](Node* node,int left,int right)->Node*{
			if(left==right){
				int k=value;
				// int k = func(node->value, value); // if i want to update
				return new Node(k);
			}
			int mid=(left+right)/2;
			if(pos<=mid){
				Node* l=dfs(node->left,left,mid);
				return new Node(func(l->value,node->right->value),l,node->right);
			}else{
				Node* r=dfs(node->right,mid+1,right);
				return new Node(func(node->left->value,r->value),node->left,r);
			}
		};

		return dfs(versions[version],0,n-1);
	}

	int create_version(int version, int pos, int value) {
		Node* new_root = update(version, pos, value);
		versions.push_back(new_root);
		return (int)versions.size() - 1;
	}

	int query(int version, int ql, int qr) {
		Node* node = versions[version];

		function<int(Node*,int,int)> dfs = [&](Node* node,int left,int right)->int{
			if(ql>right||qr<left) return 0;
			if(ql<=left&&right<=qr) return node->value;
			int mid=(left+right)/2;
			return func(
				dfs(node->left,left,mid),
				dfs(node->right,mid+1,right)
			);
		};

		return dfs(node,0,n-1);
	}
};
