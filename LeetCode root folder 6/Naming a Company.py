# credit to NeetCode: 42%
class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        n = len(ideas)
        mp = defaultdict(set)
        for i in range(n):
            a = ideas[i]
            mp[a[0]].add(a[1:])

        # print(mp)
        res = 0
        ref = 'qwertyuiopasdfghjklzxcvbnm'
        for i in range(26):
            for j in range(i + 1, 26):
                cnt = 0
                for val in mp[ref[i]]:
                    if val in mp[ref[j]]: cnt += 1
                tot = (len(mp[ref[i]]) - cnt) * (len(mp[ref[j]]) - cnt)
                tot *= 2
                res += tot
        return res