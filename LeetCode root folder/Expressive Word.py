# two pointer? four pointers!:7
# ms
# Beats
# 79.12%
class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        res = 0
        for word in words:
            l1, r1 = 0, 1
            l2, r2 = 0, 1
            while r1 <= len(word) and r2 <= len(s):
                while r1 < len(word) and word[r1 - 1] == word[r1]:
                    r1 += 1
                while r2 < len(s) and s[r2 - 1] == s[r2]:
                    r2 += 1
                len1, len2 = (r1 - l1), (r2 - l2)
                # print(len1, len2, word[l1], s[l2])
                if (
                        (word[l1] == s[l2]) and
                        (len1 == len2 or (len1 < len2 and len2 >= 3))
                ):
                    # it's a valid stretch group, continue matching
                    l1, l2 = r1, r2
                    r1 += 1
                    r2 += 1
                else:
                    # the group is not a stretch of the other group, terminate loop
                    break
            else:
                # didn't terminate, this is a valid string
                if r1 == len(word) + 1 and r2 == len(s) + 1:
                    res += 1
        return res

