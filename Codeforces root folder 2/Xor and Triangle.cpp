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
    int x, n;
    cin >> x;
    n = x;
    int zeroCnt = 0;

    string s = "";
    while (n > 0) {
        int r = n % 2;
        // cout << r;
        s += to_string(r);
        n -= r;
        n /= 2;
        if (r == 0) zeroCnt++;
    }
    // cout << endl;
    // cout << s << endl;

    if (zeroCnt == 0) cout << -1 << endl;
    else {
        int y = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == '1') {
                y += pow(2, i);
                break;
            }
        }
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == '0') {
                y += pow(2, i);
                break;
            }
        }
        if (y > x) cout << -1 << endl;  
        else cout << y << endl;
    }
}


int main() {
    int t;
    cin >> t;
    for (int T = 0; T < t; T++) {
        solve();
    }
}
