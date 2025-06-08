// dp solution with optimized approach, using array and for loop: 7%
class Solution {
    public:
        int numberOfArrays(string s, int k) {
            int n = s.size();
            int MOD = 1000000007;
            long long dp[n+1];
            for (int i = 0; i < n; i++) dp[i] = 0;
            dp[n] = 1;
            for (int i = n-1; i >= 0; i--) {
                if (s[i] == '0') continue;
                string str = "";
                for (int j = i; j < n; j++) {
                    str += s[j];
                    if (stoll(str) <= k) {
                        dp[i] += dp[j+1];
                        dp[i] %= MOD;
                    }
                    else break;
                }
            }
            for (long long num : dp) cout << num << ' ';
            return dp[0];
        }
    };