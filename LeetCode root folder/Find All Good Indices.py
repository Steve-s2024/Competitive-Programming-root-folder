# two pass with two pointer sliding window: 5%

class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        l, r = 0, 0
        nonDecre = [0] * n
        for i in range(n):
            r = max(l, r)
            while r < n and (r == l or nums[r] >= nums[r-1]):
                r += 1
            nonDecre[i] = r-l
            l += 1

        nonIncre = [0] * n
        l, r = n-1, n-1
        for i in range(n-1, -1, -1):
            l = min(l, r)
            while l >= 0 and (l == r or nums[l] >= nums[l+1]):
                l -= 1
            nonIncre[i] = r-l
            r -= 1
        # print(nonDecre)
        # print(nonIncre)

        ans = []
        for i in range(n):
            if (
                (i != n-1 and nonDecre[i+1] >= k) and
                (i != 0 and nonIncre[i-1] >= k)
            ):
                ans.append(i)
        
        return ans