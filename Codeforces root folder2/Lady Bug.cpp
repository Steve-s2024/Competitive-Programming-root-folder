

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
    string a, b;
    cin >> size;
    cin >> a >> b;

    int odd = 0, even = 0;
    
    for (int i = 0; i < size; i++) {
        if (a[i] == '1') {
            if ((i+1)%2 == 1) odd++;
            else even++;
        }
        if (b[i] == '0') {
            if ((i+1)%2 == 1) even--;
            else odd--;
        }
    }

    if (odd <= 0 && even <= 0) cout << "YES" << endl;
    else cout << "NO" << endl;
}

int main() {
    int t;
    cin >> t;
    for (int T = 0; T < t; T++) {
        solve();
    }
}
