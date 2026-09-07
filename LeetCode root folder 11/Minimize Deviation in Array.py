# a pretty common technique to handle minimize difference after multiplication of same factor
# in the base case, the largest element should never be multiplied nor divided (it remains itself and free from any operation)
# then the problem can be proven greedy by way of contradiction (either all the rest right below largest or all the rest above largest)

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        n = len(nums)
        ar = []
        for i in range(n):
            x = nums[i]
            while x % 2 == 0: x >>= 1
            ar.append([x, (2*nums[i]) if nums[i]%2 else nums[i]])
        ans = 0
        ar.sort()
        t = ar[-1][0]
        for i in range(n-1):
            mi = min(ar[i][1], t)
            while ar[i][0]*2 <= mi: ar[i][0] *= 2
            # print(ar[i][0])
            ans = max(ans, t-ar[i][0])
        ar.sort()
        # print(ans, ar)
        for i in range(n-1):
            if ar[i][0] < ar[i][1]: ans = min(ans, 2*ar[i][0]-ar[i+1][0])
            else: break
        return ans