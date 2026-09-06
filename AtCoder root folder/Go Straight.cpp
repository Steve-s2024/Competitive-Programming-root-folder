// so fking unfair that python and C++ share the same time constraint, now I have a stronger urge to change to C++
// this code took python at least 9 seconds (tested from local), and cpp passed them in 614ms



#include <bits/stdc++.h>
using namespace std;

void solve() {
    int h, w;
    cin >> h >> w;
    vector<string> g(h);
    for (int i = 0; i < h; i++) cin >> g[i];

    // int h = 1000, w = 1000;
    // vector<vector<char>> g(h, vector<char>(w, '.'));
    // g[0][0] = 'S';
    // g[h - 1][w - 1] = 'G';

    pair<int, int> srt = {-1, -1};
    pair<int, int> dst = {-1, -1};
    deque<tuple<int, int, int>> q;
    for (int i = 0; i < h; i++) {
        for (int j = 0; j < w; j++) {
            if (g[i][j] == 'S') {
                q.push_back({i, j, -1});
                srt = {i, j};
            }
            if (g[i][j] == 'G') dst = {i, j};
        }
    }

    tuple<int, int, int> cr = {-1, -1, -2};

    vector<vector<vector<bool>>> seen(h, vector<vector<bool>>(w, vector<bool>(4, false)));
    vector<vector<vector<tuple<int, int, int>>>> vs(
        h, vector<vector<tuple<int, int, int>>>(w, vector<tuple<int, int, int>>(4, {-1, -1, -2}))
    );

    while (!q.empty()) {
        auto [r, c, t] = q.front();
        q.pop_front();

        if (make_pair(r, c) == dst) {
            cr = {r, c, t};
            break;
        }

        int i = -1;
        char x = g[r][c];
        for (auto [R, C] : vector<pair<int, int>>{{r + 1, c}, {r - 1, c}, {r, c + 1}, {r, c - 1}}) {
            i += 1;
            if (R < 0 || R >= h || C < 0 || C >= w || seen[R][C][i] || g[R][C] == '#') continue;
            if ((x == 'o' && i != t) || (x == 'x' && i == t)) continue;
            seen[R][C][i] = true;
            vs[R][C][i] = {r, c, t};
            q.push_back({R, C, i});
        }
    }

    if (get<0>(cr) == -1) {
        cout << "No\n";
        return;
    }

    string ref = "DURL";
    vector<char> seq;
    while (1) {
        auto [r, c, t] = cr;
        if (make_pair(r, c) == srt) break;
        cr = vs[r][c][t];
        seq.push_back(ref[t]);
    }

    cout << "Yes\n";
    // cout << seq.size() << '\n';
    reverse(seq.begin(), seq.end());
    for (char ch : seq) cout << ch;
    cout << '\n';
}



int main() {
  solve();
  return 0;
}