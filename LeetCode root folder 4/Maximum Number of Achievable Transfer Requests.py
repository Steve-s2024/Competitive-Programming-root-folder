# when i saw the constraint, I just discarded the cycle detection solution and
# focus on the brute force dfs: 32%
class Solution:
    @staticmethod
    def check(stk, n):
        arr = [0] * n
        for u, v in stk:
            arr[u] -= 1
            arr[v] += 1
        return max(arr) == min(arr) == 0

    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        stk = []
        res = 0

        def recursive(i):
            nonlocal res, n
            if i >= len(requests):
                if Solution.check(stk, n): res = max(res, len(stk))
                return
            recursive(i + 1)
            stk.append(requests[i])
            recursive(i + 1)
            stk.pop()

        recursive(0)
        return res