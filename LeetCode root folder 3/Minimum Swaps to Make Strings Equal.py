# not easy question, the greedy solution: 25%

class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        n = len(s1)
        cnt1, cnt2 = 0, 0
        for i in range(n):
            if s1[i] == 'x' and s2[i] == 'y':
                cnt1 += 1
            if s2[i] == 'x' and s1[i] == 'y':
                cnt2 += 1

        return cnt1 // 2 + cnt2 // 2 + (cnt1 % 2 + cnt2 % 2) if Counter(s1 + s2)['x'] % 2 == 0 else -1