# no pressure 13%

class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        stk = []
        mp = [-1]*n
        for i in range(n-1, -1, -1):
            while stk and nums[stk[-1]] < nums[i]:
                j = stk.pop()
                mp[j] = i
            stk.append(i)

        res = 0
        mp2 = defaultdict(deque)
        for i in range(n):
            while mp2[nums[i]] and mp2[nums[i]][0] <= mp[i]: mp2[nums[i]].popleft()
            res += len(mp2[nums[i]])
            mp2[nums[i]].append(i)
        return res + n
