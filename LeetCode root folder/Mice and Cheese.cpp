//greedy solution: 89%

class Solution {
  public:
      int miceAndCheese(vector<int>& reward1, vector<int>& reward2, int k) {
          vector<int> diffs;
          int diff, res = 0, size = reward1.size();
          for (int i = 0; i < size; i++) {
              diff = reward1[i] - reward2[i];
              diffs.push_back(diff);
          }
          sort(diffs.begin(), diffs.end());
          for (int i = size-1; i >= size-k; i--) res += diffs[i];
          res += accumulate(reward2.begin(), reward2.end(), 0);
          return res;
      }
  };