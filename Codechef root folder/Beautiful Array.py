# solved in constant time, if you don't count the sum and hash map towards time complexity
# its just wierd to see problem that can be solved this way to even
# be a programming question, maybe it should instead be a math problem
from collections import Counter


def solve():
    n = int(input())
    nums = [int(e) % 4 for e in input().split(' ')]
    if sum(nums) % 4 != 0:
        print(-1)
    else:
        frqMp = Counter(nums)
        # print(frqMp)
        a, b, c = frqMp[1], frqMp[2], frqMp[3]
        res = 0
        tmp = min(a, c)
        res += tmp
        a -= tmp
        c -= tmp
        tmp = b // 2
        res += tmp
        b -= 2 * tmp
        if b:
            a -= 2
            c -= 2
            a = max(0, a)
            c = max(0, c)
            b = 0
            res += 2
        res += 3 * (a // 4)
        res += 3 * (c // 4)

        print(res)


t = int(input())
for tt in range(t):
    solve()