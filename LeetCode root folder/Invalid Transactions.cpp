//hashMap, sorting, and deque solution:151
//ms
//Beats
//16.49%
class Solution {
	public:
        vector<string> invalidTransactions(vector<string>& transactions) {
                unordered_map<string, vector<vector<string>>> hashMap;
                unordered_set<int> ans;
                int size = transactions.size();
                for (int i = 0; i < size; i++) {
                    vector<string> info = split(transactions[i], ',');
                    if (stoi(info[2]) > 1000) {
                        ans.insert(i);
                    }
                    info.push_back(to_string(i));
                    if (hashMap.find(info[0]) == hashMap.end()) {
                        hashMap[info[0]] = {};
                    }
                    hashMap[info[0]].push_back(info);
                }

                for (auto& e : hashMap) {
                    vector<vector<string>> arr = e.second;
                    std::sort(arr.begin(), arr.end(), [](vector<string>& a, vector<string>& b) {
                        return stoi(a[1]) < stoi(b[1]); // Convert a[1] and b[1] to int for comparison
                    });
                    deque<vector<string>> q;
                    for (int i = 0; i < arr.size(); i++) {
                        vector<string> curInfo = arr[i];
                        while (q.size() > 0 && stoi(curInfo[1]) - stoi(q[0][1]) > 60) {
                            q.pop_front();
                        }
                        if (q.size() > 0) {
                            for (vector<string> info : q) {
                                if (info[3] != curInfo[3]) {
                                    cout << curInfo[4] << endl;
                                    ans.insert(stoi(curInfo[4]));
                                    ans.insert(stoi(info[4]));
                                }
                            }
                        }
                        q.push_back(arr[i]);
                    }
                }
                vector<string> res;
                for (int idx : ans) {
                    res.push_back(transactions[idx]);
                }
                return res;
			}
	private:
			vector<string> split(string str, char delimiter) {
                // cout << str << endl;

				vector<char> seg;
				vector<string> res;
				for (int i = 0; i < str.size(); i++) {
					if (str[i] != delimiter) {
						seg.push_back(str[i]);
					}
					else {
						string segStr(seg.begin(), seg.end());
						res.push_back(segStr);
                        // cout << segStr << endl;
						seg.clear();
					}
				}
                string segStr(seg.begin(), seg.end());
                res.push_back(segStr);
                return res;
			}
	};
