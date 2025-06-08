//simulation solution:0
//ms
//Beats
//100.00%


class Solution {
	public:
			bool checkMove(vector<vector<char>>& board, int rMove, int cMove, char color) {
				vector<vector<int>> steps = {{1, 0},{1, 1},{0, 1},{-1, 1},{-1, 0},{-1, -1},{0, -1},{1, -1}};
				for (vector<int> e : steps) {
					int rStep = e[0];
					int cStep = e[1];
					if (checkByStep(rStep, cStep, rMove, cMove, color, board)) {
						return true;
					}
				}
				return false;
			}
	private:
		bool checkByStep(int rStep, int cStep, int r, int c, char side, vector<vector<char>> board) {
			int row = board.size(), col = board[0].size();
			r += rStep;
			c += cStep;
			if (
				(r < 0 || r >= row) ||
				(c < 0 || c >= col) ||
				board[r][c] == side ||
				board[r][c] == '.'
			) {
				return false;
			}
			r += rStep;
			c += cStep;
			while (r >= 0 && r < row && c >= 0 && c < col) {
				if (board[r][c] == '.') {
					return false;
				}
				if (board[r][c] == side) {
					return true;
				}
				r += rStep;
				c += cStep;
			}
			return false;
		}
};
