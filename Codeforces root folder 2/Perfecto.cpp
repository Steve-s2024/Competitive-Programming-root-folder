// boring question...
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
    long long n;
    cin >> n;
    long long total = n*(n+1)/2;
    
    // cout << sqrt(total) << ' ' << (int)sqrt(total) << endl;
    if (sqrt(total) == (int)sqrt(total)) {
        cout << -1 << endl;
    }
    else {
        total = 0;
        long long i = 1;
        while (i <= n) {
            if (sqrt(total+i) == (int)sqrt(total+i)) {
                cout << i+1 << ' ' << i << ' ';
                total += i+i+1; 
                i+=2; 
            }
            else {
                cout << i << ' ';
                total += i; 
                i++;
            }
        }
        cout << endl;
    }
}


int main() {
    int t;
    cin >> t;
    for (int T = 0; T < t; T++) {
        solve();
    }
}
