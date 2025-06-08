// python code hit TLE, so cpp, the idea is obvious, but implementation
// is tedious
void solve() {
    int row, col, n, p; cin >> row >> col >> n >> p;
    int grid[row][col];
    for (int i = 0; i < row; i++) {
        for (int j = 0; j < col; j++) {
            cin >> grid[i][j];
        }
    }
    unordered_set<int> st;
    for (int r = 0; r < row; r++) {
        for (int c = 0; c < col; c++) {
            int val1 = grid[r][c];
            if (val1 <= p && val1 != 0) {
                int coors[4][2] = {{r+1,c},{r-1,c},{r,c+1},{r,c-1}};
                for (auto coor : coors) {
                    int R = coor[0], C = coor[1];
                    if (
                        R >= 0 && R < row &&
                        C >= 0 && C < col &&
                        grid[R][C] != 0
                    ) {
                        int val2 = grid[R][C];
                        int diff = val2 - val1;
                        int cand = p + diff;
                        if (cand >= 1 and cand <= n) {
                            st.insert(cand);
                        }
                    }
                }
            }
        }
    }
    cout << st.size() << '/' << n-1 << '\n' << endl;
}

int main() {
    int t; cin >> t;
    for (int i = 0; i < t; i++) {
        solve();
    }
}
