// not sure if the best way is to devide it into three situations
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
    int n, k;
    cin >> n >> k;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    
    long long total = 0;
    if (k >= 3) {
        sort(arr.begin(), arr.end());
        for (int i = n-1; i >= n-1-k; i--) total += arr[i];
    }
    else if (k == 1) {
        int m1 = 0, m2 = 0;
        for (int i = 0; i < n; i++) {
            if (i < n-1) m1 = max(m1, arr[i]);
            if (i > 0) m2 = max(m2, arr[i]);
        }
        total = max(m1 + arr[n-1], m2 + arr[0]);
    }
    else {
        // use suffix array to store the maximum of right subarray
        vector<int> suffixMax(n);
        int mx = 0;
        for (int i = n-1; i >= 0; i--) {
            mx = max(mx, arr[i]);
            suffixMax[i] = mx;
        }

        mx = arr[0];
        for (int i = 1; i < n-1; i++) {
            // now, mx is the left max, suffixMax[i+1] is the right max
            long long cur = mx + arr[i] + suffixMax[i+1];
            total = max(total, cur);
            mx = max(mx, arr[i]);
        }
        //
        vector<int> a(arr.begin(), arr.begin()+n-1), b(arr.begin()+1, arr.begin()+n);
        sort(a.begin(), a.end());
        sort(b.begin(), b.end());

        total = max({
            (long long)a[n-2]+a[n-3]+arr[n-1], 
            (long long)b[n-2]+b[n-3]+arr[0],
            total
        });
    }
    cout << total << endl;
}


int main() {
    int t;
    cin >> t;
    for (int T = 0; T < t; T++) {
        solve();
    }
}
