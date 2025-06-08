#include<iostream>
#include<unordered_map>
#include<unordered_set>
#include<algorithm>
#include<vector>
#include<cmath>
#include<deque>
#include<limits>
using namespace std;

// the ultimate optimized eratosthene's sieve algorithm! passed
void solve(bool arr[]) {
    int n; cin >> n;
    long res = 0;
    for (int i = 2; i <= n; i++) {
        if (arr[i]) res += n/i;
    }
    cout << res << '\n';
}

int main() {
    const int max_ = 10000001;
    bool arr[max_];
    for (int i = 0; i <= max_; i++) arr[i] = 1;
    arr[0] = arr[1] = 0;
    for (int i = 2; i * i <= max_; i++) {
        if (arr[i] == 1) {
            for (int j = i*i; j <= max_; j+=i) {
                arr[j] = 0;
            }
        }
    }
    int t; cin >> t;
    for (int i = 0; i < t; i++) {
        solve(arr);
    }
}




// after changed it from vector to array, still hitting TLE... why??
void solve(int n, bool arr[]) {
    long res = 0;
    for (int i = 2; i <= n; i++) {
        if (arr[i]) res += n/i;
    }
    cout << res << '\n';
}

int main() {
    int t; cin >> t;
    int max_ = 0;
    int testcases[t];
    for (int i = 0; i < t; i++) {
        cin >> testcases[i];
        max_ = max(max_, testcases[i]);
    }
    bool arr[max_+1];
    for (int i = 0; i <= max_; i++) arr[i] = 1;
    for (int i = 2; i * i <= max_; i++) {
        if (arr[i]) {
            for (int j = i*i; j <= max_; j++) {
                if (j%i == 0) arr[j] = false;
            }
        }
    }
    for (int i = 0; i < t; i++) {
        solve(testcases[i], arr);
    }
}


// this is the best I can do, but it still hit TLE at testcase 9...
void solve(int n, vector<bool> arr) {
    long res = 0;
    for (int i = 2; i <= n; i++) {
        if (arr[i]) res += n/i;
    }
    cout << res << '\n';
}

int main() {
    int t; cin >> t;
    int max_ = 0;
    vector<int> testcases(t);
    for (int i = 0; i < t; i++) {
        cin >> testcases[i];
        max_ = max(max_, testcases[i]);
    }
    vector<bool> arr(max_+1, true);
    for (int i = 2; i * i <= max_; i++) {
        if (arr[i]) {
            for (int j = i*i; j <= max_; j++) {
                if (j%i == 0) arr[j] = false;
            }
        }
    }
    for (int i = 0; i < t; i++) {
        solve(testcases[i], arr);
    }
}



// turns out I fk up the sieve part, I actually only need to test
// factor of up to sqrt(n) to find all the primes in range(n)
void solve() {
    int n; cin >> n;
    vector<int> primes;
    vector<int> cands;
    for (int i = 2; i <= n; i++) cands.push_back(i);
    while (cands.size() != 0) {
        int m = cands.size();
        if (cands[0] * cands[0] > n) break;
        primes.push_back(cands[0]);
        vector<int> tmp;
        for (int i = 1; i < m; i++) {
            if (cands[i] % cands[0] != 0) {
                tmp.push_back(cands[i]);
            }
        }
        cands = tmp;
    }
    for (int c : cands) primes.push_back(c);
    // for (int p : primes) cout << p << ' ';
    long res = 0;
    for (int p : primes) {
        res += n / p;
    }
    cout << res << '\n';
}

int main() {
    int t; cin >> t;
    for (int i = 0; i < t; i++) {
        solve();
    }
}


// to slow...
void solve() {
    int n; cin >> n;
    vector<int> primes;
    vector<int> cands;
    for (int i = 2; i <= n; i++) cands.push_back(i);
    while (cands.size() != 0) {
        int m = cands.size();
        primes.push_back(cands[0]);
        vector<int> tmp;
        for (int i = 1; i < m; i++) {
            if (cands[i] % cands[0] != 0) {
                tmp.push_back(cands[i]);
            }
        }
        cands = tmp;
    }
    // for (int p : primes) cout << p << ' ';
    long res = 0;
    for (int p : primes) {
        res += n / p;
    }
    cout << res << '\n';
}

int main() {
    int t; cin >> t;
    for (int i = 0; i < t; i++) {
        solve();
    }
}


// depcricated
void solve() {
    int n;
    cin >> n;
    vector<int> cands, primes;    
    for (int i = 2; i*i < n; i++) cands.push_back(i);
    while (cands.size() > 0) {
        vector<int> tmp;
        primes.push_back(cands[0]);
        int f = cands[0];
        for (int j = 1; j < cands.size(); j++) {
            if (cands[j] % f != 0) tmp.push_back(cands[j]);
        }
        cands = tmp;
    }
    // for (int p : primes) cout << p << ' ';
    int res = 0;  
    for (int p : primes) {
        int multiple = n / p; // multiple is the number of pairs that match with the prime 'p'
        // these pairs share the form of: (1, 1*p), (2, 2*p), (3, 3*p)
        // obviously, the ratio lcm/gcd of all such pairs are 'p', and 'p' is prime
        // so, all such pairs are of interesting ratio, and 2*p <= n always hold.
        res += multiple;
    }
    cout << res << endl;
}


int main() {
    int t;
    cin >> t;
    for (int T = 0; T < t; T++) {
        solve();
    }
}
