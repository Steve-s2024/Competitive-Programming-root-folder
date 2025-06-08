#include<iostream>
#include<unordered_map>
#include<unordered_set>
#include<algorithm>
#include<vector>
#include<cmath>
#include<deque>
#include<limits>
using namespace std;


void solve() {
    int n;
    cin >> n;
    vector<int> nums(n);
    unordered_map<int, int> mp;
    int maxPos = 1;

    for (int i = 0; i < n; i++) {
        cin >> nums[i];
        while (nums[i] >= pow(2, maxPos)) maxPos++;

        int num = nums[i];
        int remain = 0;
        int pos = 0;
        while (num > 0) {
            remain = num%2;
            num -= remain;
            num /= 2;
            if (remain == 1) mp[pos]++;
            pos+=1;
        }
    }
    // cout << "MP size: " << mp.size() << endl;
    if (mp.size() == 0) cout << 0;
    else {
        maxPos -= 1;
        // cout << "maxPos: " << maxPos << endl;
        long long ans = 0;
        for (int num : nums) {
            long long pos = 0, remain = 0, res = 0;
            while (pos <= maxPos) {
                remain = num%2;
                num -= remain;
                num /= 2;
                if (remain > 0) res += (long long)(n-mp[pos])*pow(2, pos);
                else res += (long long)mp[pos] * pow(2, pos);
                pos++;
            }
            ans = max(ans, res);
        }
        cout << ans;
    }
    cout << endl;
}


int main() {
    int t;
    cin >> t;
    for (int T = 0; T < t; T++) {
        solve();
    }
}
