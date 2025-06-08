# brute-force: tle
'''
class Solution:
    def numWays(self, s: str) -> int:
        # brute-force
        num = Counter(s)['1']
        if num % 3 != 0:
            return 0
        count = num // 3
        res = 0
        def recursive(idx, depth):
            nonlocal count, res
            if depth >= 2:
                res += 1
                return
            i = idx
            cur = 0
            while i < len(s):
                if s[i] == '1':
                    cur += 1
                if cur == count:
                    break
                i += 1
            i += 1
            while i < len(s):
                recursive(i, depth + 1)
                if s[i] != '0':
                    break
                i += 1
        recursive(0, 0)
        return res'''

# dp solution: tle
'''class Solution:
    def numWays(self, s: str) -> int:
        # dp solution
        num = Counter(s)['1']
        if num % 3 != 0:
            return 0
        count = num // 3
        dp = {}
        def recursive(idx, depth):
            nonlocal count
            if (idx, depth) in dp:
                return dp[(idx, depth)]
            if depth >= 2:
                return 1
            i = idx
            cur = 0
            while i < len(s):
                if s[i] == '1':
                    cur += 1
                if cur == count:
                    break
                i += 1
            i += 1
            res = 0
            while i < len(s):
                res += recursive(i, depth + 1)
                if s[i] != '0':
                    break
                i += 1
            dp[(idx, depth)] = res
            return res
        return recursive(0, 0)'''

# greedy solution:95
# ms
# Beats
# 23.45%
class Solution:
    def numWays(self, s: str) -> int:
        # greedy
        num = Counter(s)['1']
        if num % 3 != 0:
            return 0
        if num == 0:
            return ((len(s) - 1) * (len(s) - 2) // 2) % (pow(10, 9) + 7)
        count = num // 3
        i = 0
        res = 1
        for tar in range(2):
            cur = 0
            while i < len(s):
                if s[i] == '1':
                    cur += 1
                if cur == count:
                    break
                i += 1
            i += 1
            j = i
            while j < len(s):
                if s[j] != '0':
                    break
                j += 1
            res *= (j - i + 1)
            i = j
        return res % (pow(10, 9) + 7)

