//dp solution:0
//ms
//Beats
//100.00%

class Solution {
public:
	int minPathCost(vector<vector<int>>& grid, vector<vector<int>>& moveCost) {
		int m = grid.size();
		int n = grid[0].size();
		vector<int> dp = grid[m-1];
		for (int i = m-2; i >= 0; i--) {
			vector<int> tmp;
			for (int j = 0; j < n; j++) {
				int minCost = moveCost[grid[i][j]][0] + dp[0];
				for (int k = 0; k < n; k++) {
					int curCost = moveCost[grid[i][j]][k] + dp[k];
					minCost = min(minCost, curCost);
				}
				tmp.push_back(minCost + grid[i][j]);
			}
			dp = tmp;
		}
		return *min_element(dp.begin(), dp.end());
	}
};
