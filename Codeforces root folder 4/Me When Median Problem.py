# mothfker shit is hard, it is so insanely difficult to prove the monotonicity of answer (by converting to binar array)
# and it is very hard to figure out the O(n) solution to binary array (by stack)

def solve():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    ans = -1
    l, r = 0, max(max(A), max(B))
    while l <= r:
        m = (l+r)//2
        ar, br = [], []
        res = False
        for i in range(n):
            a, b = A[i], B[i]
            ar.append(1 if a >= m else 0)
            br.append(1 if b >= m else 0)
        # ar and br is binary array
        ct = 0
        f = 1
        pre = [0]*n
        for i in range(n):
            a, b = ar[i], br[i]
            pre[i] = ct
            if a == b:
                if a: ct += 1
                elif f == 1: ct -= 1
                f = a

        f = 1
        for i in range(n-1, -1, -1):
            a, b = ar[i], br[i]
            if a == b == 1 and ct>=0 and pre[i]>=0:
                res = True
                break
            if a == b:
                if a: ct += 1
                elif f == 1: ct -= 1
                f = a



        if res:
            ans = m
            l = m+1
        else: r = m-1
    print(ans)

for _ in range(int(input())): solve()
