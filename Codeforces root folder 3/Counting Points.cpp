// weird run time complexity, can't tell for sure 
// what complexity this is, but it passed anyway
// also the question clearly reappeared in the AtCoder 
// contest a few weeks later...

#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;

void solve() {
    ll n, m; cin >> n >> m;
    int nums[n];
    int radii[n];
    for (int i = 0; i < n; i++) cin >> nums[i];
    for (int i = 0; i < n; i++) cin >> radii[i];

    unordered_map<int, int> mp;
    for (int i = 0; i < n; i++) {
        int cent = nums[i], radi = radii[i];
        for (int j = cent-radi; j <= cent+radi; j++) {
            int tmp = 2*(int)sqrt(pow(radi, 2) -pow(cent-j, 2)) +1;
            mp[j] = max(mp[j], tmp);
        }
    }
    ll tot = 0;
    for (auto p : mp) tot += p.second;
    cout << tot << endl;
}


int main() {
    cin.tie(nullptr);
    int t; cin >> t;
    for (int i = 0; i < t; i++) {
        solve();
    }
}
