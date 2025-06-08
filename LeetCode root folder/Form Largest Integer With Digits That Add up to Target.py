# for some wierd reason that the same approach, but with
# using the built-in max() function, it speed up by 60 fold!
# : 30%
# looks like it is because the built-in method max() is implemented
# in c, which has a huge advantage over looping in python and let python
# interpreter to translate it.

class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        def getMax(s1, s2):
            n, m = len(s1), len(s2)
            if n > m:
                return s1
            if n < m:
                return s2
            return max(s1, s2)

        
        dp = {}
        def recursive(remain):
            if remain in dp:
                return dp[remain]
            if remain == 0:
                return ''
            if remain < 0:
                return '0'
            res = '0'
            for j in range(9):
                a = recursive(remain-cost[j]) + str(j+1)
                if a[0] != '0':
                    # res = str(max(int(a), int(res)))
                    res = getMax(a, res)
            dp[remain] = res
            return res

        return recursive(target)


# brute force dp solution: 5%
class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        def getMax(s1, s2):
            n, m = len(s1), len(s2)
            if n > m:
                return s1
            elif n < m:
                return s2
            else:
                for i in range(n):
                    if s1[i] > s2[i]:
                        return s1
                    if s1[i] < s2[i]:
                        return s2
                return s1

        
        dp = {}
        def recursive(remain):
            if remain in dp:
                return dp[remain]
            if remain == 0:
                return ''
            if remain < 0:
                return '0'
            res = '0'
            for j in range(9):
                a = recursive(remain-cost[j]) + str(j+1)
                if a[0] != '0':
                    # res = str(max(int(a), int(res)))
                    res = getMax(a, res)
            dp[remain] = res
            return res

        return recursive(target)