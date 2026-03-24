# sliding window + binary search

# observation on how if distinct(nums[l:r]) = k, then distinct(nums[L:R]) >= k for all L <= l and R >= r
# once this is established then we can calculate the number of subarray has distinct() >= m for arbitrary m in O(n) time
# plus the median monotonic nature, the binary search solution is just evidential 
class Solution:
    def medianOfUniquenessArray(self, nums: List[int]) -> int:
        n, l, r = len(nums), 1, len(set(nums))
        N = n*(n+1)//2
        t = (N-1)//2
        # print(N)
        while l <= r:
            m, a, b = (l+r)//2, 0, 0
            j, x, mp = 0, 0, defaultdict(int)
            for i in range(n):
                mp[nums[i]] += 1
                if mp[nums[i]] == 1: x += 1
                while x > m:
                    mp[nums[j]] -= 1
                    if mp[nums[j]] == 0: x -= 1
                    j += 1
                if x == m: a += j
            # a -> number of >= m+1 subarray
            j, x, mp = 0, 0, defaultdict(int)
            for i in range(n):
                mp[nums[i]] += 1
                if mp[nums[i]] == 1: x += 1
                while x > m-1:
                    mp[nums[j]] -= 1
                    if mp[nums[j]] == 0: x -= 1
                    j += 1
                if x == m-1: b += j
            # b -> number of >= m subarray
            # print(m, a, b)
            if t in range(N-b, N-a): return m
            elif t > N-b: l = m+1
            else: r = m-1
        # print(l, r, t)
        return 0
