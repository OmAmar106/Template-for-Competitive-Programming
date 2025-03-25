# How to convert a Python Code to CPP Guide

1. Rather than Sorted List, use Multiset or OrderedSet
2. Keep in mind of integer overflow and weird stuff like that
3. Learn more stuff about more ds from cpp
4. To store more two value, use pair for more than that use tuple
5. if you iterate , to access the variable use .first, .second
6. If more than that, use get<num>(tuple)
7. To sort using a custom function, add a third parameter [](const auto& a,const auto& b){return get<2>(a)<get<2>(b)>}
n. Be happy with your faster code :) 