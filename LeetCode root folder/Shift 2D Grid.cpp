// 5%
class Solution {
  public:
      vector<vector<int>> shiftGrid(vector<vector<int>>& grid, int k) {
          int m  = grid.size(), n = grid[0].size();
          deque<int> nums(m*n);
          for (int r = 0; r < m; r++) {
              for (int c = 0; c < n; c++) {
                  int pos = n*r + c;
                  nums[pos] = grid[r][c];
              }
          }
          while (k--) {
              nums.push_front(nums.back());
              nums.pop_back();
          }

          for (int e : nums) cout << e << ' ';
          for (int r = 0; r < m; r++) {
              for (int c = 0; c < n; c++) {
                  int pos = n*r + c;
                  grid[r][c] = nums[pos];
              }
          }
          return grid;
      }
  };