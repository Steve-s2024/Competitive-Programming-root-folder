// TLE
#include<bits/stdc++.h>
using namespace std;

void solve() {
    int n; cin >> n;
    int nums[n];
    for (int i = 0; i < n; i++) cin >> nums[i];

    unordered_map<long long, int> mp;
    mp[0] = 1;
    deque<long long> prefix;
    prefix.push_back(0);
    int res = 0;
    long long total = 0;

    for (int num : nums) 
    {
        total += (long long)num;
        if (mp.find(total) != mp.end()) 
        {
            res++;
            while (prefix.size()) {
                long long cur = prefix.front();
                prefix.pop_front();
                mp[cur]--;
                if (mp[cur] == 0) mp.erase(cur);
            }
        }
        mp[total]++;
        prefix.push_back(total);
    }
    cout << res << endl;
}


int main() {
    cin.tie(nullptr);
    int t; cin >> t;
    for (int i = 0; i < t; i++) {
        solve();
    }
}
