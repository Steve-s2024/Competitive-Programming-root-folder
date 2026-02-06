# never have so such fun doing a problem, this is more like a quiz than a real problem. the solution is just funny
# and stupid

class Solution:
    def originalDigits(self, s: str) -> str:
        mp = Counter(s)

        def helper(word, x, mp):
            res = mp[x]
            for c in word: mp[c] -= res
            return res

        ref = [(0, 'zero', 'z'), (8, 'eight', 'g'), (6, 'six', 'x'), (7, 'seven', 's'), (5, 'five', 'v'), (4, 'four', 'f'), (2, 'two', 'w'), (1, 'one', 'o'), (3, 'three', 't'), (9, 'nine', 'i')]
        ans = []
        for num, word, x in ref:
            for _ in range(helper(word, x, mp)):
                ans.append(num)

        ans.sort()
        return ''.join(str(e) for e in ans)