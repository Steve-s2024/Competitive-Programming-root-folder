# greedy solution: 76
# ms
# Beats
# 13.25%
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        hashMap = {}
        for r, c in reservedSeats:
            if r not in hashMap:
                hashMap[r] = [True, True, True]
            if c in range(2, 6):
                hashMap[r][0] = False
            if c in range(4, 8):
                hashMap[r][1] = False
            if c in range(6, 10):
                hashMap[r][2] = False
        res = 0
        for val in hashMap.values():
            if val[0] and val[2] == True:
                res += 2
            elif val[0] or val[1] or val[2] == True:
                res += 1
        return res + (n-len(hashMap)) * 2