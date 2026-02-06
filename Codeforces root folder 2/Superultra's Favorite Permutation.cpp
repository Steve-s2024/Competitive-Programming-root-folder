#include<iostream>
#include<vector>
using namespace std;


int main() {
    int p;
    cin >> p;
    for (int pos = 0; pos < p; pos++) {
        int n;
        cin >> n;
        if (n >= 5) {
            vector<int> ans;
            for (int i = 1; i < n; i+=2) {
                if (i == 5) continue;
                ans.push_back(i);
            }
            ans.push_back(5);
            ans.push_back(4);
            for (int i = 2; i < n; i+=2) {
                if (i == 4) continue;
                ans.push_back(i);
            }
            for (int num : ans) cout << num << ' ';
            cout << endl;
        }
        else cout << -1 << endl;
    }
    
}
