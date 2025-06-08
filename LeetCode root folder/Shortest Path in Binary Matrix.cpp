//bfs solution:1258
//ms
//Beats
//5.01%
class Solution {
  public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        if (grid[0][0] == 1) {
            return -1;
        }
        int minLen = 1;
        deque<vector<int>> q = {{0, 0}};
        int row = grid.size();
        int col = grid[0].size();
        unordered_set<string> visited;
        visited.insert("0,0");
        while (q.size() > 0) {
            int l = q.size();
            while (l > 0) {
            vector<int> cur = q.front();
            int r = cur[0];
            int c = cur[1];
            q.pop_front();
            if (r == row-1 && c == col-1) {
                return minLen;
            }

            vector<vector<int>> nextCoors = {{r+1, c}, {r+1, c+1}, {r, c+1}, {r-1, c+1}, {r-1, c}, {r-1, c-1}, {r, c-1}, {r+1, c-1}};
            for (vector<int> e : nextCoors) {
                int R = e[0];
                int C = e[1];
                string coor = to_string(R) +  ',' + to_string(C);
                if (
                (R >= 0 && R < row) &&
                (C >= 0 && C < col) &&
                (visited.find(coor) == visited.end()) &&
                grid[R][C] != 1
                ) {
                visited.insert(coor);
                q.push_back({R, C});
                }
            }
            l -= 1;
            }
            minLen++;
        }
        return -1;
    }
};
