// 100%
class Solution {
  public:
      vector<int> diStringMatch(string s) {
          vector<int> ans;
          int n = s.size()+1;
          int cnt = 0;
          for (char c : s) {
              if (c == 'I') {
                  cnt++;
              }
              else {
                  for (int i = n - cnt; i <= n; i++) ans.push_back(i-1);
                  n -= cnt+1;
                  cnt = 0;
              }
          }
          for (int i = n - cnt; i <= n; i++) ans.push_back(i-1);
          return ans;
      }
  };