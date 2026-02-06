// fking 100ms while python hit TLE at tc4 with 2000ms
#include<iostream>
#include<unordered_map>
#include<unordered_set>
#include<algorithm>
#include<vector>
#include<cmath>
#include<deque>
#include<limits>
#include<cstdio>
#include<numeric>
using namespace std;

void solve() {
    long long k, l1, r1, l2, r2; cin >> k >> l1 >> r1 >> l2 >> r2;
    long long res = 0, tar = 1;
    while (l1*tar <= r2) {
        // cout << l1 << ' ' << tar << ' ' << r2 << endl;
        int left = -1, right = -1;
        int l = l1, r = r1;
        while (l <= r) {
            int m = floor((l+r)/2);
            if (m*tar > r2) {
                r = m-1;
            }
            else {
                right = m;
                l = m+1;
            }
        }
        l = l1, r = r1;
        while (l <= r) {
            int m = floor((l+r)/2);
            if (m*tar < l2) {
                l = m+1;
            }
            else{
                left = m;
                r = m-1;
            }
        }
        tar *= k;
        if (left != -1 && right != -1) {
            res += right - left + 1;
        }
    }
    cout << res << '\n';
}


int main() {
    cin.tie(nullptr);
    int t; cin >> t;
    for (int i = 0; i < t; i++) {
        solve();
    }
}
