# very intricate relationship, but all I did was follow the instinct to get to the solution, the hard part is actually
# handling the binary search properly so no miscount / off by one happens: 6%


class Solution:
    @staticmethod
    def getMx(nums):
        sm = sum(nums)
        tot = 0
        cnt = 0
        for i in range(len(nums) - 1):
            tot += nums[i]
            if tot * 2 == sm: cnt += 1
        return cnt

    def waysToPartition(self, nums: List[int], k: int) -> int:

        st = set()
        pre = defaultdict(list)
        n = len(nums)
        sm = sum(nums)
        tot = 0
        for i in range(n - 1):
            tot += nums[i]
            st.add(nums[i])
            re = sm - tot
            # make tot equals to re
            # tot - nums[x] + k == re
            # tot - re + k == nums[x]
            tar = tot - re + k
            if tar in st: pre[tar].append(i + 1)

        st = set()
        suf = defaultdict(list)
        tot = 0

        for i in range(n - 1, 0, -1):
            tot += nums[i]
            st.add(nums[i])
            re = sm - tot
            tar = tot - re + k
            if tar in st: suf[tar].append(i)

        # print(pre)
        # print(suf)

        ans = 0
        for i in range(n):
            cur = nums[i]
            # print()
            # print(cur)
            cnt = 0
            res = len(pre[cur])
            l, r = 0, len(pre[cur]) - 1
            while l <= r:
                m = (l + r) // 2
                if pre[cur][m] > i:
                    res = m
                    r = m - 1
                else:
                    l = m + 1
            cnt += len(pre[cur]) - res
            # print(len(pre[cur])-res, cnt)

            res = len(suf[cur])
            l, r = 0, len(suf[cur]) - 1
            while l <= r:
                m = (l + r) // 2
                if suf[cur][m] <= i:
                    res = m
                    r = m - 1
                else:
                    l = m + 1
            cnt += len(suf[cur]) - res
            # print(len(suf[cur])-res, cnt)

            ans = max(ans, cnt)
        return max(ans, Solution.getMx(nums))