# almost exactly the same as 2262, I just copied the solution from there and made one adjustment: 36%
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        n = len(s)
        mp = defaultdict(list)
        for i in range(n):
            if s[i] not in mp: mp[s[i]].append(-1)
            mp[s[i]].append(i)
        for val in mp.values(): val.append(n)
        res = 0
        for val in mp.values():
            for i in range(1, len(val)-1):
                a, b, c = val[i-1], val[i], val[i+1]
                l, r = b-a, c-b
                res += l*r
        # print(res)
        return res