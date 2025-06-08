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
    int x, k;
    cin >> x >> k;

    if (k == 1 && x == 1) cout << "NO" << endl;
    else if (k == 1) {
        bool flag = true;
        int f = 2;
        while (f*f <= x) {
            if (x%f == 0) flag = false;
            f++;
        }
        if (flag) cout << "YES" << endl;
        else cout << "NO" << endl;

    }
    else if (x == 1) {
        int n = 0;
        for (int i = 0; i < k; i++) {
            n*= 10;
            n++;
        }

        int f = 2;
        bool flag = true;
        while (f*f <= n) {
            if (n%f == 0) flag = false;
            f++;
        }
        if (flag) cout << "YES" << endl;
        else cout << "NO" << endl;
    }
    else cout << "NO" << endl;
}


int main() {
    int t;
    cin >> t;
    for (int T = 0; T < t; T++) {
        solve();
    }
}
