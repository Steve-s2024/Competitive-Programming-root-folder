#include<iostream>
using namespace std;

int main() {
  int n;
  cin >> n;
  for (int i = 0; i < n; i++ ) {
    int total = 0;
    int tmp;
    for (int j = 0; j < 3; j++) {
      cin >> tmp;
      total += tmp;
    }
    tmp = (2*total) % 3;
    if (tmp > 0) {
      cout << 1 << endl;
    }
    else {
      cout << 0 << endl;
    }
  }
}