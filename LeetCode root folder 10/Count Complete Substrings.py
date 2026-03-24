# no use of data structure, just index manipulation (very tough question)

class Solution:
    def countCompleteSubstrings(self, word: str, k: int) -> int:
        ar = [ord(c)-ord('a') for c in word]
        n = len(ar)
        mp = [[] for _ in range(26)]
        res = 0
        lw = 0
        for i in range(n):
            if i and abs(ar[i]-ar[i-1]) > 2: lw = i
            mp[ar[i]].append(i)
            tp = []
            for j, v in enumerate(mp):
                if not v: continue
                tp.append((v[-1], j))
            tp.sort(reverse = True)

            mx = -1
            mi = n
            for I in range(len(tp)):
                v, j = tp[I]
                if len(mp[j]) < k: break
                if len(mp[j]) > k: mx = max(mx, mp[j][-k-1])
                mi = min(mi, mp[j][-k])
                if mi < lw or mi <= mx: break
                x = mp[tp[I+1][1]][-1] if I < len(tp)-1 else -1
                if mi > x: res += 1
        return res