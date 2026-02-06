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
    string p, s;
    cin >> p >> s;
    int n = p.size(), m = s.size();
    int i1 = 0, i2 = 0;
    bool flag = true;
    while (i1 < n && i2 < m) {
        int r1 = i1, r2 = i2;
        while (r1 < n && p[r1] == p[i1]) r1++;
        while (r2 < m && s[r2] == s[i2]) r2++;
        if (
            p[i1] != s[i2] ||
            (r1-i1)*2 < r2-i2 ||
            r1-i1 > r2-i2 
        ) {
            flag = false;
            break;
        }
        if (flag == false) break;
        i1 = r1;
        i2 = r2;
    }
    if (flag && i1 == n && i2 == m) cout << "YES" << '\n';
    else cout << "NO" << '\n';
    cout.flush();
}


int main() {
    int t;
    cin >> t;
    for (int T = 0; T < t; T++) {
        solve();
    }
}
