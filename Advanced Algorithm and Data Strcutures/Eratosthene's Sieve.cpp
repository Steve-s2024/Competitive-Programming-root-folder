#include<vector>
#include<bits/c++io.h>
#include<iostream>
using namespace std;

// this code runs in O(nlog(logn)) time, it is much more optimized than my old code.
void sieve(int n) {
    vector<bool> arr(n+1, true);
    for (int i = 2; i * i <= n; i++) {
        if (arr[i]) {
            for (int j = i*i; j <= n; j+=i) {
                arr[j] = 0;
            }
        }
    }
    for (int i = 2; i  <= n; i++) if (arr[i]) cout << i << ' ';
}

int main() {
    sieve(100);
    sieve(1000);
}
