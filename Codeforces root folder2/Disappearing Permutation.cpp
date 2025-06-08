

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
    int n;
    cin >> n;
    vector<int> nums(n), queries(n);
    for (int i = 0; i < n; i++) cin >> nums[i];
    for (int i = 0; i < n; i++) cin >> queries[i];

    unordered_map<int, int> hashMap;
    for (int i = 0; i < n; i++) {
        hashMap[nums[i]] = i;
    }

    int cnt = 0;
    unordered_set<int> visited;
    for (int q : queries) {
        int idx = q-1;
        while (visited.find(idx) == visited.end()) {
            visited.insert(idx);
            idx = hashMap[idx+1];
            cnt++;
        }
        cout << cnt << ' ';
    }
    cout << endl;
}


int main() {
    int t;
    cin >> t;
    for (int T = 0; T < t; T++) {
        solve();
    }
}
