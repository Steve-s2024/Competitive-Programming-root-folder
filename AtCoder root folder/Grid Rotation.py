# stupid rotation, Just fking play with my mind

def solve():
    n = int(input())
    S, T = [], []
    for i in range(n):
        row = input()
        S.append(row)
    for i in range(n):
        row = input()
        T.append(row)
    print()
    cnt = [0] * 4
    for r in range(n):
        for c in range(n):
            if S[r][c] != T[r][c]:
                cnt[0] += 1
            if S[n-1-c][r] != T[r][c]:
                cnt[1] += 1
            if S[n-1-r][n-1-c] != T[r][c]:
                cnt[2] += 1
            if S[c][n-1-r] != T[r][c]:
                cnt[3] += 1
    # print(cnt)
    print(min([cnt[0], cnt[1]+1, cnt[2]+2, cnt[3]+3]))
solve()
