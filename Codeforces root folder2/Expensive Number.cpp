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
    string s = to_string(n);
    int res = 0;
    int tracingZero = 0;
    int i = s.size()-1;
    for (; i >= 0; i--) {
        if (s[i] != '0') break;
        tracingZero++;
    }
    for (;i >= 0; i--) {
        if (s[i] != '0') res++;
    }
    cout << tracingZero+res-1 << endl;
}


int main() {
    int t;
    cin >> t;
    for (int T = 0; T < t; T++) {
        solve();
    }
}
