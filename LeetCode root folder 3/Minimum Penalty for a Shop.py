# easy prefix suffix implementation, all about problem simplification
# (interpret it to easier alternate problem): 33.33%
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        prefix = []
        cnt = 0
        for i in range(n):
            if customers[i] == 'N':
                cnt += 1
            prefix.append(cnt)
        suffix = [0] * n
        cnt = 0
        for i in range(n-1, -1, -1):
            if customers[i] == 'Y':
                cnt += 1
            suffix[i] = cnt

        min_ = suffix[0]
        res = 0
        for i in range(1, n):
            penalty = prefix[i-1] + suffix[i]
            if penalty < min_:
                min_ = penalty
                res = i
        if prefix[-1] < min_:
            res = n
        return res