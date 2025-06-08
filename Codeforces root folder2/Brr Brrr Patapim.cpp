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

    unordered_set<int> set;
    vector<int> perm(2*n);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> perm[i+j+1];
            set.insert(perm[i+j+1]);
        }
    }
    for (int i = 1; i <= 2*n; i++) {
        if (set.find(i) == set.end()) {
            perm[0] = i;
            break;
        }
    }
    for (int num : perm) cout << num << ' ';
    cout << endl;
}


int main() {
    int t;
    cin >> t;
    for (int T = 0; T < t; T++) {
        solve();
    }
}
