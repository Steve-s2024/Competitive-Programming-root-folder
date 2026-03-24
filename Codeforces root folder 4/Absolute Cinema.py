# div3 D, but pretty tricky. double difference array plus a lot of summation manipulation
def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]
    dif = []
    for i in range(n-1): dif.append(nums[i+1]-nums[i])

    res = []
    for i in range(n-2): res.append((dif[i+1]-dif[i]) // 2)
    # print(res)
    sm = 0
    for i in range(n-2): sm += (i+1)*res[i]
    # print(sm)

    x = nums[0] - sm
    # x = (n-1)*seq[-1]
    res.append(x//(n-1))
    # seq[0] = f(2) - f(1) + sum(res)
    fst = nums[1] - nums[0] + sum(res)
    res = [fst] + res
    # print(res)

    print(' '.join(str(e) for e in res))

for _ in range(int(input())): solve()

