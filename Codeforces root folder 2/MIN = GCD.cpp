// fk up question! way too hard. I some how manage to sovle it, finally!😢
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
    vector<long long> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    // vector<long long> a = {998244359987710471, 99824435698771045, 1000000007};

    sort(a.begin(), a.end());
    vector<long long> multiples;
    vector<long long> prev;
    bool flag = false;

    for (int i = 1; i < n; i++) {
        if (a[i] % a[0] == 0) {
            vector<long long> factors;
            int f = 2;
            long long num = a[i] / a[0];
            long long limit = num;
             
            // factoring the 'num'
            while (pow(f, 2) <= limit) {
                while (num % f == 0) {
                    factors.push_back(f);
                    num /= f;
                }
                f++;
            }
            if (num != 1) factors.push_back(num);
            
            // find overlap factors
            if (flag) {
                vector<long long> tmp;
                int i1 = 0, i2 = 0;
                while (i1 < factors.size() && i2 < prev.size()) {
                    if (factors[i1] == prev[i2]) {
                        tmp.push_back(factors[i1]);
                        i1++;
                        i2++;
                    }
                    else if (factors[i1] < prev[i2]) i1++;
                    else i2++;
                }
                prev = tmp;
            }
            else {
                prev = factors;
                flag = true;
            }
        }   
    }
    if (prev.size() == 0 && flag) cout << "YES" << endl;
    else cout << "NO" << endl;

}


int main() {
    int t;
    cin >> t;
    for (int T = 0; T < t; T++) {
        solve();
    }
}

