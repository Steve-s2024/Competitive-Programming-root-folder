# this hash map & sliding window approach is not very intuitive tbh: 9%
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        mp = defaultdict(int)
        j = 0
        res = inf
        for i in range(n):
            while j < n and nums[j] - nums[i] <= n - 1:
                mp[nums[j]] += 1
                j += 1

            re = n - len(mp)

            res = min(res, re)
            mp[nums[i]] -= 1
            if mp[nums[i]] == 0: mp.pop(nums[i])
        return res


    # deprecated sliding window solution
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        itv = []
        l, r = 0, 0
        while r < n:
            while r < n - 1 and nums[r] + 1 == nums[r + 1]: r += 1
            if l:
                dif = nums[l] - nums[l - 1] - 1
                itv.append(dif)
            itv.append((l, r))
            l = r + 1
            r = l

        # print(itv)
        m = len(itv)
        j = 0
        tot = itv[0][1] - itv[0][0] + 1
        cost = 0
        res = inf
        for i in range(0, m, 2):
            while j < m - 2 and tot < n:
                l, r = itv[j + 2]
                gap = itv[j + 1]
                cost += gap
                tot += gap + r - l + 1
                j += 2
            if tot >= n:
                if j:
                    l, r = itv[j]
                    gap = itv[j - 1]
                    res = min(
                        min(
                            cost,
                            cost - gap + (n - (tot - gap - (r - l + 1)))
                        ),
                        res)
                else:
                    res = min(cost, res)
            if cost:
                cost -= itv[i + 1]
                tot -= itv[i + 1]
            tot -= itv[i][1] - itv[i][0] + 1
        return res