// solution:0
//ms
//Beats
//100.00%
//second question of the c++ easy questions marathon
class Solution {
public:
    vector<vector<int>> flipAndInvertImage(vector<vector<int>>& image) {
        int row = image.size(), col = image[0].size();
        vector<vector<int>> res;
        for (int r = 0; r < row; r++) {
            vector<int> curRow;
            res.push_back(curRow);
            for (int c = 0; c < col; c++) {
                int curCell = (image[r][col-c-1] + 1) % 2;
                res[r].push_back(curCell);
            }
        }
        return res;
    }
};