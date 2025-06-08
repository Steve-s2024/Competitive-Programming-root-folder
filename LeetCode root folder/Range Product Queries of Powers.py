# boring question, prefix sum:103
# ms
# Beats
# 35.84%

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        ans = []
        toTheLeft = []
        total = 0
        cur = 0
        for c in list(str(bin(n))[2:])[::-1]:
            if int(c):
                total += cur
                toTheLeft.append(total)
            cur += 1

        # print(toTheLeft)
        for l, r in queries:
            pow_ = toTheLeft[r] - (toTheLeft[l-1] if l > 0 else 0)
            ans.append(pow(2, pow_) % (pow(10, 9) + 7))
        return ans
