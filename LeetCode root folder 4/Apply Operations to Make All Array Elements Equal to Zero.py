# pretty intuitive solution, once realize that start from boundary and shrinking greedily (also very simple code)
#: 53%
class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        if k == 1: return True
        n = len(nums)
        q = deque()
        tot = 0
        for i in range(n):
            if len(q) == k: tot -= q.popleft()

            x = nums[i] - tot
            if x < 0: return False
            tot += x
            q.append(x)

        return q[-1] == 0