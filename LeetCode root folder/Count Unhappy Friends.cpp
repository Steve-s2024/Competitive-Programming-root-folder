//simulation solution:75
//ms
//Beats
//14.69%

class Solution {
  public:
    int unhappyFriends(int n, vector<vector<int>>& preferences, vector<vector<int>>& pairs) {
        unordered_map<int, int> hashMap;
        for (vector<int> e : pairs) {
          int p1 = e[0];
          int p2 = e[1];
          hashMap[p1] = p2;
          hashMap[p2] = p1;
        }

        unordered_set<string> hashSet;
        unordered_set<int> unhappyFriends;
        for (int i = 0; i < n; i++) {
            for (int p : preferences[i]) {
                if (p == hashMap[i]) {
                    break;
                }
                string preferredPair = to_string(min(i, p)) + ',' + to_string(max(i, p));
                if (hashSet.find(preferredPair) != hashSet.end()) {
                    unhappyFriends.insert(i);
                    unhappyFriends.insert(p);
                }
                else {
                    hashSet.insert(preferredPair);
                }
            }
        }
        return unhappyFriends.size();
    }
};