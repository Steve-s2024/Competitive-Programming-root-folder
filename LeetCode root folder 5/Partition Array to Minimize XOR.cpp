// hate leetcode when it being super unfriendly to python user, and I can't believe I forget to implement DP during
// the contest and wondering why this hit TLE sooner than my python code...: 43%
class Solution {
public:
    vector<int> arr;
    int n = -1;
    int **dp;
    long recursive(int i, int k) {
        if (i >= n) {
            if (k == 0) return 0;
            else return 1<<30;
        }
        if (k < 1) return 1<<30;
        if (dp[i][k-1] != -1) return dp[i][k-1];
        long res = 1<<30;
        long x = 0;
        for (int j = i; j<n; j++) {
            x ^= arr[j];
            long a = recursive(j+1, k-1);
            res = min(res, max(a, x));
        }
        dp[i][k-1] = res;
        return res;
    }

    long minXor(vector<int>& nums, int k) {
        n = nums.size();
        arr = nums;
        dp = (int **)malloc(sizeof(int *)*n);
        for (int i = 0; i < n; i++) {
            dp[i] = (int *)malloc(sizeof(int)*k);
            memset(dp[i], -1, sizeof(int)*k);
        }
        int res = recursive(0, k);
        for (int i = 0; i < n; i++) free(dp[i]);
        free(dp);
        return res;
    }
};