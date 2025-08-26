#

def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]
    cnt = 0
    for i in range(n):
        if i%2 == 1:
            # even position
            tot = (nums[i-1] if i else 0) + (nums[i+1] if i<n-1 else 0)
            if tot > nums[i]:
                diff = tot-nums[i]
                if i < n-1:
                    a = min(diff, nums[i+1])
                    nums[i+1] -= a
                    cnt += a
                    diff -= a
                if i and diff:
                    a = min(diff, nums[i-1])
                    nums[i-1] -= a
                    cnt += a
    print(cnt)



t = int(input())
for i in range(t):
    solve()
