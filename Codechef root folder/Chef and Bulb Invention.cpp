#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n, p, k;
    cin >> n >> p >> k;
    n--;
    int multiple = n / k, remain = n % k;
    int tar = p%k;
    int res = min(tar, remain+1) * (multiple+1) + max(tar-remain-1, 0) * multiple + (p/k+1);
    cout << res << endl;
}

int main() {
	// your code goes here
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        solve();
    }
}
