// interesting question, teaches you how to view a problem the 
// way its most comfortable. problem solving skill (look at problems
// in different ways)
#include<iostream>
#include<unordered_map>
#include<unordered_set>
#include<algorithm>
#include<vector>
#include<cmath>
#include<deque>
#include<limits>
#include<cstdio>
#include<numeric>
using namespace std;


void solve() {
    int n, m; cin >> n >> m;
    int grid[n][m];
    for (int r = 0; r < n; r++) {
        for (int c = 0; c < m; c++) {
            cin >> grid[r][c];
        }
    }
    unordered_map<int, int> mp;
    for (int r = 0; r < n; r++) {
        for (int c = 0; c < m; c++) {
            int val = grid[r][c];
            int coors[4][2] = {{r, c+1}, {r, c-1}, {r+1, c}, {r-1, c}};
            for (auto& coor : coors) {
                int R = coor[0], C = coor[1];
                if (R >= 0 and R < n and C >= 0 and C < m and grid[R][C] == val) mp[val] = 2;
                if (mp.find(val) == mp.end()) mp[val] = 1;
            }
        }
    }
    int res = 0;
    int maximum = 0;
    for (auto& entry : mp) {
        res += entry.second;
        maximum = max(maximum, entry.second);
    }    
    cout << res - maximum << endl;
}

int main() {
    int t; cin >> t;
    for (int i = 0; i < t; i++) {
        solve();
    }
}
