# brainless brute force with hash map, key is to realize k <= 100 is small enough to support the brute force: 100%
class Solution:
    def countPairs(self, coordinates: List[List[int]], k: int) -> int:
        mp = {}
        n = len(coordinates)
        res = 0
        for i in range(n):
            a, b = coordinates[i]
            for j in range(k + 1):
                # c and d will be the second coors when a^c = j and b^d = k-j
                c, d = j ^ a, (k - j) ^ b
                if c in mp: res += mp[c][d]
            if a not in mp: mp[a] = defaultdict(int)
            mp[a][b] += 1
        return res

