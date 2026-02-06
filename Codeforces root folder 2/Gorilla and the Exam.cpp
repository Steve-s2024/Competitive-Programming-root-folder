#include<iostream>
#include<unordered_map>
#include<algorithm>
using namespace std;
// tle on testcase 19
void solve() {
    int n, k; cin >> n >> k;
    int nums[n];
    unordered_map<int, int> mp;
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
        mp[nums[i]]++;
    }
    vector<int> vals(mp.size());
    int i = 0;
    for (auto p : mp) {
        vals[i] = p.second;
        i++;
    }
    sort(vals.begin(), vals.end());
    i = 0;
    int total = 0;
    int m = vals.size();
    while (i < m && total + vals[i] <= k) {
        total += vals[i];
        i++;
    }
    cout << max(m-i, 1) << '\n';
}

int main() {
    int t; cin >> t;
    for (int i = 0; i < t; i++) {
        solve();
    }
}



// solution no.1, brute force hashmap: tle

int main() {
  int t;
  cin >> t;
  while (t--) {
    int size, k;
    cin >> size >> k;
    unordered_map<int, int> map;
    for (int i = 0; i < size; i++) {
      int key;
      cin >> key;
      if (map.find(key) == map.end()) {
        map[key] = 0;
      }
      map[key]++;
    }
    int arr[map.size()];
    int i = 0;
    for (const auto& p : map) {
      arr[i] = p.second;
      i++;
    }
    int arrSize = (sizeof(arr) / sizeof(arr[0]));
    sort(arr, arr + arrSize);
    int ans = arrSize;
    for (int e : arr) {
      // cout << e << endl;
      k -= e;
      if (k < 0) {
        break;
      }
      ans--;
    }
    ans = max(ans, 1);
    cout << ans << endl;

  }
  
}


// solution no.2: tle on testcase 14 (the solution is solid, but the c++ code can be optimized with c++ tricks, which idk how)

void solve() {
  int n, k;
  cin >> n >> k;
  int cur;
  unordered_map<int, int> frq;
  for (int i = 0; i < n; i++) {
      cin >> cur;
      frq[cur]++;
  }
  vector<int> frqArr;
  for (pair<int, int> p : frq) frqArr.push_back(p.second);
  sort(frqArr.begin(), frqArr.end());
  int res = frqArr.size();
  for (int num : frqArr) {
      if (k >= num) {
          k -= num;
          res--;
      }
      else break;
  }
  res = max(res, 1);
  cout << res << endl;
}


int main() {
  int t;
  cin >> t;
  for (int T = 0; T < t; T++) {
      solve();
  }
}