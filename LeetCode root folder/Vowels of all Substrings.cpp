// greedy solution:50.29%
class Solution {
public:
    long long countVowels(string word) {
        // the number of time a digit in word appears in substring can be represent by:
        //          f(i) = (n-i) * (i+1), where n is the size of word, i is the index of the digit
        long long n = word.size();
        long long res = 0;
        unordered_set<char> set;
        set.insert('a');
        set.insert('e');
        set.insert('i');
        set.insert('o');
        set.insert('u');
        for (long long i = 0; i < n; i++) {
            if (set.find(word[i]) != set.end()) {
                res += (n-i) * (i+1);
            }
        }
        return res;
    }
};