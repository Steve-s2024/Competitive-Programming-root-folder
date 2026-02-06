# to avoid anti-hashing testcase

def solve():
    n = int(input())
    nums = sorted([int(e) for e in input().split()])
    for i in range(n - 1):
        if nums[i] == nums[i + 1]: nums[i] = -1
    tmp = []
    for i in range(n):
        if nums[i] == -1: continue
        tmp.append(nums[i])
    nums = tmp

    ar = [1 << 31] * (n + 1)
    st = [0] * (n + 1)
    for v in nums:
        ar[v] = 1
        st[v] = 1
    if nums[0] == 1: nums = nums[1:]

    for i in range(len(nums)):
        f = nums[i]
        x = f
        i = 1
        while x <= n:
            tmp = []
            for v in range(1, n + 1):
                t = x * v
                if t > n: break
                if st[v] == 0: continue
                ar[t] = min(ar[t], ar[v] + i)
                tmp.append(t)
            for t in tmp: st[t] = 1
            x *= f
            i += 1

    for i in range(1, n + 1):
        if ar[i] == 1 << 31: ar[i] = -1
    ar = ar[1:]
    # print(ar)
    print(' '.join(str(e) for e in ar))


for _ in range(int(input())): solve()

# stroke of genius 😝, how smart I must be to invent this nlog^2n approach out of thin air.
# this is probably some well known math algorithm of finding minimum decomposition element count
# key idea is brute force over choices & harmonic series reduce time complexity

def solve():
    n = int(input())
    nums = sorted(set([int(e) for e in input().split()]))
    ar = [1<<31]*(n+1)
    st = [0]*(n+1)
    for v in nums:
        ar[v] = 1
        st[v] = 1
    if nums[0] == 1: nums = nums[1:]

    for i in range(len(nums)):
        f = nums[i]
        x = f
        i = 1
        while x <= n:
            tmp = []
            for v in range(1, n+1):
                t = x*v
                if t > n: break
                if st[v] == 0: continue
                ar[t] = min(ar[t], ar[v]+i)
                tmp.append(t)
            for t in tmp: st[t] = 1
            x *= f
            i += 1

    for i in range(1, n+1):
        if ar[i] == 1<<31: ar[i] = -1
    ar = ar[1:]
    # print(ar)
    print(' '.join(str(e) for e in ar))

for _ in range(int(input())): solve()