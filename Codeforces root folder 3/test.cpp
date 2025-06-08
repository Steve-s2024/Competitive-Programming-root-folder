#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;


vector<int> factorize(int num) {
    vector<int> res;
    for (int f = 2; f < (int)sqrt(num)+1; f++) {
        while (num % f == 0) {
            res.push_back(f);
            num /= f;
        }
    }
    if (num != 1) {
        res.push_back(num);
    }
    return res;
}

int intersect(int num, vector<int> &arr) {
    int res = 1;
    for (int f : arr) {
        if (num % f == 0) {
            res *= f;
            num /= f;
        }
    }
    return res;
}

int recursive(vector<int> &nums, vector<vector<int>> &fs, int al, int (&dp)[5000][5000], int n, int i, int gcd) {
    if (dp[i][gcd] != 0) {
        return dp[i][gcd];
    }
    if (gcd == al) {
        return 0;
    }
    if (i >= n) {
        return 100000000;
    }
    int a, b;
    if (gcd != 0) {
        a = recursive(nums, fs, al, dp, n, i+1, intersect(gcd, fs[i])) + 1;
    }
    else {
        a = recursive(nums, fs, al, dp, n, i+1, nums[i]);
    }
    b = recursive(nums, fs, al, dp, n, i+1, gcd);
    dp[i][gcd] = min(a, b);
    return min(a, b);
}

void solve() {
    int n; cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; i++) cin >> nums[i];

    vector<vector<int>> fs;
    for (int num : nums) {
        fs.push_back(factorize(num));
    }

    unordered_map<int, int> mp;
    for (int f : fs[0]) mp[f]++;
    for (vector<int> f : fs) {
        unordered_map<int, int> tmp;
        for (int a : f) tmp[a]++;
        for (pair<int, int> p : mp) {
            mp[p.first] = min(p.second, tmp[p.first]);
        }
    }

    int al = 1;
    for (pair<int, int> p : mp) {
        al *= pow(p.first, p.second);
    }

    mp.clear();
    for (int num : nums) mp[num]++;
    if (mp.find(al) != mp.end()) {
        cout << n-mp[al] << endl;
    }
    else {
        int dp[5000][5000];
        memset(dp, 0, sizeof(dp));
        int res = recursive(nums, fs, al, dp, n, 0, 0);
        cout << res-1+n << endl;
    }
}

int main() {
    ios_base::sync_with_stdio(false);cout.tie(nullptr);cin.tie(nullptr);
    int t; cin >> t;
    for (int i = 0; i < t; i++) {
        solve();
    }
}
