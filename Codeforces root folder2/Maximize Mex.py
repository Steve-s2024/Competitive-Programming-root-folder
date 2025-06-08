# greedy solution with the help of hashing
def solve():
    n, x = [int(e) for e in input().split()]
    nums = [int(e) for e in input().split()]
    nums.sort()
    prev = nums[0]
    best = set()
    best.add(nums[0])
    dup = defaultdict(deque)
    for i in range(1, n):
        if nums[i] == prev:
            dup[nums[i]%x].append(nums[i])
        else:
            best.add(nums[i])

        prev = nums[i]
    # print(best, dup)
    prev = -1
    while True:
        cur = prev+1
        if cur not in best:
            tar = prev+1
            remain = tar%x
            if dup[remain] and dup[remain][0] < tar:
                dup[remain].popleft()
            else:
                break

        prev += 1
    print(prev+1)



t = int(input())
for i in range(t):
    solve()
