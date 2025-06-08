# bit manipulation solution:1099
# ms
# Beats
# 6.05%
class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        hashMap = defaultdict(int)
        for cand in candidates:
            i = 0
            for c in str(bin(cand))[2:][::-1]:
                hashMap[i] += int(c)
                i += 1
        return max(hashMap.values())