// I just cannot believe how fking faster it is to use static array dp over dynamic size vector even if it means to
// create dp array of size 16 millions for every single fucking testcase...
// this is so fking dramatic: 12%

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int longestPalindrome(string word1, string word2) {
        string a = word1 + word2;
        int n = a.size();
        const int NEG_INF = -1000000000;

        // dp[i][j][f1][f2]
        static int dp[2000][2000][2][2];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                for (int f1 = 0; f1 < 2; f1++)
                    for (int f2 = 0; f2 < 2; f2++)
                        dp[i][j][f1][f2] = -1;

        function<int(int,int,int,int)> recursive = [&](int i, int j, int f1, int f2) -> int {
            if (dp[i][j][f1][f2] != -1) return dp[i][j][f1][f2];
            if (i == j) return dp[i][j][f1][f2] = (f1 && f2) ? 1 : NEG_INF;
            if (i > j) return dp[i][j][f1][f2] = (f1 && f2) ? 0 : NEG_INF;

            int res;
            if (a[i] == a[j]) {
                int nf1 = f1, nf2 = f2;
                if (i < (int)word1.size()) nf1 = 1;
                if (j >= (int)word1.size()) nf2 = 1;
                res = recursive(i + 1, j - 1, nf1, nf2) + 2;
            } else {
                res = max(recursive(i + 1, j, f1, f2),
                          recursive(i, j - 1, f1, f2));
            }
            return dp[i][j][f1][f2] = res;
        };

        int res = recursive(0, n - 1, 0, 0);
        return (res > 0) ? res : 0;
    }
};