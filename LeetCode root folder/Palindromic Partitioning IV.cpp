// none of these worked, all due to MLE, the fact is, i have 
// tried how LeetCode told me to do, but it failed to pass...
class Solution {
    public:
        bool checkPartitioning(string s) {
            int n = s.size();
            vector<vector<bool>> ref(n, vector<bool>(n, false));
            for (int i = 0; i < n; i++) {
                for (int j = i; j < n; j++) {
                    ref[i][j] = validPalin(i, j, s);
                }
            }
    
            for (int i = 1; i < n-1; i++) {
                for (int j = i; j < n-1; j++) {
                    if (ref[0][i-1] && ref[i][j] && ref[j+1][n-1]) return true;
                }
            }
            return false;
        }
        bool validPalin(int i, int j, string s) {
            while (i < j) {
                if (s[i] != s[j]) return false;
                i++;
                j--;
            }
            return true;
        }
    };


// can't figure out the way to limit the memory:MLE
class Solution {
    public:
        bool checkPartitioning(string s) {
            bool ref[2000][2000] = {};
            int n = s.size();
            for (int i = 0; i < n; i++) {
                for (int j = i; j < n; j++) {
                    ref[i][j] = validPalin(i, j, s);
                }
            }
            
            bool dp[2000][3] = {};
            for (int i = 0; i <= 1; i++)  {
                for (int j = n-1; j >= 0; j--) {
                    for (int k = j; k < n; k++) {
                        if (ref[j][k]) {
                            if (i == 0 && k == n-1) dp[j][i] = true;
                            else if (i != 0 && k < n-1 && dp[k+1][i-1]) dp[j][i] = true; 
                        }
                    }
                }
            }
            for (int i = 0; i < n-2; i++) {
                if (ref[0][i] && dp[i+1][1]) return true;
            }
            return false;
        }
        bool validPalin(int i, int j, string s) {
            while (i < j) {
                if (s[i] != s[j]) return false;
                i++;
                j--;
            }
            return true;
        }
    };

// failed attempt of c++ with optimized dp: WA
class Solution {
    public:
        bool checkPartitioning(string s) {
            int n = s.size();
            bool dp[2000][3] = {};
            for (int i = 0; i <= 2; i++)  {
                for (int j = n-1; j >= 0; j--) {
                    for (int k = j; k < n; k++) {
                        if (validPalin(j, k, s)) {
                            if (i == 0 && k == n-1) dp[j][i] = true;
                            else if (i != 0 && k < n-1 && dp[k+1][i-1]) dp[j][i] = true; 
                            if (i == 2 && dp[k][i]) return true;
                        }
                    }
                }
            }
            return false;
        }
        bool validPalin(int i, int j, string s) {
            while (i < j) {
                if (s[i] != s[j]) return false;
                i++;
                j--;
            }
            return true;
        }
    };