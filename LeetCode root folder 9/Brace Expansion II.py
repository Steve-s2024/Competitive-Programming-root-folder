# not hard, but difficult. did the same approach in early expression parsing solution (basic calculator style)
# it is just very brain-recking
class Solution:
    def braceExpansionII(self, exp: str) -> List[str]:
        n = len(exp)
        stk = []
        mp = {}
        for i in range(n):
            if exp[i] == '{':
                stk.append(i)
            elif exp[i] == '}':
                mp[stk.pop()] = i

        def recursive(l, r):
            res = []
            cr = set()
            i = l
            ar = []
            while i <= r:
                if exp[i] == '{':
                    if ar:
                        res.append(({''.join(ar)}, '*'))
                        ar = []
                    cr = recursive(i + 1, mp[i] - 1)
                    i = mp[i]
                    res.append((cr, '+' if i + 1 > n - 1 or exp[i + 1] == ',' else '*'))
                elif exp[i] == ',':
                    if ar:
                        s = ''.join(ar)
                        cr = {s}
                        res.append((cr, '+'))
                        ar = []
                else:
                    ar.append(exp[i])
                i += 1
            if ar:
                s = ''.join(ar)
                cr = {s}
                res.append((cr, '_'))
            st = set()
            cr, op1 = res[0]
            for i in range(len(res) - 1):
                nxt, op2 = res[i + 1]
                if op1 == '+':
                    for v in cr: st.add(v)
                    cr = nxt
                else:
                    tmp = list(cr)
                    cr = set()
                    for v in tmp:
                        for v2 in nxt: cr.add(v + v2)
                op1 = op2
            st = st.union(cr)
            # print(l, r, res)
            # print(st)
            return st

        res = recursive(0, n - 1)
        # print(res)
        return list(sorted(res))