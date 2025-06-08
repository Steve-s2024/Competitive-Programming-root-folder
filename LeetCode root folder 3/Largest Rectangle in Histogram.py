# the classic hard question, I can't remember the solution, what
# manage to come up with a very simple mono-stack solution. very nice
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        lMp, rMp = {}, {}
        for i in range(n - 1, -1, -1):
            while stack and stack[-1][0] > heights[i]:
                val, idx = stack.pop()
                lMp[idx] = i

            stack.append((heights[i], i))

        stack = []
        for i in range(n):
            while stack and stack[-1][0] > heights[i]:
                val, idx = stack.pop()
                rMp[idx] = i

            stack.append((heights[i], i))

        res = 0
        for i in range(n):
            l, r = lMp[i] if i in lMp else -1, rMp[i] if i in rMp else n
            res = max(res, heights[i] * (r - l - 1))
        return res