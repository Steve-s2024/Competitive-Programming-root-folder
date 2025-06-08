#include<iostream>
using namespace std;


void solve(int n, int m, int k, string s) {
    int cnt = 0, i = 0, res = 0;
    while (i < s.size()) {
        char c = s[i];
        if (c == '0') {
            cnt++;
            if (cnt >= m) {
                res++;
                i += k;
                cnt = 0;  
                i--;
            }
        }
        else cnt = 0;
        i++;
    }
    cout << res << endl;
}

int main() {
    int t;
    cin >> t;
    for (int T = 0; T < t; T++) {
        int n, m, k;
        string s;

        cin >> n >> m >> k >> s;
        solve(n, m, k, s);
    }
}
