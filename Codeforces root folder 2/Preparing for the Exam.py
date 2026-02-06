# tle, the test case requires to read 30,000 numbers from console
# as inputs and run the algorithm under 1500ms, this is just nuts!
t = int(input())
for i in range(t):
    [n, m, k] = [int(e) for e in input().split(' ')]
    exclude = [int(e) for e in input().split(' ')]
    known = [int(e) for e in input().split(' ')]
    if n == k:
        print('1'*m)
    elif n == k+1:
        res = ''
        for i in range(m):
            if exclude[i] in known:
                # screwed
                res += '0'
            else:
                res += '1'
        print(res)
    else:
        print('0'*m)