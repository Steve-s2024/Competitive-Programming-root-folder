// TLE on tc.4
#include<bits/stdc++.h>
using namespace std;

void solve() {
    int n, m, L; cin >> n >> m >> L;
    vector<pair<int, int>> intervals;
    unordered_map<int, vector<int>> mp;
    
    for (int i = 0; i < n; i++) {
        pair<int, int> tmp; cin >> tmp.first >> tmp.second;
        intervals.push_back(tmp);
    }
    if (intervals.size() && intervals[0].first == 1) {
        cout << -1 << '\n';
        return;
    }
    
    for (int i = 0; i < m; i++) {
        int pos, bst; cin >> pos >> bst;
        mp[pos].push_back(bst);
    }
    
    priority_queue<int> maxHeap;
    bool flag = 1;
    int i = 1;
    int j = 0;
    int jump = 1;
    int res = 0;
    while (i <= L) {
        if (j < n && i == intervals[j].first) {
            int gap = intervals[j].second-intervals[j].first+2;
            while (maxHeap.size() && jump < gap) {
                res++;
                jump += maxHeap.top();
                maxHeap.pop();
            }
            if (jump < gap) {
                flag = 0;
                break;
            }
            i = intervals[j].second+1;
            j++;
        }
        if (mp.find(i) != mp.end()) {
            for (int num : mp[i]) {
                maxHeap.push(num);
            }
        }
        i++;
    }
    if (flag) cout << res << '\n';
    else cout << -1 << '\n';
}


int main() {
    cin.tie(nullptr);
    int t; cin >> t;
    for (int i = 0; i < t; i++) {
        solve();
    }
}
