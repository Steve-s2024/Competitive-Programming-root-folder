# after all the time, the bug is because of the improper calculation of sm, now it is fixed, but the code keeps
# getting MLE at the last few TCs. in the discussion tab they are suggests bottom up DP. which I guess save some memory
class Solution:
    def maxSum(self, nums: List[int], k: int, m: int) -> int:
        inf = math.inf
        n = len(nums)

        pre = []
        tot = 0
        for i in range(n):
            tot += nums[i]
            pre.append(tot)
        dp = {}
        def recursive(i, k, status):
            nonlocal n, m, inf
            if k == 0: return 0
            if i >= n: return -inf
            state = (i, k, status)
            if state in dp: return dp[state]
            res = -inf
            if status == 1:
                res = max(
                    nums[i] + recursive(i+1, k, 1),
                    nums[i] + recursive(i+1, k-1, 0)
                )
            else:
                res = recursive(i+1, k, 0)
                if i+m-1 < n:
                    # sm = sum(e for e in nums[i:i+m-1])
                    sm = (pre[i+m-2]-pre[i]+nums[i] if m >= 2 else 0)
                    res = max(res, sm + recursive(i+m-1, k, 1))
            dp[state] = res
            return res
        return recursive(0, k, 0)


# second attempt, still has error
class Solution:
    def maxSum(self, nums: List[int], k: int, m: int) -> int:

        inf = math.inf
        n = len(nums)

        pre = []
        tot = 0
        for i in range(n):
            tot += nums[i]
            pre.append(tot)

        def recursive(i, k, status):
            nonlocal n, m, inf
            if k == 0: return 0
            if i >= n: return -inf

            res = -inf
            if status == 'open':
                res = max(
                    nums[i] + recursive(i+1, k, 'open'),
                    nums[i] + recursive(i+1, k-1, 'close')
                )
            else:
                res = recursive(i+1, k, 'close')
                if i+m-1 < n:
                    sm = pre[i+m-1]-pre[i]
                    res = max(res, sm + recursive(i+m-1, k, 'open'))
            return res
        return recursive(0, k, 'close')




# first attempt, have error but is at the right direction
class Solution:
    def maxSum(self, nums: List[int], k: int, m: int) -> int:

        inf = math.inf
        n = len(nums)

        pre = []
        tot = 0
        for i in range(n):
            tot += nums[i]
            pre.append(tot)

        def recursive(i, k, status):
            nonlocal n, k, m, inf
            if k == 0: return 0, i-1
            if i >= n: return -inf, -1

            res = (-inf, -1)
            if status == 'open':
                a, j = recursive(i+1, k-1, 'close')
                if a > res[0]: res = (a, i)
            else:
                a, j = recursive(i+m-1, k, 'open')
                if a+pre[j]-pre[i]+nums[i] > res[0]: res = (a+pre[j]-pre[i]+nums[i], j)
            a, j = recursive(i+1, k, status)
            if a > res[0]: res = (a, j)
            return res
        a, j = recursive(0, k, 'close')
        return a