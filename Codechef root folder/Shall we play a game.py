# relatively acceptable difficulty
# cook your dish here
t = int(input())
for x in range(t):
    n = int(input())
    # the first round alice choose 2^0
    # then bob choose 2^1
    # alice -> -2^2
    # bob -> -2^3
    # alice -> 2^4
    res = 0
    cnt = 0
    max_, min_ = 0, 0
    powOfTwo = 1
    for i in range(n):

        if cnt < 2:
            res += powOfTwo
        else:
            res -= powOfTwo
        max_ = max(max_, res)
        min_ = min(min_, res)
        powOfTwo *= 2
        cnt += 1;
        cnt %= 4;
    print((max_ - min_) % 998244353)
