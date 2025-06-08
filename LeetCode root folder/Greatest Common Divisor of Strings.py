# 25%
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1, l2 = len(str1), len(str2)
        res = ""
        for i in range(1, max(l1, l2)+1):
            if l1 % i == 0 and l2 % i == 0 and str1[:i] == str2[:i]:

                flag1, flag2 = False, False
                for j in range(i, l1-i+1, i):
                    if str1[j-i:j] != str1[j:j+i]:
                        break
                else:
                    flag1 = True
                for j in range(i, l2-i+1, i):
                    if str2[j-i:j] != str2[j:j+i]:
                        break
                else:
                    flag2 = True

                if flag1 and flag2:
                    res = str1[:i]
        return res 