#include <bits/stdc++.h>
using namespace std;

void solve() {
  int n;
  cin >> n;
  int a;
  int res = 0;
  for (int i = 0; i < n; i++) {
    cin >> a;
    res += a-1;
  }
  cout << res << endl;
}

int main() {
  int t;
  cin >> t;
  for (int i = 0; i < t; i++) {
    solve();
  }
}

