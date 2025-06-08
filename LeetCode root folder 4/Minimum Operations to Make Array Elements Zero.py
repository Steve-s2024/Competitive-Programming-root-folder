# I'm pro! greedy and neet: 66%
class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        res = 0
        for l, r in queries:
            prev = l
            tmp = 1
            cnt = 0
            tot = 0
            while True:
                if tmp - 1 >= prev:
                    tot += cnt * (min(r + 1, tmp) - prev)
                    prev = tmp
                if tmp >= r + 1:
                    break
                tmp *= 4
                cnt += 1

            # print(tot)
            res += (tot + 1) // 2
        return res

