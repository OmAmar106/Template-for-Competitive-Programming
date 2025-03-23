// #include <ctime>
// #include <iostream>
// #include <unordered_map>
// using namespace std;

// const int N = 2e5;

// void insert_numbers(long long x) {
//     clock_t begin = clock();
//     unordered_map<long long, int> numbers;

//     for (int i = 1; i <= N; i++)
//         numbers[i * x] = i;

//     printf("x = %lld: %.3lf seconds\n", x, (double) (clock() - begin) / CLOCKS_PER_SEC);
// }

// int main() {
//     insert_numbers(107897);
// }


#include <bits/stdc++.h>
#include <fstream>
#include <iostream>
using namespace std;
int main() {
    constexpr int N = 2e5;
    cout << "1\n" << N <<"\n";
    uint32_t x = 107897;
    for(int i=1;i<=N;i++){
        cout<<x*i;
        if(i!=N){
            cout<<" ";
        }
    }
    cout << "\n";
    // cout.close();
}