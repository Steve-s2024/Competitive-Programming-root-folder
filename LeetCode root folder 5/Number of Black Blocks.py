# bona fide retard question:18%
class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        mp = defaultdict(int)
        for r, c in coordinates:
            for R, C in [(r - 1, c - 1), (r - 1, c), (r, c - 1), (r, c)]:
                if R in range(m - 1) and C in range(n - 1):
                    mp[(R, C)] += 1

        tot = (m - 1) * (n - 1)
        ans = [0] * 5
        for val in mp.values():
            ans[val] += 1
        ans[0] = tot - sum(ans)
        return ans