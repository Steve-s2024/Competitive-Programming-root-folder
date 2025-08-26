# so funny that it looks so impossible at first 28/571 accepts, but turn out only a bit tricky greedy solution

class Solution:
    def maxTotal(self, value: List[int], limit: List[int]) -> int:
        zp = list(zip(value, limit))
        zp.sort(key = lambda i:(i[1], -i[0]))
        print(zp)

        n = len(zp)
        res = 0
        i = 0
        j = 0
        cnt = 0
        while i < n:
            res += zp[i][0]
            cnt += 1
            if cnt == zp[j][1]:
                tmp = zp[j][1]
                while j <= i and zp[j][1] == tmp:
                    cnt -= 1
                    j += 1
                while j < n and zp[j][1] == tmp: j += 1
                old = i
                while i < n and zp[i][1] == tmp: i += 1
                if i == old: i += 1
            else: i += 1
        return res
