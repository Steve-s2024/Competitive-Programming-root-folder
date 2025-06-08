# turns out I made a silly mistake, and double counting the result, only need to change the order of the line
# tot += tot and two += tot for it to work, now its ten times faster
def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]
    MOD = 998244353

    two = 0
    tot = 0
    res = 0
    for i in range(n):
        if nums[i] == 1:
            tot += 1
        if nums[i] == 2:
            two += tot
            two %= MOD
            tot += tot
            tot %= MOD

        if nums[i] == 3:
            res += two
            res %= MOD

    print(int(res))




t = int(input())
for i in range(t):
    solve()

# love python, it didn't even hit TLE, I almost thought it will
# python big int is magical.
# I can't use modulo during the operations, and therefore can't reduce time, because for some reason this
# algorithm spit out 2 * the actual value, and if I did modulo before the res//2 (the last line), it will sometimes
# not be the right answer

def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]
    MOD = 998244353

    two = 0
    tot = 0
    res = 0
    for i in range(n):
        if nums[i] == 1:
            tot += 1
        if nums[i] == 2:
            tot += tot
            two += tot
        if nums[i] == 3:
            res += two

    print(res//2 % MOD)




# greedy solution, but don't know why its not working
# as expected

def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]
    MOD = 998244353

    one = two = 0

    tot = 0
    res = 0
    for i in range(n):
        if nums[i] == 1:
            one += 1
        if nums[i] == 2:
            tot += one
            two += tot
        if nums[i] == 3:
            res += two
        print(one, two, tot, res)

    print(res)