# this solution is not much different than the one below
# we still greedily build the array non-dynamically, except
# that for the sole n = 6 test case, we set default value for
# it because my program only support n >= 7,not sure if this
# solution is intended
def solve():
    n = int(input())
    if n == 6:
        print('1 1 2 3 1 2')
    else:
        res = ['1']
        for i in range(2, n-1):
            res.append(str(i))
        res.append('1')
        res.append(str(n-5))
        print(' '.join(res))



t = int(input())
for tt in range(t):
    solve()



# so many constraints to build the array, and all of them
# are related to one number 'n', very annoying, this is deprecated
def solve():
    n = int(input())
    # m = n
    # n, m -->
    # construct an array with arr[i] in range(1, n+1)
    # longest palindrome subsequence count > m

    # candidates --> 1, 2, 3, 4.. n-1, n

    res = ['1']
    for i in range(2, n+1):
        res.append(str(i))
    res.append('1')
    res.append(str(n))
    print(' '.join(res))



t = int(input())
for tt in range(t):
    solve()
