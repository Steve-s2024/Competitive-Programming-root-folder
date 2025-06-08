# brute force:
class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        row, col = len(mana), len(skill)
        res = [[0] * col for i in range(2)]
        cur = 0
        for c in range(col):
            cur += mana[0] * skill[c]
            res[0][c] = cur

        for r in range(1, row):
            for c in range(col):
                cur += mana[r] * skill[c]
                res[1][c] = cur

            min_ = float('inf')
            for c in range(col - 1):
                diff = res[1][c] - res[0][c + 1]
                min_ = min(min_, diff)

            # res[r][0] - (mana[r] * skill[0]) >= res[r-1][0]
            # res[r][0] - res[r-1][0] >= (mana[r] * skill[0])
            min_ = min(min_, res[1][0] - (res[0][0] + mana[r] * skill[0]))
            for c in range(col):
                res[1][c] -= min_
            res.pop(0)
            res.append([0] * col)
        # print(res)
        return res[0][col - 1]

