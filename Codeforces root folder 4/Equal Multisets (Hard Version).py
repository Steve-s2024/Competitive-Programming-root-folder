# im appalled😱. 3 wrong answer, but this passed being hardly different from the rest.
# asshole cf give such a hard time for me fixing mini bug...


def solve():
    n, k = [int(e) for e in input().split()]
    A = [int(e) for e in input().split()]
    B = [int(e) for e in input().split()]
    for i in range(k):
        for j in range(i, n, k):
            # print(B)
            if j+k < n and A[j] != A[j+k]:
                if B[j] not in [-1, A[j]] or B[j+k] not in [-1, A[j+k]]:
                    print('No')
                    return
                B[j] = A[j]
            if B[j] == -1: continue

            for l in range(j-k, -1, -k):
                if A[l] == A[l+k]:
                    if B[l] != B[l+k] and B[l] != -1:
                        print('No')
                        return
                    B[l] = B[l+k]
                else:
                    if B[l+k] != A[l+k] or (B[l] != A[l] and B[l] != -1):
                        print('No')
                        return
                    B[l] = A[l]
            for r in range(j+k, n, k):
                if A[r] == A[r-k]:
                    if B[r] != B[r-k] and B[r] != -1:
                        print('No')
                        return
                    B[r] = B[r-k]
                else:
                    if B[r-k] != A[r-k] or (B[r] != A[r] and B[r] != -1):
                        print('No')
                        return
                    B[r] = A[r]
            break

    # print(B)

    mp1 = [0] * (n + 1)
    mp2 = [0] * (n + 1)
    for i in range(k):
        mp1[A[i]] += 1
        if B[i] != -1: mp2[B[i]] += 1
    for i in range(1, n + 1):
        if mp2[i] > mp1[i]:
            print('No')
            return
    print('Yes')

for _ in range(int(input())): solve()

