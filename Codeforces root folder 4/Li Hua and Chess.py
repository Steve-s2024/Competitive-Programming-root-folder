# rarely see O(1) solution
# greedy greedy okey-dokey

def query(r, c):
    print(f'? {r} {c}')
    stdout.flush()
    x = int(input())
    if x == -1: exit(114514)
    return x

def solve():
    n, m = [int(e) for e in input().split()]
    a, b = query(1, 1), query(n, m)
    if a+b == n-1 != m-1: # on ath row
        print(f'! {a+1} {query(a+1, 1)+1}')
        return
    if a+b == m-1 != n-1: # on ath col
        # print('Yes')
        print(f'! {query(1, a+1)+1} {a+1}')
        return


    r, c = a+1, m-b
    if r in range(1, n+1) and c in range(1, m+1) and query(r, c) == 0: print(f'! {r} {c}')
    else: print(f'! {n-b} {r}')





for _ in range(int(input())): solve()
