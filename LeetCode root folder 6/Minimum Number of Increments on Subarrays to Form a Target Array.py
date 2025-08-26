# pretty funny greedy solution, its like counting climbing distance: 20%
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        res = target[0]
        for i in range(1, len(target)):
            a, b = target[i-1], target[i]
            res += max(0, b-a)
        return res