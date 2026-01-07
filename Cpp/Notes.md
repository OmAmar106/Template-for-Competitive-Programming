# How to convert a Python Code to CPP Guide

1. Rather than Sorted List, use OrderedMultiset
2. Keep in mind of integer overflow and weird stuff like that
3. Learn more stuff about more ds from cpp
4. To store more two value, use pair for more than that use tuple
5. if you iterate , to access the variable use .f, .s
6. If more than that, use get<num>(tuple)
7. To sort using a custom function, add a third parameter [](const auto& a,const auto& b){return get<2>(a)<get<2>(b);}
8. To initialize a 2-D vector with all zeroes, use vector<vector<int>> dp(n,vector<int>(m,0)); 
9. Rather than heap, priority queue.
10. pop does not return any value, first peek then pop.
11. C++ 17 allows &[a,b,c].
12. Use emplace_back rather than push_back to push complicated structures.
13. print will work the same way in python now.
14. Multiset can be used in many place, but OrderedMultiSet is better personally.
15. Min Heap: priority_queue<pi,vector<pi>,greater<pi>> pq;
16. int val = *max_element(L.begin(),L.end());
17. Inline Function:
    auto func_name = [](int a,int b){
        return a*b;
    };
18. __builtin_popcount(m) : popcount of the number

n. Be happy with your faster code :) 