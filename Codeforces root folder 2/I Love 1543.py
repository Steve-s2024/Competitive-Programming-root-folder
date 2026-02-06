# how the fk this get accepted... I thought that I did not
# handle the case for n or m as odd number (which means the
# core layer is not reached by the program), but this actually
# passed...
# holy im fking lucky, n and m are even numbers as mentioned in the
# problem but I didn't notice that before submitting.
def solve():
    n, m = [int(e) for e in input().split()]
    grid = []
    for i in range(n):
        grid.append(input())

    # print(grid)

    res = 0
    top, left = 0, 0
    while True:
        arr = []
        for c in range(left, m-left):
            arr.append(grid[top][c])
        for r in range(top+1, n-top-1):
            arr.append(grid[r][m-left-1])
        for c in range(m-left-1, left-1, -1):
            arr.append(grid[n-top-1][c])
        for r in range(n-top-2, top, -1):
            arr.append(grid[r][left])
        # print(arr)
        size = len(arr)
        for i in range(size):
            a, b, c, d = arr[i], arr[(i+1)%size], arr[(i+2)%size], arr[(i+3)%size]
            if a+b+c+d == '1543':
                res += 1

        left += 1
        top += 1
        if top >= n//2 or left >= m//2:
            break
    print(res)




t = int(input())
for i in range(t):
    solve()
