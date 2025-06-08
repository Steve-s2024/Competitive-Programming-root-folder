# bitmask solution credit for neetcode, I thought about this
# solution, and gave up because I thought the time complexity
# is 4^n, but it's only for the worst case, in most cases
# the time and number of subsequence palindrome is very small
# the time complexity varies greatly based on the input content: 42%
class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        hashMap = {}
        for mask in range(1, 1 << n):
            string = []
            for i in range(n):
                if mask & (1<<i) == (1<<i):
                    string.append(s[i])
            # check if string is palindrome
            m = len(string)
            for i in range(m//2):
                if string[i] != string[m-1-i]:
                    break
            else:
                hashMap[mask] = len(string)
        # print(hashMap)

        res = 0
        for mk1 in hashMap:
            for mk2 in hashMap:
                if mk1 & mk2 == 0:
                    # print(mk1, mk2)
                    res = max(res, hashMap[mk1] * hashMap[mk2])
        return res



# brute force recursion knapsack upgrade: 5%
class Solution:
    @staticmethod
    def checkIfPalin(arr1, arr2):
        n, m = len(arr1), len(arr2)
        for i in range(n // 2):
            if arr1[i] != arr1[n - 1 - i]:
                return False
        for i in range(m // 2):
            if arr2[i] != arr2[m - 1 - i]:
                return False
        return True

    def maxProduct(self, s: str) -> int:
        stk1, stk2 = [], []
        res = 0
        n = len(s)

        def recursive(i):
            nonlocal res
            if i >= n:
                if Solution.checkIfPalin(stk1, stk2):
                    res = max(res, len(stk1) * len(stk2))
                return

            # pick from the three option below for the current index:
            # 1. make it belongs to palin1
            # 2. make it belongs to palin2
            # 3. make it belongs to neither
            # this is an upgrade of knapsack, we upgraded from pick or not pick --> pick this, that, or that.
            # for complexity: s.length <= 12, so, up to 3^12
            # 3^3 = 27 < 30 --> 3^12 = 27^4 < 30^4 == 810,000 (its probably good)
            stk1.append(s[i])
            recursive(i + 1)
            stk1.pop()

            stk2.append(s[i])
            recursive(i + 1)
            stk2.pop()

            recursive(i + 1)

        recursive(0)
        return res