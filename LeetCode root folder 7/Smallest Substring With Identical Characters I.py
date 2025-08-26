# first I thought its knapsack, but its binary search and greedy, also need to take special care of when result is 1: 42%
class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        n = len(s)
        l, r = 2, n
        res = -1
        while l <= r:
            m = (l + r) // 2
            tmp = list(s)
            j = 0
            cnt = 0
            for i in range(n):
                if tmp[i] != tmp[j]: j = i
                if i - j + 1 > m:
                    if i == n - 1 or tmp[i] == tmp[i + 1]:
                        tmp[i] = '0' if tmp[i] == '1' else '1'
                        j = i
                    else:
                        tmp[i - 1] = '0' if tmp[i] == '1' else '1'
                        j = i
                    cnt += 1
            # print(m, cnt, numOps)
            # print(tmp)
            if cnt <= numOps:
                res = m
                r = m - 1
            else:
                l = m + 1

        cnt1, cnt2 = 0, 0
        for i in range(n):
            if i % 2 == 0 and s[i] != '0': cnt1 += 1
            if i % 2 == 1 and s[i] != '1': cnt1 += 1
            if i % 2 == 0 and s[i] != '1': cnt2 += 1
            if i % 2 == 1 and s[i] != '0': cnt2 += 1

        if min(cnt1, cnt2) <= numOps: return 1
        return res