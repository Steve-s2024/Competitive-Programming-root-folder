using namespace std;
class Solution {
  public:
      vector<int> countOfPairs(int n, int x, int y) {
        unordered_map<int, int> map;
        for (int i = 1; i <= n; i++) {
          for (int j = i + 1; j <= n; j++) {
            int minDist = min({
                j - i,
                1 + abs(i - x) + abs(j - y),
                1 + abs(j - x) + abs(i - y)
          });
            map[minDist] += 2;
          }
        }
        vector<int> ans(n, 0);
        for (int i = 0; i < n; i++) {
          ans[i] = (map[i+1]);
        }
        return ans;
      }
  };