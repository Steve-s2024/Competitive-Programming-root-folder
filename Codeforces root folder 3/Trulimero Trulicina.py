# used the below approach idea and the hint from tutorial, here is the working version of it
def solve():
    n, m, k = [int(e) for e in input().split()]
    grid = [[0]*m for _ in range(n)]
    cnt = 1
    if m%k != 0:
        for i in range(n):
            for j in range(m):
                grid[i][j] = cnt
                cnt %= k
                cnt += 1
    elif n%k != 0:
        for j in range(m):
            for i in range(n):
                grid[i][j] = cnt
                cnt %= k
                cnt += 1
    else:
        q = deque([i for i in range(1, k+1)])
        for i in range(n):
            for j in range(m//k):
                print(' '.join(str(e) for e in q), end=' ')
            print()
            q.append(q.popleft())
        return
    for r in grid:
        print(' '.join(str(e) for e in r))

t = int(input())
for i in range(t):
    solve()




# some flaw exist in the approach
def solve():
    n, m, k = [int(e) for e in input().split()]
    if n == 1:
        print(' '.join([str(e) for e in range(1, k+1)]*(n*m//k)))
        return
    if m == 1:
        for i in range(n*m//k):
            for j in range(1, k+1):
                print(j)
        return

    arr = []
    for i in range(1, k+1):
        for j in range(n*m//k): arr.append(i)

    grid = [[0]*m for _ in range(n)]
    idx = 0
    for i in range(0, n, 2):
        for j in range(min(i+1, m)):
            grid[i-j][j] = arr[idx]
            idx += 1
    for j in range(n%2+1, m, 2):
        for i in range(min(m-j, n)):
            grid[n-1-i][j+i] = arr[idx]
            idx += 1

    for i in range(1, n, 2):
        for j in range(min(i+1, m)):
            grid[i-j][j] = arr[idx]
            idx += 1
    for j in range((n+1)%2+1, m, 2):
        for i in range(min(m-j, n)):
            grid[n-1-i][j+i] = arr[idx]
            idx += 1

    for r in grid: print(' '.join(str(e) for e in r))

t = int(input())
for i in range(t):
    solve()