// the first question on codeforces
#include<iostream>
#include<unordered_map>
#include<unordered_set>
#include<algorithm>
#include<vector>
#include<cmath>
#include<deque>
#include<limits>
#include<cstdio>
#include<numeric>
using namespace std;

int main() {
    cin.tie(nullptr);
    long long n, m, a; cin >> n >> m >> a;
    long long l = ceil((double)m / a), w = ceil((double)n / a);
    cout << l * w << endl;
}
