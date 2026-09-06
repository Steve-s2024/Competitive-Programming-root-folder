# pure guessing. the pattern is easily spotted by printing the prefix xor (1^2^3^4...)
def solve():
    M = 998244353
    n, x = [int(e) for e in input().split()]

    res = ((x//4+1) * ((n+1)//4-x//4)) % M

    def helper(n): return (n+3)//4
    res += (helper(x-1) * (helper(n)-helper(x-1))) % M

    print(res%M)


for _ in range(int(input())): solve()