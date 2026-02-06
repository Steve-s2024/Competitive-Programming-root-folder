# still can't believe I can pull this off all by myself. this feel like the most brain-racking task.
# solving this one problem feel like solving 2,3 mediums combined in a complicated way
class Solution:
    def countOfAtoms(self, frmu: str) -> str:
        s = frmu
        news = [s[0]]
        for i in range(1, len(frmu)):
            if ('A' <= s[i] <= 'Z' or s[i] in '()') and ('a' <= s[i - 1].lower() <= 'z' or s[i - 1] == ')'):
                news.append('1')
            news.append(s[i])
        if news[-1] not in '0123456789': news.append('1')
        frmu = ''.join(news)
        n = len(frmu)

        stk = []
        mp = {}
        for i in range(n):
            if frmu[i] == '(':
                stk.append(i)
            elif frmu[i] == ')':
                mp[stk.pop()] = i
        # print(frmu)
        # print(mp)

        def recursive(l, r):
            frq = defaultdict(int)
            nameAr, ctAr = [], []
            i = l
            tmp = {}
            while i <= r:

                if 'a' <= frmu[i].lower() <= 'z':
                    nameAr.append(frmu[i])
                elif '0' <= frmu[i] <= '9':
                    ctAr.append(frmu[i])

                if i > l and frmu[i] in '0123456789' and 'a' <= frmu[i - 1].lower() <= 'z':
                    tmp = {''.join(nameAr): 1}
                    nameAr = []

                if i > l and frmu[i] not in '0123456789' and frmu[i - 1] in '0123456789':
                    ct = int(''.join(ctAr))
                    ctAr = []
                    for key, val in tmp.items(): frq[key] += val * ct

                # print(nameAr, ctAr, tmp)
                if frmu[i] == '(':
                    tmp = recursive(i + 1, mp[i] - 1)
                    # print(tmp)
                    i = mp[i]

                i += 1
            ct = int(''.join(ctAr))
            for key, val in tmp.items(): frq[key] += val * ct
            return frq

        frq = recursive(0, n - 1)
        # print(frq)
        ans = list(frq.items())
        ans.sort()
        return ''.join(e[0] + (str(e[1]) if e[1] != 1 else '') for e in ans)