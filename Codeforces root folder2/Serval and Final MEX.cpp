

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
    deque<int> nums(n);
    for (int i = 0; i < n; i++) cin >> nums[i];        

    vector<pair<int, int>> ans;
    int length = n;
    if (nums[0] == 0) {
        ans.push_back({1, 2});
        length--;
        nums.pop_front();
        nums.pop_front();
    }
    if (nums[nums.size()-1] == 0) {
        ans.push_back({length-1, length});
        length--;
        nums.pop_back();
        nums.pop_back();
    }
    bool flag = true;
    for (int i = 0; i < nums.size(); i++) {
        if (nums[i] == 0) {
            flag = false;
            break;
        }
    }

    if (flag) ans.push_back({1, length});
    else {
        ans.push_back({1, length-1});
        ans.push_back({1, 2});
    }

    cout << ans.size() << endl;
    for (pair<int, int> p : ans) {
        cout << p.first << " " << p.second << endl;
    }
}


int main() {
    int t;
    cin >> t;
    for (int T = 0; T < t; T++) {
        solve();
    }
}
