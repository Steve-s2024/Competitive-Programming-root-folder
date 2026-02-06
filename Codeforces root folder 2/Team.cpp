#include<iostream>
using namespace std;
int main() {
  int n, count, cur;
  int res = 0;
  cin >> n;
  for (int i = 0; i < n; i++) {
    count = 0;
    for (int j = 0; j < 3; j++) {
      cin >> cur;
      count += cur;
    }
    if (count >= 2) {
      res++;
    }
  }
  cout << res << endl;
}