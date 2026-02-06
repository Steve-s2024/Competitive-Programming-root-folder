#include<bits/stdc++.h>
// #include<algorithm>
using namespace std;

void solve() {
    int n, k; cin >> n >> k;
    int nums[n];
    unordered_map<int, int> mp;
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
        mp[nums[i]]++;
    }
    vector<int> keys;
    for (auto p : mp) keys.push_back(p.first);
    sort(keys.begin(), keys.end());
     
    int m = keys.size();
    long long res = 0;
    deque<int> q;
    long long total = 0;
    for (int i = 0; i < m; i++) {
        int cur = mp[keys[i]];
        total += cur;
        q.push_back(cur);
        res = max(res, total);

        if (i < m-1 && keys[i+1] != keys[i]+1) {
            total = 0;
            q.clear();
        }
        if (q.size() == k) {
            total -= q.front();
            q.pop_front();
        }

    }
    cout << res << endl;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t; cin >> t;
    for (int i = 0; i < t; i++) {
        solve();
    }
}
