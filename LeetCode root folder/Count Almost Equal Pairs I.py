#39%
class Solution:
    def countPairs(self, nums: List[int]) -> int:
        def checkStrings(string1, string2):
            if len(string1) >= len(string2):
                s1, s2 = string1, string2
            else:
                s1, s2 = string2, string1
            s2 = (len(s1) - len(s2)) * '0' + s2
            pair = []
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    pair.append(i)
            if len(pair) == 0:
                return True
            if len(pair) != 2:
                return False
            return s1[pair[0]] == s2[pair[1]] and s1[pair[1]] == s2[pair[0]]

        res = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if checkStrings(str(nums[i]), str(nums[j])):
                    # print(nums[i], nums[j])
                    res += 1
        return res
