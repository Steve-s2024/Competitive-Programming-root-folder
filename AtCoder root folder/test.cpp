#include<iostream>
#include<deque>
#include<unordered_map>
#include<unordered_set>
#include<bits/c++io.h>
#include <vector>
using namespace std;



int recursive(int i, int x, int n, int *arr, int *brr, int *prr, int dp[][500]) {
    if (dp[i][x] != -1) return dp[i][x];
    if (i >= n) return x;
    if (prr[i] < x) x -= min(x, brr[i]);
    else x += arr[i];
    int res = recursive(i+1, x, n, arr, brr, prr, dp);
    dp[i][x] = res;
    return res;
}


void solve() {
    int n;
    cin >> n;
    const int mx = 500;
    int prr[n], arr[n], brr[n];
    for (int i = 0; i < n; i++) {
        cin >> prr[i] >> arr[i] >> brr[i];
    }

    int pre[n];
    int tot = 0;
    for (int i = 0; i < n; i++) {
        tot += brr[i];
        pre[i] = tot;
    }

    int dp[n][mx];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < mx; j++) {
            dp[i][j] = -1;
        }
    }

    int q;
    cin >> q;
    for (int i = 0; i < q; i++) {
        int x;
        cin >> x;
        int l = 0, r = n-1;
        int res = 0;
        while (l <= r) {
            int m = (l+r)/2;
            if (x - pre[m] <= mx) {
                res = m;
                r = m-1;
            }
            else l = m+1;
        }
        // cout << x << endl;
        if (!(x <= mx)) x -= min(x, pre[res]);
        else res = -1;
        // cout << res << ' ' << x << endl;
        int ans = recursive(res+1, x, n, arr, brr, prr, dp);
        // cout << ans << endl;
    }
}


int main() {
    solve();
}