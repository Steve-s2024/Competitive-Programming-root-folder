#include<iostream>
#include<unordered_map>
#include<unordered_set>
#include<algorithm>
#include<vector>
#include<cmath>
#include<deque>
#include<limits>
#include<numeric>
using namespace std;

class Solution {
    public:
        bool checkPartitioning(string s) {
            int n = s.size();
            bool dp[n][3] = {};
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