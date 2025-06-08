// 100%
class Solution {
  public:
      int minDeletionSize(vector<string>& strs) {
          int size = strs[0].size();
          vector<char> ref(size, 'a');
          int res = 0;
  
          for (string s : strs) {
              for (int i = 0; i < size; i++) {
                  if (s[i] < ref[i]) {
                      res++;
                      ref[i] = '1';
                  }
                  else if (ref[i] != '1') ref[i] = s[i];
              }
          }
          return res;
      }
  };