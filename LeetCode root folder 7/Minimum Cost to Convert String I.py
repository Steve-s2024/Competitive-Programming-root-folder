# why is it slow when using optimal solution, Floyd Warshall? cause I used the recursive Floyd Warshall: 10%
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        n = len(original)
        size = 26
        mp = [[inf] * size for _ in range(26)]
        for i in range(n):
            a, b = original[i], changed[i]
            a, b = ord(a) - ord('a'), ord(b) - ord('a')
            mp[a][b] = min(mp[a][b], cost[i])

        for i in range(size): mp[i][i] = 0

        @cache
        def recursive(i, j, k):
            if k == -1: return mp[i][j]
            a = recursive(i, j, k - 1)
            b = recursive(i, k, k - 1) + recursive(k, j, k - 1)
            return min(a, b)

        # for i in range(size):
        #     for j in range(i+1, size):
        #         recursive(i, j, size-1)
        m = len(source)
        res = 0
        for i in range(m):
            a, b = source[i], target[i]
            a, b = ord(a) - ord('a'), ord(b) - ord('a')
            cost = recursive(a, b, size - 1)
            if cost == inf: return -1
            res += cost

        return res