



# brute force game theory solution: TLE
class Solution:
    def sumGame(self, num: str) -> bool:
        mp = Counter(num)
        if '?' in mp:
            if mp['?'] % 2 == 1:
                return True
            else:
                n = len(num)
                cnt1, cnt2 = 0, 0
                l, r = 0, 0
                for i in range(n // 2):
                    if num[i] == '?':
                        cnt1 += 1
                    else:
                        l += int(num[i])
                for i in range(n // 2, n):
                    if num[i] == '?':
                        cnt2 += 1
                    else:
                        r += int(num[i])

                def recursive(i, tot1, tot2):
                    nonlocal cnt1, cnt2, l, r
                    if cnt1 == cnt2 == 0:
                        return abs(l + tot1 - tot2 - r)

                    mx, mi = 0, float('inf')
                    for j in range(10):
                        if cnt1:
                            cnt1 -= 1
                            a = recursive(i + 1, tot1 + j, tot2)
                            mx = max(mx, a)
                            mi = min(mi, a)
                            cnt1 += 1
                        if cnt2:
                            cnt2 -= 1
                            a = recursive(i + 1, tot1, tot2 + j)
                            mx = max(mx, a)
                            mi = min(mi, a)
                            cnt2 += 1
                    if i % 2 == 0:
                        # alice
                        return mx
                    else:
                        # bob
                        return mi

            return recursive(0, 0, 0) != 0
        else:
            n = len(num)
            l, r = 0, 0
            for i in range(n // 2):
                l += int(num[i])
            for i in range(n // 2, n):
                r += int(num[i])
            return l != r