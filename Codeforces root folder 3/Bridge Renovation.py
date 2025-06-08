# holy I did not expect this O(1) to work...
# funny question, all I did is translate it into a combining ball question and try to find the greedy approach from there.

# the question is: group one, two, three all have n balls, the value of ball in each
# group is 18, 21, 25. I am allowed to do unlimited number of operation on the balls,
#           the operation --> combine any two balls into one ball, the one ball value
#           cannot exceed 60 after the operation, and its value after operation will be
#           the sum of the two balls which it composed of.
#
# now the question is, find the minimum number of balls remain after all operations.

def solve():
    n = int(input())
    fst = 2*n // 3
    scd = n // 2
    trd = 2*n % 3 + n % 2
    if trd == 3:
        print(fst + scd + 2)
    elif trd > 0:
        print(fst + scd + 1)
    else:
        print(fst + scd)
t = int(input())
for i in range(t):
    solve()
