// solution:0
//ms
//Beats
//100.00%

class Solution {
	public:
        vector<vector<int>> largeGroupPositions(string s) {
            vector<vector<int>> ans;
            int begin = 0;
            int count = 0;
						int size = s.size();
            for (int i = 1; i < size; i++) {
                if (s[i] == s[i-1]) {
                    count += 1;
                }
                else {
                    if (count >= 2) {
                        ans.push_back({begin, i-1});
                    }
                    begin = i;
                    count = 0;
                }
            }
            if (count >= 2) {
                ans.push_back({begin, size-1});
            }
            return ans;
        }
	};
