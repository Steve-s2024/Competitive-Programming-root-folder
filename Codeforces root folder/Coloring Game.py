

#TLE
def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]
    nums.sort()

    stk = []
    def recursive(i, k):
        if k == 0:
            if stk[0]+stk[1] > stk[2] and sum(stk) > nums[-1]: return 1
            return 0
        if i >= n: return 0
        res = 0
        stk.append(nums[i])
        res += recursive(i+1, k-1)
        stk.pop()
        res += recursive(i+1, k)
        return res

    print(recursive(0, 3))

t = int(input())
for i in range(t):
    solve()



