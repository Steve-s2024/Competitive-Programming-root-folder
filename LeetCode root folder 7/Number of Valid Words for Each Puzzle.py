# thought brute force will tle, but this brute force will not: 41%
class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        mp = defaultdict(int)
        n = len(words)
        for i in range(n):
            mask = 0
            for c in words[i]:
                cnt = ord(c) - ord('a')
                mask |= (1 << cnt)
            mp[mask] += 1

        def recursive(i, mask, s):
            if i >= len(s): return mp[mask]
            crr = ord(s[i]) - ord('a')
            return (
                recursive(i + 1, mask, s) +
                recursive(i + 1, mask | (1 << crr), s)
            )

        ans = []
        for p in puzzles:
            ans.append(recursive(1, 1<<(ord(p[0])-ord('a')), p))
        return ans
