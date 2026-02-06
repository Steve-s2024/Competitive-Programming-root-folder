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
    int n, m, l, r;
    cin >> n >> m >> l >> r;
    int L = -min(abs(m), abs(l));
    int R = min(m+L, r);
    cout << L << ' ' << R << endl;

}


int main() {
    int t;
    cin >> t;
    for (int T = 0; T < t; T++) {
        solve();
    }
}
