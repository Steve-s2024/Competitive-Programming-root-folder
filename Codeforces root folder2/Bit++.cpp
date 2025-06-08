#include<iostream>
using namespace std;
int main() {
  int n;
  cin >> n;
  int num = 0;
  string cur;
  for (int i = 0; i < n; i++) {
    cin >> cur;
    if (cur[1] == '+') {
      num++;
    } 
    else {
      num--;
    }
  }
  cout << num << endl;
}