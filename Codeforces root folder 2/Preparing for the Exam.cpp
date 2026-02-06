

#include<iostream>
#include<unordered_map>
#include<unordered_set>
#include<algorithm>
#include<vector>
#include<cmath>
#include<deque>
#include<limits>
using namespace std;




void solve(int n, int m, int k) {
    string res(m, '0');
    if (n > k+1) {
        cout << res << endl;
        return;
    } 

    vector<int> missing;
    unordered_set<int> known;

    for (int i = 0; i < m; i++) {
        int tmp;
        cin >> tmp;
        missing.push_back(tmp);
    }
    for (int i = 0; i < k; i++) {
        int tmp;
        cin >> tmp;
        known.insert(tmp);
    }
    
    for (int i = 0; i < missing.size(); i++) {
        if (known.find(missing[i]) == known.end()) res[i] = '1';
    }
    cout << res << endl;
}

int main() {
    int t;
    cin >> t;
    for (int T = 0; T < t; T++) {
        int n, m, k;
        cin >> n >> m >> k;
        solve(n, m, k);
    }
}


s