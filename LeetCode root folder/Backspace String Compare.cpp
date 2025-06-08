// solution:1
//ms
//Beats
//14.39%
class Solution {
public:
    bool backspaceCompare(string s, string t) {
        vector<char> arr1, arr2;
        for (char c : s) {
             if (c != '#') arr1.push_back(c);
            else if (arr1.size() > 0) arr1.pop_back();
        }
        for (char c : t) {
            if (c != '#') arr2.push_back(c);
            else if (arr2.size() > 0) arr2.pop_back();
        }
        // cout << arr1.size() << ' ' << arr2.size() << endl;
        if (arr1.size() != arr2.size()) return false;
        for (int i = 0; i < arr1.size(); i++) {
            if (arr1[i] != arr2[i]) return false;
        }
        return true;
    }
};