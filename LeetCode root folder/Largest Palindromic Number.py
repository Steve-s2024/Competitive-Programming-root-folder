# greedy solution:23
# ms
# Beats
# 80.06%
class Solution:
    def largestPalindromic(self, num: str) -> str:
        cands = []
        hashMap = Counter(num)
        mid = -1
        for key, val in hashMap.items():
            if val > 1:
                cands.append((key, val // 2))
            if val % 2 != 0:
                mid = max(mid, int(key))

        res = ''
        cands.sort(key = lambda i : i[0], reverse=True)
        if not cands or cands[0][0] == '0':
            if mid == -1:
                return '0'
            else:
                return str(mid)
        # print(cands)
        for cand, count in cands:
            res += cand * count
        res = res + (str(mid) if mid != -1 else '') + res[::-1]
        return res