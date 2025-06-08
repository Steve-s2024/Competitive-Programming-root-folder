#include<iostream>
using namespace std;
int main() {
  int n;
  cin >> n;
  for (int i = 0; i < n; i++) {
    int res = 0;
    int length;
    string str;
    int count = -1;
    cin >> length;
    cin >> str;
    
    for (int j = 0; j < length; j++) {
      if (str[j] == 'A') {
        res = max(count, res);
        count = 0;
      }
      else if (count != -1) {
        count++;
      }
    }
    cout << max(res, count) << endl;
  }
}