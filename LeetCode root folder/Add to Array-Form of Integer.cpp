// 100%
class Solution {
  public:
      vector<int> addToArrayForm(vector<int>& num, int k) {
          vector<int> ds;
          string str = to_string(k);
          for (int i = 0; i < str.size(); i++) ds.push_back(str[i]-'0');
          
          deque<int> res;
          for (int n : num) res.push_back(n);
          for (int i = ds.size()-1; i >= 0; i--) {
              int d = ds[i];
              int comp = ds.size()-1-i;
              if (comp >= res.size()) res.push_front(0);
              int size = res.size();
              int total = res[size-1-comp] + d;
              int carry = total / 10, remain = total % 10;
              res[size-1-comp] = remain;
              for (int j = size-2-comp; j >= 0; j--) {
                  if (carry == 0) break;
                  total = res[j] + carry;
                  carry = total / 10, remain = total % 10;
                  res[j] = remain;
              }
              if (carry == 1) res.push_front(1);
          }
          vector<int> ans(res.begin(), res.end());
          return ans;
      }
  };