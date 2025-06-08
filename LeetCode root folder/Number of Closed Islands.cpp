//dfs solution which worked well with python, don't
//know why took so long in c++:856
//ms
//Beats
//5.18%
/*
class Solution {
	unordered_set<string> visited;
	public:
			int closedIsland(vector<vector<int>>& grid) {
				int row = grid.size(), col = grid[0].size();
				visited.clear();
				int numOfIsland = 0;
				for (int r = 0; r < row; r++) {
					for (int c = 0; c < col; c++) {
						if (visited.find(to_string(r)+','+to_string(c)) == visited.end() && grid[r][c] != 1) {
                            // cout << r << '-' << c << endl;
							if (validIsland(row, col, grid, r, c)) {
								numOfIsland++;
							}
						}
					}
				}
				return numOfIsland;
			}
	private:
			bool validIsland(int row, int col, vector<vector<int>> grid, int r, int c) {
				bool res = true;
				if (r == 0 || r == row-1 || c == 0 || c == col-1) {
					res = false;
				}
				// cout << r << ',' << c << endl;
				// for (const auto& e : visited) {
				// 	cout << e << endl;
				// }
				visited.insert(to_string(r)+','+to_string(c));
				vector<vector<int>> step = {{r+1, c},{r-1, c},{r, c+1},{r, c-1}};
				for (vector<int> coor : step) {
					int R = coor[0], C = coor[1];

					if (
						(R >= 0 && R < row) &&
						(C >= 0 && C < col) &&
						(visited.find(to_string(R)+','+to_string(C)) == visited.end()) &&
						grid[R][C] != 1
					) {
                        // cout << R << '_' << C << endl;
                        bool valid = validIsland(row, col, grid, R, C);
						res = res && valid;
					}
				}
				return res;
			}
	};
*/


// dfs solution no.2, for some how this is so much faster??:0
//ms
//Beats
//100.00%

class Solution {
	bool visited[100][100];
    vector<vector<int>> matrix;
    int row, col;
    vector<pair<int, int>> step ={{1, 0},{-1, 0},{0, 1},{0, -1}};
	public:
			int closedIsland(vector<vector<int>>& grid) {
                matrix = grid;
                row = matrix.size(), col = matrix[0].size();
                memset(visited, false, sizeof(visited));
                int numOfIsland = 0;
				for (int r = 0; r < row; r++) {
					for (int c = 0; c < col; c++) {
						if (!visited[r][c] && matrix[r][c] != 1) {
                            // cout << r << '-' << c << endl;
							if (dfs(r, c)) {
								numOfIsland++;
							}
						}
					}
				}
				return numOfIsland;
            }
    private:
        bool dfs(int r, int c) {
            visited[r][c] = true;
            bool res = true;
            if (r == 0 || r == row-1 || c == 0 || c == col-1) {
                res = false;
            }
            for (pair<int, int> e : step) {
                int R = r + e.first, C = c + e.second;
                if (
                    (R >= 0 && R < row) &&
                    (C >= 0 && C < col) &&
                    !visited[R][C] &&
                    matrix[R][C] != 1
                ) {
                    bool tmp = dfs(R, C);
                    res = res && tmp;
                }
            }
            return res;
        }
	};