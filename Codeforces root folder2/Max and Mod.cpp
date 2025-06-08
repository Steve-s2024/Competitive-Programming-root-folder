#include<iostream>
#include<unordered_map>
#include<unordered_set>
#include<algorithm>
#include<vector>
#include<cmath>
#include<deque>
#include<limits>
using namespace std;


void solve() {
    int n;
    cin >> n;
    if (n%2 == 0) {
        cout << -1 << endl; 
    }
    else {
        cout << n << ' ';
        for (int i = 1; i < n; i++) {
            cout << i << ' ';
        }
        cout << endl;
    }
}


int main() {
    int t;
    cin >> t;
    for (int T = 0; T < t; T++) {
        solve();
    }
}
