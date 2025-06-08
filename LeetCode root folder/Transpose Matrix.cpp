class Solution {
public:
    vector<vector<int>> transpose(vector<vector<int>>& matrix) {
        int row = matrix.size(), col = matrix[0].size();
        vector<vector<int>> res;
        for (int c = 0; c < col; c++) {
            vector<int> tmp;
            res.push_back(tmp);
            for (int r = 0; r < row; r++) {
                int cur = matrix[r][c];
                res[c].push_back(cur);
            }
        }
        return res;
    }
};