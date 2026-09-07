# beat 100% faster than the current fastest?? wow


class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        trie = {}
        for i in range(len(paths)):
            cr = trie
            for j in range(len(paths[i])):
                c = paths[i][j]
                if c not in cr: cr[c] = {}
                cr = cr[c]

        mp = {'':0}
        st = set()
        def dfs(cr):
            if not cr: return mp['']

            ar = []
            for v, nxt in cr.items():
                x = dfs(nxt)
                ar.append(v+str(x))
            ar.sort()
            s = ''.join(ar)
            if s not in mp: mp[s] = len(mp)
            else: st.add(s)
            cr['*'] = s
            return mp[s]
        dfs(trie)
        # print(st)

        ans = []
        stk = []
        def fn(cr):
            if cr and cr['*'] in st: return
            ans.append(stk[:])
            if not cr: return
            for v, nxt in cr.items():
                if v == '*': continue
                stk.append(v)
                fn(nxt)
                stk.pop()
        fn(trie)
        return ans[1:]