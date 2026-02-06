

// depricated
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
    int n, k;
    cin >> n >> k;
    vector<int> left(n), right(n);
    for (int i = 0; i < n; i++) cin >> left[i];
    for (int i = 0; i < n; i++) cin >> right[i];
    sort(left.begin(), left.end(), greater<>());
    sort(right.begin(), right.end(), greater<>());
    int total1 = accumulate(left.begin(), left.end(), 0);
    int total2 = accumulate(right.begin(), right.end(), 0);
    int min1 = 0, min2 = 0;
    for (int i = 0; i < k-1; i++) {
        min1 += left[i];
        min2 += right[i];
    }
    int res = max(total1 + min2, total2 + min1);
    cout << res+1 << endl;

}


int main() {
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        solve();
    }
}

