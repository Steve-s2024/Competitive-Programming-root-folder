#include<iostream>
#include<unordered_map>
#include<algorithm>
using namespace std;
int main() {
  int t;
  cin >> t;
  while (t--) {
    int size;
    cin >> size;
    int arr[size];
    int tar[size];
    for (int i = 0; i < size; i++) {
      cin >> arr[i];
    }
    for (int i = 0; i < size; i++) {
      cin >> tar[i];
    }
    long long totalReduce = 0;
    for (int i = 0; i < size; i++) {
      int reduce = max(tar[i] - arr[i], 0);
      totalReduce += reduce;
    }

    bool valid = true;

    for (int i = 0; i < size; i++) {
      int reduce = max(tar[i] - arr[i], 0);
      long long curVal = max(tar[i], arr[i]) - (totalReduce - reduce);
      if (curVal < tar[i]) {
        valid = false;    
        break;
      }
    }
    if (valid) {
      cout << "YES" << endl;
    }
    else {
      cout << "NO" << endl;
    }
  }
  
}