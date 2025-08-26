# solved this 2300 question without much help other than checking the problem tags, lets go!
# and it didn't even take me too long to implement, and the idea strike me after 20 minutes staring at the problem: 5%
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)

        tot = 0
        pre = [0]
        for i in range(n):
            tot += nums[i]
            pre.append(tot)
        # print(pre)
        res = inf
        q = deque()
        sl = SortedList()
        for i in range(n + 1):
            cnt = sl.bisect_right(pre[i] - k)
            # print(pre[i], cnt)
            flag = cnt > 0
            while cnt:
                val = q.popleft()
                sl.remove(val)
                if pre[i] - k >= val: cnt -= 1
            if flag: res = min(res, len(q) + 1)
            sl.add(pre[i])
            q.append(pre[i])

        return res if res != inf else -1



