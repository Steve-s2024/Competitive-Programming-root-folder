# brilliant tackle, almost run out of time, I tink this deserve to be the
# most difficult question so far solved on codeforces. I gambled the last bit
# with the binary search range, and it turns out indeed only falls into [1, 16]
# otherwise my solution will need more than 7 commands to do the job
# I don't know how so many people actually solved it, I'd say it is around 1600 to 1700
# not to mention the interactive feature really give me a hard time sending and receiving
# stuff with the judge

import sys

def printOut(msg):
    print(msg)
    sys.stdout.flush()
    res = int(input())
    if res == -1:
        sys.exit()
    return res

def solve():
    n = int(input())
    printOut('digit')
    printOut('digit')
    l, r = 1, 16
    while l < r:
        m = (l+r)//2
        res = printOut('add ' + str(-m))
        if res == 1:
            l, r = 1, r-m
        else:
            r = m

    printOut('add ' + str(n-1))
    printOut('!')



t = int(input())
for i in range(t):
    solve()


