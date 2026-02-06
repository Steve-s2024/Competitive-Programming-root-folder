# a standard solution of finding the next greater element among all permutation of the input number
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        s = list(str(n))
        for i in range(len(s)-2, -1, -1):
            if s[i] < s[i+1]:
                idx = i+1
                for j in range(i+1, len(s)):
                    if s[j] > s[i]: idx = j
                s[i], s[idx] = s[idx], s[i]
                s = s[:i+1] + sorted(s[i+1:])
                res = int(''.join(s))
                return res if res < 1<<31 else -1
        return -1