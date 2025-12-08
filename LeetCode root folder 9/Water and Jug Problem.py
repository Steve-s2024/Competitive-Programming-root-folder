# this got to be the weirdest shaped code I ever wrote on leetcode

class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        dp = set()

        def recursive(a, b):
            nonlocal x, y
            state = (a, b)
            if state in dp: return
            dp.add(state)
            recursive(0, b)
            recursive(a, 0)
            mi = min(x - a, b)
            recursive(a + mi, b - mi)
            mi = min(y - b, a)
            recursive(a - mi, b + mi)
            recursive(x, b)
            recursive(a, y)

        recursive(0, 0)
        # print(dp)
        for a, b in dp:
            if a+b == target: return True
        return False
