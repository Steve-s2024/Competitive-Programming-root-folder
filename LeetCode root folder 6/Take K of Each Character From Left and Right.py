# sliding window solution: 5%
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0: return 0
        arr = [0, 0, 0]
        for c in s:
            arr[ord(c) - ord('a')] += 1

        n = len(s)
        j = -1
        res = inf
        comp = [0, 0, 0]
        for i in range(n):
            while all(arr[i] - comp[i] >= k for i in range(3)):
                j += 1
                if j >= n: break
                comp[ord(s[j]) - ord('a')] += 1
            res = min(n - (j - i), res)
            comp[ord(s[i]) - ord('a')] -= 1

        return res if res <= n else -1
