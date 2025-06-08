//bfs solution:3
//ms
//Beats
//15.89%
class Solution {
	public:
		vector<int> shortestToChar(string s, char c) {
			unordered_set<int> visited;
			deque<int> q;
			vector<int> ans(s.size(), 0);
			for (int i = 0; i < s.size(); i++) {
				if (s[i] == c) {
					q.push_back(i);
					visited.insert(i);
                    // cout << q[q.size()-1] << endl;
				}
			}


			int time = 0;
			while (q.size() > 0) {
				int l = q.size();
				while (l > 0) {
					int cur = q.front();
					q.pop_front();
					ans[cur] = time;
					if (visited.find(cur-1) == visited.end() && cur > 0) {
                        visited.insert(cur-1);
						q.push_back(cur-1);
					}
					if (visited.find(cur+1) == visited.end() && cur < s.size()-1) {
						visited.insert(cur+1);
						q.push_back(cur+1);
					}
					l--;
				}
				time++;
			}
			return ans;
		}
	};