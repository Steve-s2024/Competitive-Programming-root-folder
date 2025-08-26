# sob i didn't know below 5% is even possible, but still happy to conceive this brilliant solution: 4.11%
class Solution:
    def getChar(self, mp, cands):
        mi = 'z'
        for cand in cands:
            flag = 1
            for other in cands:
                if mp[other][-1] < mp[cand][0]: flag = 0
            if flag: mi = min(mi, cand)

        for cand in cands:
            while mp[cand][0] < mp[mi][0]: mp[cand].popleft()

        cands.remove(mi)
        return mi

    def smallestSubsequence(self, s: str) -> str:
        n = len(s)
        mp = defaultdict(deque)
        for i, c in enumerate(s):
            mp[c].append(i)

        cands = set(mp.keys())
        size = len(cands)
        strarr = []
        for i in range(size):
            c = self.getChar(mp, cands)
            strarr.append(c)

        return ''.join(strarr)





# a good try
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        n = len(s)
        mp = Counter(s)

        frq = defaultdict(int)
        q = deque()
        strarr = []
        for i in range(n):
            q.append(s[i])
            frq[s[i]] += 1
            mp[s[i]] -= 1
            while mp[s[i]] == 0 and s[i] in frq:
                # stop increment, find the current smallest candidate
                mi = min(frq.keys())
                while q[0] != mi:
                    c = q.popleft()
                    frq[c] -= 1
                    if frq[c] == 0: frq.pop(c)
                c = q.popleft()
                frq[c] -= 1
                if frq[c] == 0: frq.pop(c)
                strarr.append(c)

        vis = set()
        for i in range(len(strarr)):
            if strarr[i] in vis:
                strarr[i] = ''
            else:
                vis.add(strarr[i])

        return ''.join(strarr)
