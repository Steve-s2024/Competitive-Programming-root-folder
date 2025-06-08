# i actually have an improvement idea with prefix sum to calc
# the frqMp in O(26) --> O(1) time, but don't feel the need to
# implement it anymore.

# I absolutely have zero hope that this will not hit TLE, but
# magically it passed... I guess is because the worst case didn't
# included in the testcases, otherwise the complexity can reach
# O(n^2), or maybe I made a mistake analysing the complexity: 80%
class Solution:
    def minAnagramLength(self, s: str) -> int:
        ref = defaultdict(int)
        for c in s:
            ref[c] += 1

        n = len(s)
        for i in range(1, n+1):
            if n % i == 0:
                for j in range(0, n, i):
                    frqMp = Counter(s[j:j+i])
                    for letter, frq in frqMp.items():
                        if ref[letter] / (n/i) != frq:
                            break
                    else:
                        continue
                    break
                else:
                    return i
