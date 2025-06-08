// 600th LeetCode question!!
class Solution {
public:
	int surfaceArea(vector<vector<int>>& grid) {
        int length = grid.size();
        int totalSurfaceArea = 0;
        int validCount = 0;

        for (int r = 0; r < length; r++) {
            for (int c = 0; c < length; c++) {
                vector<pair<int, int>> surrounding = {{r+1, c},{r-1, c},{r, c+1},{r, c-1}};
                for (pair<int, int> p : surrounding) {
                    int R = p.first, C = p.second;
                    if (
                        (R >= 0 && R < length) &&
                        (C >= 0 && C < length)
                    ) {
                        totalSurfaceArea += max(0, grid[R][C] - grid[r][c]);
                    }
                    else totalSurfaceArea += grid[r][c];
                }
                if (grid[r][c] != 0) validCount++;
            }
        }
        return totalSurfaceArea + 2 * validCount;
	}
};