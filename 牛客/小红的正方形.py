# a tedious square checker (not necessarily work for rectangle)
# check the intersection point of two squares

def helper(a, b):
    ar = sorted([a, b])
    if ar[0][1] in range(ar[1][0] + 1, ar[1][1] + 1): return True

    if ar[0][1] > ar[1][1]: return '*'
    return False


def solve():
    A = [int(e) for e in input().split()]
    B = [int(e) for e in input().split()]

    ar = [A[1], A[3]]
    ar.sort()
    for a in [A[0], A[2]]:
        for b in [B[0], B[2]]:
            if a == b and helper(ar, sorted([B[1], B[3]])):
                print('inf')
                return

    ar = [A[0], A[2]]
    ar.sort()
    for a in [A[1], A[3]]:
        for b in [B[1], B[3]]:
            if a == b and helper(ar, sorted([B[0], B[2]])):
                print('inf')
                return

    for x, y in [[A[0], A[1]], [A[2], A[3]], [A[0], A[3]], [A[2], A[1]]]:
        for X, Y in [[B[0], B[1]], [B[2], B[3]], [B[0], B[3]], [B[2], B[1]]]:
            if x == X and y == Y:
                print(1)
                return

    s = helper(sorted([A[0], A[2]]), sorted([B[0], B[2]]))
    t = helper(sorted([A[1], A[3]]), sorted([B[1], B[3]]))

    if s and t and (s != '*' or t != '*'):
        print(2)
        return

    print(0)


solve()