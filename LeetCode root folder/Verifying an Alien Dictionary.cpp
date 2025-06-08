// 100%
class Solution {
  public:
      bool isAlienSorted(vector<string>& words, string order) {
          unordered_map<char, int> dict;
          int i = 0;
          for (char c : order) {
              dict[c] = i;
              i++;
          }
  
          for (int i1 = 1; i1 < words.size(); i1++) {
              string word1 = words[i1-1];
              string word2 = words[i1];
              int length = min(word1.size(), word2.size());
              int i2 = 0;
              for (; i2 < length; i2++) {
                  if (dict[word1[i2]] > dict[word2[i2]]) return false;
                  if (dict[word1[i2]] < dict[word2[i2]]) break;
              }
              if (i2 == length && word1.size() > word2.size()) return false;
          }                    
          return true;
      }
  };