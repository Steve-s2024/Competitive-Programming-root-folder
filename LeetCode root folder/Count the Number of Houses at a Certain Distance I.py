# greedy solution:150
# ms
# Beats
# 76.64%
class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        hashMap = defaultdict(int)
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                # i - j
                # "(y - x)" 1 + abs(i-x) + abs(j-y)
                # "(y - x)" 1 + abs(j-x) + abs(i-y)
                minDist = min(
                    j - i,
                    1 + abs(i-x) + abs(j-y),
                    1 + abs(j-x) + abs(i-y)
                )
                hashMap[minDist] += 2

        ans = []
        for i in range(1, n+1):
            ans.append(hashMap[i])
        return ans
