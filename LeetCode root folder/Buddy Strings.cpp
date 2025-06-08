class Solution {
public:
    bool buddyStrings(string s, string goal) {
        if (s.size() != goal.size()) return false;
        unordered_map<char, int> map;
        int cnt = 0;
        int maxFrq = 0;
        for (int i = 0; i < s.size(); i++) {
            if (s[i] != goal[i]) {
                cnt++;
            }
            if (map.find(s[i]) == map.end()) {
                map[s[i]] = 0;
            }
            map[s[i]] ++;
            maxFrq = max(maxFrq, map[s[i]]);
        }
        for (char c : goal) {
            if (map.find(c) == map.end() || map[c] == 0) return false;
            map[c]--;
        }
        return (cnt == 2) || (cnt == 0 && maxFrq > 1);
    }
};