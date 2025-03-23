#include <bits/stdc++.h>
#include <fstream>
#include <iostream>
using namespace std;
int main() {
    constexpr uint32_t mask = (1 << 16) - 1;
    constexpr int N = 2e5, prefill = (1 << 15) + 1;
    // fstream cout;
    // cout.open("samples.txt");
    cout << "1\n" << N <<"\n";
    cout << mask + 1;
    uint32_t x = 1;
    for (int i = 1; i < prefill; ++i) {
        cout << " " << x;
        x = x * 5 + 1;
        x &= mask;
    }
    for (int i = prefill; i < N; ++i) {
        cout << " 0";
    }
    cout << "\n";
    // cout.close();
}