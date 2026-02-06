

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
    int size;
    long long res = 0;
    int max_ = 0;
    bool flag1 = false, flag2 = false;
    cin >> size;
    for (int i = 0; i < size; i++) {
        int cur;
        cin >> cur;
        res += cur;
        max_ = max(max_, cur);
        if (cur % 2 == 1) {
            flag1 = true;
            res--;
        }
        else {
            flag2 = true;
        }
    }
    if (flag1 && flag2) cout << (res+1) << endl;
    else cout << max_ << endl;
}


int main() {
    int t;
    cin >> t;
    for (int T = 0; T < t; T++) {
        solve();
    }
}

