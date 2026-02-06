// interactive question, binary search guessing game
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




int main() {
    string sign;
    int l = 1, r = 1000000;
    int res = l;
    // cout << 1 << endl;
    while (l <= r) {
        int m = (l+r) / 2;
        cout << m << endl;
        cin >> sign;
        if (sign == ">=") {
            res = max(res, m);
            l = m+1;
        }
        else r = m-1;
    }
    // printf("! %d %n", res);
    cout << "! " << res << endl;
}


