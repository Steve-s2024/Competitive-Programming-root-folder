# solution no.1: Memory Limit Exceeded
class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        rows = defaultdict(int)
        hashSet = set()
        for x, y, side in squares:
            for i in range(y, y+side):
                rows[i] += side
                if i not in hashSet:
                    hashSet.add(i)

        arr = sorted(list(hashSet))
        sum_ = sum(rows.values())
        total = 0
        for row in arr:
            val = rows[row]
            sum_ -= val
            total += val
            if sum_ <= total:
                res = row
                diff = total - sum_
                res -= (diff / 2.0) / val
                res += 1
                return res
