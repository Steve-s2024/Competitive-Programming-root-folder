# greedy solution, I have no idea as to why it works: 50%

class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        q = deque()
        res = 0
        for i in range(n - k + 1):
            if q and q[0] <= i: q.popleft()
            cnt = len(q)
            if (nums[i] + cnt) % 2 != 1:
                res += 1
                q.append(i + k)
                # print(res)
        for i in range(n - k + 1, n, 1):
            if q and q[0] <= i: q.popleft()
            if (len(q) + nums[i]) % 2 == 0: return -1

        return res