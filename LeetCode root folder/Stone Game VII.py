

# depricated
class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        dp = {}
        total = sum(stones)
        def recursive(i, j, total, a, b, turn):
            if (i, j) in dp:
                return dp[(i, j)]
            if i > j:
                return a-b
            if turn:
                res = min(
                    recursive(i+1, j, total-stones[i], a+total-stones[i], b, not turn),
                    recursive(i, j-1, total-stones[j], a+total-stones[j], b, not turn)
                )
            else:
                res = min(
                    recursive(i+1, j, total-stones[i], a, b+total-stones[i], not turn),
                    recursive(i, j-1, total-stones[j], a, b+total-stones[j], not turn)
                )
            dp[(i, j)] = res
            return res

        n = len(stones)
        recursive(0, n-1, total, 0, 0, True)
        print(dp)
        return 0