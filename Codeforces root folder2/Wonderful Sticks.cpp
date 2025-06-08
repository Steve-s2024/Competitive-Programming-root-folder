#include<iostream>
#include<unordered_map>
#include<unordered_set>
#include<algorithm>
#include<vector>
#include<cmath>
#include<deque>
#include<limits>
#include<cstdio>
using namespace std;


void solve() {
    int n;
    cin >> n;
    vector<int> ans;
    string s;
    cin >> s;
    ans.push_back(1);
    int max_ = 1, min_ = 1;
    for (char c : s) {
        if (c == '<') {
            min_--;
            ans.push_back(min_);
        }
        else {
            max_++;
            ans.push_back(max_);
        }
    }
    int incre = -min_+1;
    for (int i = 0; i < ans.size(); i++) {
        ans[i] += incre;
    }
    for (int num : ans) cout << num << ' ';
    cout << endl;
}


int main() {
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        solve();
    }
}

