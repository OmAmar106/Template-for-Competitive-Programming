template <typename T>
class SortedList {
	ordered_multiset<T> os;
	int uid = 0;
public:
	void insert(T x) {
		os.insert({x, uid++});
	}
	void erase_one(T x) {
		auto it = os.lower_bound({x, 0});
		if (it != os.end() && it->first == x)
			os.erase(it);
	}
	int index(T x) {
		return os.order_of_key({x, 0});
	}
	int count(T x) {
		return os.order_of_key({x, INT_MAX}) - os.order_of_key({x, 0});
	}
	T operator[](int k) {
		return os.find_by_order(k)->first;
	}
	int size() const {
		return os.size();
	}
	void print() {
		for (int i = 0; i < size(); i++) std::cout << (*this)[i] << " ";
		std::cout << "\n";
	}
};