# two pointer solution, greedy: 70%
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        if len(tokens) == 0:
            return 0
        tokens.sort()
        score = 0
        n = len(tokens)
        res = 0
        l, r = 0, n - 1
        while True:
            while l < n and power >= tokens[l]:
                power -= tokens[l]
                score += 1
                l += 1
            res = max(res, score)
            if score:
                score -= 1
                power += tokens[r]
                r -= 1
            else:
                break
            if l - 1 >= r + 1:
                break
        return res




