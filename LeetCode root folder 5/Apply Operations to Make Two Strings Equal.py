# finally, using many hints and solved via DP knap-sack: 16%

class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:

        arr = []
        n = len(s1)
        for i in range(n):
            if s1[i] != s2[i]: arr.append(i)

        # print(arr)
        @lru_cache(10**5)
        def recursive(i, stat1, stat2):
            if i >= len(arr):
                if stat1 is not None or stat2: return inf
                return 0
            res = recursive(i+1, stat1, not stat2) + x/2
            if stat1 is not None: res = min(res, recursive(i+1, None, stat2) + arr[i]-stat1)
            else: res = min(res, recursive(i+1, arr[i], stat2))
            return res

        res = recursive(0, None, False)
        if res == inf: return -1
        return int(res)




# failed attempt
class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:

        arr = []
        n = len(s1)
        for i in range(n):
            if s1[i] != s2[i]: arr.append(i)

        cost = 0
        i1 = 0
        for i in range(n):
            if i1 < len(arr) and i == arr[i1]:
                if i1 + 1 >= len(arr): return -1
                a, b = arr[i1], arr[i1 + 1]
                cost += min(b - a, x)
                i1 += 2

        return cost