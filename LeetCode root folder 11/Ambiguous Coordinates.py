# some of the early mediums are just so fking boring
class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        s = s[1:-1]

        def helper(s):
            res = []
            if s == '0' or s[0] != '0': res.append(s)
            ar = []
            for i in range(1, len(s)):
                ar.append(s[:i] + '.' + s[i:])
            for v in ar:
                if v[-1] == '0' or (v[0] == '0' and v[1] != '.'): continue
                res.append(v)
            return res

        n = len(s)
        ans = []
        for i in range(n):
            a, b = s[:i], s[i:]
            if not a or not b: continue
            ar, br = helper(a), helper(b)
            # print(a, b, ar, br)
            for v1 in ar:
                for v2 in br:
                    ans.append(f'({v1}, {v2})')
        return ans