# first KMP solved independently: 15%
from sortedcontainers import SortedList
class Solution:
    @staticmethod
    def build(p):
        n = len(p)
        lps = [0] * n
        length = 0
        for i in range(1, n):
            while length > 0 and p[i] != p[length]:
                length = lps[length - 1]
            if p[i] == p[length]:
                length += 1
                lps[i] = length
        return lps

    @staticmethod
    def check(s, p):
        lps = Solution.build(p)
        length = 0
        n = len(s)
        arr = []
        for i in range(n):
            while length > 0 and s[i] != p[length]:
                length = lps[length - 1]
            if s[i] == p[length]:
                length += 1
                if length >= len(p):
                    arr.append(i - len(p) + 1)
                    length = lps[length - 1]
        return arr

    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        arr = Solution.check(s, a)
        brr = Solution.check(s, b)
        arr.sort()
        brr.sort()
        ans = []
        sl = SortedList()

        for b in brr: sl.add(b)

        for a in arr:
            j = sl.bisect_left(a)
            if j > 0 and abs(a - brr[j - 1]) <= k:
                ans.append(a)
            elif j < len(brr) and abs(a - brr[j]) <= k:
                ans.append(a)

        return ans
