// tle
class Solution {
  unordered_set<string> visited;
  int row, col;
  vector<vector<int>> matrix;
public:
  int getMaximumGold(vector<vector<int>>& grid) {
      row = grid.size(), col = grid[0].size();
      matrix = grid;
      int res = 0;
      for (int r = 0; r < row; r++) {
          for (int c = 0; c < col; c++) {
              res = max(res, dfs(r, c));
          }
      }
      return res;
  }

  int dfs(int r, int c) {
      string coor = to_string(r) + ',' + to_string(c);
      if (
          (r < 0 || r >= row) ||
          (c < 0 || c >= col) ||
          visited.find(coor) != visited.end() ||
          matrix[r][c] == 0
      ) return 0;

      visited.insert(coor);
      int res = max({dfs(r+1, c), dfs(r-1, c), dfs(r, c+1), dfs(r, c-1)}) + matrix[r][c];
      visited.erase(coor);
      return res;
  } 
};
