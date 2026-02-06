# definitely a tough C and with misleading description
# after realize what the problem statement really means, I start to try to come up with an efficient code with prefix sum
# after so long I feel like this is way too hard for a C, then I double-checked the "brute-force" solution, but its complexity
# is actually not what I expected... its linear and intended


def solve():
    n, w = [int(e) for e in input().split()]
    nums = [int(e) for e in input().split()]
    if w >= n:
        print(0)
        return

    sm = 0
    for i in range(w, n, 2*w):
        for j in range(i, min(i+w, n)): sm += nums[j]

    res = sm
    for i in range(2*w):
        for j in range(i, n, 2*w): sm += nums[j]
        x = (i+w) if i < w else (i-w)
        for j in range(x, n, 2*w): sm -= nums[j]
        res = min(res, sm)

    print(res)



for _ in range(int(input())): solve()