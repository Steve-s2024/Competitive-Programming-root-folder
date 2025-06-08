// cpp ten times faster than python again
#include<bits/stdc++.h>
using namespace std;

void solve() {
    int n; cin >> n;
    unordered_map<int, int> mp;     
    for (int i = 0; i < n; i++) {
        int input; cin >> input;
        mp[input]++;
    }

    vector<int> keys;
    for (auto p : mp) keys.push_back(p.first);
    sort(keys.begin(), keys.end());

    int flag = 4;
    int prev = keys[0]-1;
    for (int key : keys) {
        if (prev+1 != key) flag = 4;
        int val = mp[key];
        if (val == 3 || val == 2) {
            flag /= 2;
        }
        else if (val >= 4) {
            flag = 1;
        }

        if (flag == 1) break;
        prev = key;
    }

    if (flag == 1) cout << "Yes" << endl;
    else cout << "No" << endl; 
}


int main() {
    cin.tie(nullptr);
    int t; cin >> t;
    for (int i = 0; i < t; i++) {
        solve();
    }
}
