// 

# is one is accepted
void solve() {
    int n, m;
    cin >> n >> m;
    vector<int> ans(n);
    for (int i = 0; i < n; i++) {
        int prev, cur;
        cin >> prev;
        int min_ = prev;
        for (int j = 1; j < m; j++) {
            cin >> cur;
            min_ = min(min_, cur);
            if (abs(prev-cur) % n != 0) {
                ans.clear();
                ans.push_back(-1);
            } 
        }
        if (ans[0] != -1) ans[min_] = i+1;
    }

    for (int num : ans) cout << num << ' ';
    cout << endl;
    
}


int main() {
    int t;
    cin >> t;
    for (int T = 0; T < t; T++) {
        solve();
    }
}