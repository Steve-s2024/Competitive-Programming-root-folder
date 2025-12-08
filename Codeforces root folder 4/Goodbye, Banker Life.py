# goddamn not satisfying problem, I'm pretty deviated from the good path and start to make un-evident supported
# claims and with not moderate amount of them. though it worked in this case I think either the problem is designed
# badly such that 1700 participant can only solve it this way, or I must be not thinking in the right direction

# my recursive solution, runs pretty fast and worked in first attempt.

# k = 1
# arr = [k]
# n = 20
# print(' '*n + str(k))
# for i in range(1, n):
#     tmp = [arr[0]]
#     for j in range(i-1):
#         tmp.append(arr[j]^arr[j+1])
#     tmp.append(arr[-1])
#     arr = tmp
#     print(' '*(n-i), end = '')
#     print(' '.join(str(e) for e in tmp))


def solve():
    n, k = [int(e) for e in input().split()]
    pw = 1
    while pw < n: pw *= 4
    pw //= 4

    def recursive(n, pw):
        nonlocal k
        if n == 1:
            return [k]
        elif n == 2:
            return [k, k]
        elif n == 3:
            return [k, 0, k]
        elif n == 4:
            return [k, k, k, k]

        ct = 1
        while ct * pw < n: ct += 1
        nw = n - (ct - 1) * pw
        res = recursive(nw, pw // 4)

        m = len(res)
        if ct == 1:
            return res
        elif ct == 2:
            return res + [0] * (n - 2 * m) + res
        elif ct == 3:
            return res + [0] * (n - 2 * m) + res
        else:
            zeros = [0] * ((n - 4 * m) // 3)
            return res + zeros + res + zeros + res + zeros + res

    # print(recursive(n, pw))
    res = recursive(n, pw)
    print(' '.join(str(e) for e in res))


t = int(input())
for i in range(t): solve()
# 17
# 1 1
# 2 1
# 3 1
# 4 1
# 5 1
# 6 1
# 7 1
# 8 1
# 9 1
# 10 1
# 11 1
# 12 1
# 13 1
# 14 1
# 15 1
# 16 1
# 17 1