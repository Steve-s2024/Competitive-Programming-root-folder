# funny problem, light work greedy solution: 55%
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        if k == 1: return 0
        arr = [weights[i] + weights[i+1] for i in range(n-1)]
        arr.sort()
        # print(arr)
        # print(k-1)
        return sum(arr[-(k-1):]) - sum(arr[:k-1])