# KMP solution, toasted my brain learning this new algorithm
# it is so far the most sophisticated algorithm: 80%
class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        arr = []
        n = len(nums)
        for i in range(1, n):
            a = nums[i] - nums[i - 1]
            if a != 0:
                a = a // abs(a)
            arr.append(a)

        m = len(pattern)
        lps = [0] * m
        length = 0
        for i in range(1, m):
            while length > 0 and pattern[length] != pattern[i]:
                length = lps[length - 1]
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length

        res = 0
        j = 0
        for i in range(n - 1):
            # print(i, j)
            while j > 0 and arr[i] != pattern[j]:
                j = lps[j - 1]
            if arr[i] == pattern[j]:
                j += 1
            if j == m:
                res += 1
                j = lps[j - 1]
        return res


# bit masking: TLE
class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n = len(nums)
        m = len(pattern)
        res = 0
        mask = 0
        cur = 0
        for i in range(1, m+1):
            a = nums[i] - nums[i-1]
            if a != 0:
                a = a//abs(a)
            mask += (pattern[i-1]+1) * pow(3, i-1)
            cur += (a+1) * pow(3, i-1)
        if cur == mask:
            res += 1

        for i in range(n-1-m):
            a = nums[i+1] - nums[i]
            b = nums[i+m+1] - nums[i+m]
            if a != 0:
                a = a//abs(a)
            if b != 0:
                b = b//abs(b)
            cur -= (a+1)
            cur //= 3
            cur += (b+1) * pow(3, m-1)
            if cur == mask:
                res += 1
        return res

# brute force: TLE
class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n = len(nums)
        m = len(pattern)
        res = 0
        for i in range(0, n-m):
            for j in range(i+1, i+m+1):
                # print(i, i+m+1)
                a = nums[j] - nums[j-1]
                if a != 0:
                    a = a//abs(a)
                if a != pattern[j-i-1]:
                    break
            else:
                res += 1
        return res
