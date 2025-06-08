# greedy solution:0
# ms
# Beats
# 100.00%
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        res = ''
        cur = 1
        pattern += 'I'
        ref = 0
        for p in pattern:
            if p == 'I':
                count = cur
                while count > ref:
                    res += str(count)
                    count -= 1
                ref = cur
            cur += 1
        # print(res)
        return res
