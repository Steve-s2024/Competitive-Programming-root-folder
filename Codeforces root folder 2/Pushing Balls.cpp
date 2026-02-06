// 
void solve() {
    int n, m;
    cin >> n >> m;
    string row;
    bool flag = true;
    unordered_map<string, pair<bool, bool>> hashMap;
    // hashMap[string...][0] --> horizontal validity
    // hashMap[string...][1] --> vertical validity
    for (int r = 0; r < n; r++) {
        cin >> row;
        for (int c = 0; c < m; c++) {
            int cur = row[c] - '0';
            if (cur == 1) {
                string s = to_string(r)+','+to_string(c);
                string s1 = to_string(r-1)+','+to_string(c);
                string s2 = to_string(r)+','+to_string(c-1);

                hashMap[s].first = (r == 0 || hashMap[s1].first);
                hashMap[s].second = (c == 0 || hashMap[s2].second);

                if (!hashMap[s].first && !hashMap[s].second) flag = false;
            }
        }
    }

    if (flag) cout << "YES" << endl;
    else cout << "NO" << endl;
}


int main() {
    int t;
    cin >> t;
    for (int T = 0; T < t; T++) {
        solve();
    }
}





// depricated
void solve() {
    int n, m;
    cin >> n >> m;
    string row;
    bool flag = true;
    unordered_set<string> hashSet;
    for (int r = 0; r < n; r++) {
        cin >> row;
        for (int c = 0; c < m; c++) {
            int cur = (int)row[c];
            if (cur == 1) {
                string a = to_string(r+1)+','+to_string(c), b = to_string(r)+','+to_string(c+1);
                hashSet.insert(a);
                hashSet.insert(b);
            }
            string s = to_string(r)+','+to_string(c);
            if (cur == 1 && r != 0 && c != 0 && hashSet.find(s) == hashSet.end()) {
                cout << s << endl;
                flag = false;
            }
        }
    }
    
    if (flag) cout << "YES" << endl;
    else cout << "NO" << endl;
}


int main() {
    int t;
    cin >> t;
    for (int T = 0; T < t; T++) {
        solve();
    }
}
